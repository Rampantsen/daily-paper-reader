"""Alternative metadata sources for date-bounded arXiv topic searches."""

from datetime import date, timedelta, timezone
from email.utils import parsedate_to_datetime
import json
from pathlib import Path
import re
import sqlite3
import tempfile
import zipfile

import requests

from paper_dates import publication_window_status, resolve_publication_date
from query_boolean import evaluate_expr, parse_boolean_expr

KAGGLE = "https://www.kaggle.com/api/v1/datasets/download/Cornell-University/arxiv"
SEMANTIC = "https://api.semanticscholar.org/graph/v1/paper/search/bulk"


def _quoted(term):
    return '"' + term.replace('"', '""') + '"'


def _semantic_expression(node):
    if node.kind == "TERM":
        # The Semantic Scholar bulk endpoint only searches titles and abstracts.
        if node.value.lower().startswith("author:"):
            raise ValueError("author queries require the metadata snapshot")
        return node.value if node.value.isalnum() else _quoted(node.value)
    if node.kind == "NOT":
        return "-(" + _semantic_expression(node.left) + ")"
    operator = " + " if node.kind == "AND" else " | "
    return (
        "("
        + _semantic_expression(node.left)
        + operator
        + _semantic_expression(node.right)
        + ")"
    )


def semantic_candidates(query, start, end):
    # Filter exact dates downstream. Journal publication dates can differ from arXiv v1.
    node = parse_boolean_expr(query)
    plain_terms = query.split()
    expression = (
        " + ".join(plain_terms)
        if plain_terms
        and all(
            term.isalnum() and term.upper() not in {"OR", "AND", "NOT"}
            for term in plain_terms
        )
        else _semantic_expression(node)
    )
    last_day = date.fromisoformat(end) - timedelta(days=1)
    response = requests.get(
        SEMANTIC,
        params={
            "query": expression,
            "fields": "title,abstract,externalIds,authors",
            "publicationDateOrYear": f"{start}:{last_day}",
        },
        timeout=(10, 30),
    )
    response.raise_for_status()
    rows = []
    for hit in response.json()["data"]:
        identifier = str((hit.get("externalIds") or {}).get("ArXiv") or "")
        match = re.fullmatch(r"(\d{2})(0[1-9]|1[0-2])\.\d{4,5}(?:v\d+)?", identifier)
        if not match or not hit.get("abstract") or not hit.get("title"):
            continue
        row = dict(
            id=identifier,
            title=hit["title"],
            abstract=hit["abstract"],
            authors=[a["name"] for a in hit.get("authors") or [] if a.get("name")],
            link=f"https://arxiv.org/abs/{identifier}",
            pdf_url=f"https://arxiv.org/pdf/{identifier}",
            source="arxiv",
            retrieval_source="arxiv",
        )
        rows.append(row)
    return rows[:300]


def verified_semantic_rows(query, start, end):
    candidates = semantic_candidates(query, start, end)
    verified = []
    for offset in range(0, len(candidates), 30):
        batch = candidates[offset : offset + 30]
        by_doi = {
            "10.48550/arxiv." + re.sub(r"v\d+$", "", row["id"]): row for row in batch
        }
        response = requests.get(
            "https://api.datacite.org/dois",
            params={
                "query": "id:(" + " OR ".join(_quoted(doi) for doi in by_doi) + ")",
                "page[size]": len(by_doi),
            },
            timeout=(10, 30),
        )
        response.raise_for_status()
        for item in response.json()["data"]:
            row = by_doi.get(item["id"].lower())
            if row is None:
                continue
            submitted = next(
                (
                    d["date"]
                    for d in item["attributes"].get("dates", [])
                    if d.get("dateType") == "Submitted"
                    and d.get("dateInformation") == "v1"
                ),
                None,
            )
            if not submitted:
                continue
            row["published"] = submitted
            row.update(resolve_publication_date(row))
            row["publication_date_source"] = "https://doi.org/" + item["id"]
            row["publication_window_status"] = publication_window_status(
                row, start, end
            )
            if row["publication_window_status"] == "included":
                verified.append(row)
        if len(verified) >= 100:
            break
    return verified[:100]


def _snapshot_row(record, published):
    identifier = record["id"]
    authors = [
        ", ".join(part for part in person if part)
        for person in record.get("authors_parsed", [])
    ]
    row = dict(
        id=identifier,
        title=record["title"],
        abstract=record["abstract"],
        authors=authors,
        categories=record.get("categories", "").split(),
        doi=record.get("doi"),
        source="arxiv",
        retrieval_source="arxiv",
        published=published,
        link=f"https://arxiv.org/abs/{identifier}",
        pdf_url=f"https://arxiv.org/pdf/{identifier}",
        publication_window_status="included",
    )
    row.update(resolve_publication_date(row))
    row["publication_date_source"] = (
        "Cornell arXiv metadata snapshot: versions[v1].created"
    )
    return row


