"""Bounded Topic Research retrieval using the public arXiv API."""

from datetime import date, timedelta

from query_boolean import parse_boolean_expr
from long_range_review import fingerprint, write_json
from paper_dates import resolve_publication_date, publication_window_status
import time
import json
from pathlib import Path


def _expression(node, window):
    if node is None:
        raise ValueError("无效的 arXiv 检索表达式")
    if node.kind == "TERM":
        field, value = "all", node.value
        if value.lower().startswith("author:"):
            field, value = "au", value.split(":", 1)[1]
        return f'{field}:"{value.replace(chr(34), " ")}"'
    if node.kind == "NOT":
        return f"({window} ANDNOT {_expression(node.left, window)})"
    return f"({_expression(node.left, window)} {node.kind} {_expression(node.right, window)})"


def _query_results(client, search):
    import arxiv

    for attempt in range(3):
        try:
            return list(client.results(search))
        except arxiv.HTTPError as exc:
            if exc.status != 429 or attempt == 2:
                raise
            delay = 60 * (2 ** attempt)
            print(f"[arXiv API] 请求受限，等待 {delay} 秒后重试", flush=True)
            time.sleep(delay)


def add_arxiv_results(result, plan, root):
    import arxiv

    start, end = plan["arxiv_start"], plan["as_of"]
    last_day = date.fromisoformat(end) - timedelta(days=1)
    window = f"submittedDate:[{start.replace('-', '')}0000 TO {last_day:%Y%m%d}2359]"
    keywords = [
        t["query"]["query_text"]
        for t in plan["tasks"]
        if t["source"] == "arxiv" and t["lane"] == "bm25"
    ]
    queries = list(dict.fromkeys(keywords or plan["profile"]["queries"]))
    if not queries:
        raise ValueError("没有可用的 arXiv 专题检索词")
    cache = Path(root) / ".local-runs/starter-pack-cache/retrieval/arxiv-api"
    cache.mkdir(parents=True, exist_ok=True)
    client = arxiv.Client(page_size=100, delay_seconds=3, num_retries=3)
    papers = {}
    for query in queries:
        expression = _expression(parse_boolean_expr(query), window)
        search = arxiv.Search(
            query=f"({expression}) AND {window}",
            max_results=100,
            sort_by=arxiv.SortCriterion.Relevance,
        )
        key = fingerprint(["arxiv-api-v1", search.query, search.max_results])
        path = cache / f"{key}.json"
        restored = path.exists()
        if restored:
            rows = json.loads(path.read_text())
        else:
            rows = []
            for hit in _query_results(client, search):
                row = dict(
                    id=hit.get_short_id(),
                    title=hit.title,
                    abstract=hit.summary,
                    published=hit.published.isoformat(),
                    link=hit.entry_id,
                    pdf_url=hit.pdf_url,
                    authors=[a.name for a in hit.authors],
                    categories=hit.categories,
                    primary_category=hit.primary_category,
                    doi=hit.doi,
                    source="arxiv",
                    retrieval_source="arxiv",
                )
                row.update(resolve_publication_date(row))
                row["publication_window_status"] = publication_window_status(
                    row, start, end
                )
                if row["publication_window_status"] == "included":
                    rows.append(row)
            write_json(path, rows)
        for rank, row in enumerate(rows, 1):
            record = papers.setdefault(row["id"], dict(row, retrieval_evidence=[]))
            record["retrieval_evidence"].append(
                dict(lane="arxiv_relevance", query_text=query, task_key=key, rank=rank)
            )
        result["tasks"].append(
            dict(
                key=key,
                source="arxiv",
                lane="arxiv_relevance",
                query_text=query,
                start=start,
                end_exclusive=end,
                status="done",
                restored=restored,
                bounded=True,
                raw_count=len(rows),
            )
        )
        print(f"[arXiv API] {query}: {len(rows)} 篇", flush=True)
    result["papers"].extend(papers.values())
    result["coverage"].update(
        arxiv_keyword="arXiv API relevance top100/query",
        arxiv_vector="disabled",
        note="arXiv API 按检索词返回相关度前100篇，合并去重后进入专题重排。",
    )
    return result