def build_snapshot(directory, start, end, archive_path=None):
    database = Path(directory) / "index.sqlite"
    with tempfile.TemporaryFile(dir=directory) as download:
        if archive_path is None:
            with requests.get(KAGGLE, stream=True, timeout=(15, 90)) as response:
                response.raise_for_status()
                for chunk in response.iter_content(1024 * 1024):
                    download.write(chunk)
        with (
            zipfile.ZipFile(archive_path or download) as archive,
            sqlite3.connect(database) as db,
        ):
            db.execute("CREATE TABLE papers (id TEXT PRIMARY KEY, record TEXT)")
            db.execute(
                "CREATE VIRTUAL TABLE terms USING fts5(title, abstract, authors)"
            )
            earliest = start[2:7].replace("-", "").encode()
            latest = end[2:7].replace("-", "").encode()
            last_seen = ""
            with archive.open("arxiv-metadata-oai-snapshot.json") as entries:
                for line in entries:
                    # Modern IDs usually occur first. Skip decoding older years of metadata.
                    prefix = re.match(rb'\s*\{\s*"id"\s*:\s*"(\d{4})\.', line)
                    if prefix and not earliest[:2] <= prefix[1][:2] <= latest[:2]:
                        continue
                    record = json.loads(line)
                    first = next(
                        (v for v in record["versions"] if v["version"] == "v1"), None
                    )
                    if not first:
                        continue
                    published = (
                        parsedate_to_datetime(first["created"])
                        .astimezone(timezone.utc)
                        .date()
                        .isoformat()
                    )
                    if not start <= published < end:
                        continue
                    last_seen = max(last_seen, published)
                    row = _snapshot_row(record, published)
                    cursor = db.execute(
                        "INSERT INTO papers VALUES (?,?)", (row["id"], json.dumps(row))
                    )
                    db.execute(
                        "INSERT INTO terms(rowid,title,abstract,authors) VALUES (?,?,?,?)",
                        (
                            cursor.lastrowid,
                            row["title"],
                            row["abstract"],
                            " ; ".join(row["authors"]),
                        ),
                    )
            db.execute("CREATE TABLE coverage (latest_submission TEXT)")
            db.execute("INSERT INTO coverage VALUES (?)", (last_seen,))
            if not last_seen:
                raise ValueError("Cornell 快照没有覆盖请求的日期窗口")
            print(
                f"[Cornell] 所选窗口内快照最新 v1 提交日期: {last_seen or '无记录'}",
                flush=True,
            )
    return sqlite3.connect(database)


def _positive_terms(node, negated=False):
    if node.kind == "TERM":
        return [] if negated else [_quoted(node.value.removeprefix("author:"))]
    if node.kind == "NOT":
        return _positive_terms(node.left, not negated)
    return _positive_terms(node.left, negated) + _positive_terms(node.right, negated)


def snapshot_matches(db, query):
    node = parse_boolean_expr(query)
    terms = _positive_terms(node)
    # An OR with a negative branch can match rows without any positive term.
    if terms and "NOT" not in query.upper() and "!" not in query:
        hits = db.execute(
            "SELECT record FROM terms JOIN papers ON papers.rowid=terms.rowid "
            "WHERE terms MATCH ? ORDER BY bm25(terms, 3, 1, 1), papers.id",
            (" OR ".join(terms),),
        )
    else:
        hits = db.execute("SELECT record FROM papers ORDER BY id DESC")
    rows = []
    for (data,) in hits:
        row = json.loads(data)
        if evaluate_expr(node, row["title"], row["abstract"], row["authors"]):
            rows.append(row)
            if len(rows) == 100:
                break
    return rows


class TopicMirrors:
    def __init__(self, directory, start, end):
        self.directory = directory
        self.start = start
        self.end = end
        self.snapshot = None
        self.snapshot_latest = None
        self.semantic_limited = False

    def retrieve(self, query):
        if not self.semantic_limited:
            try:
                rows = verified_semantic_rows(query, self.start, self.end)
                if rows:
                    return "semantic_scholar", rows
            except (requests.RequestException, ValueError) as error:
                response = getattr(error, "response", None)
                self.semantic_limited = (
                    response is not None and response.status_code == 429
                )
                print(
                    f"[Semantic Scholar / DataCite] {type(error).__name__}，使用 Cornell 快照",
                    flush=True,
                )
        if self.snapshot is None:
            self.snapshot = build_snapshot(self.directory, self.start, self.end)
            self.snapshot_latest = self.snapshot.execute(
                "SELECT latest_submission FROM coverage"
            ).fetchone()[0]
        return "cornell_snapshot", snapshot_matches(self.snapshot, query)

    def close(self):
        if self.snapshot is not None:
            self.snapshot.close()
