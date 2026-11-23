import json
import sys
from pathlib import Path
from unittest.mock import Mock
import zipfile

import requests

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
import topic_mirrors as mirrors


def test_snapshot_queries_check_v1_date_and_boolean_terms(tmp_path):
    archive = tmp_path / "test.zip"
    items = []
    for identifier, day, abstract in [
        ("2601.00101", "02 Jan 2026", "humanoid navigation"),
        ("2601.00102", "01 Jan 2026", "humanoid navigation"),
        ("2601.00103", "03 Jan 2026", "humanoid navigation with drones"),
        ("2601.00104", "04 Jan 2026", "humanoid navigation"),
    ]:
        items.append(
            dict(
                id=identifier,
                title="Paper",
                abstract=abstract,
                authors_parsed=[["Lin", "A", ""]],
                versions=[dict(version="v1", created=day + " 00:00:00 GMT")],
            )
        )
    with zipfile.ZipFile(archive, "w") as f:
        f.writestr(
            "arxiv-metadata-oai-snapshot.json", "\n".join(json.dumps(x) for x in items)
        )
    db = mirrors.build_snapshot(tmp_path, "2026-01-02", "2026-01-04", archive)
    try:
        rows = mirrors.snapshot_matches(db, "humanoid AND navigation AND NOT drones")
        assert [r["id"] for r in rows] == ["2601.00101"]
        assert rows[0]["published"] == "2026-01-02"
    finally:
        db.close()


def test_semantic_dates_require_explicit_v1(monkeypatch):
    rows = [dict(id=f"2601.0000{i}", source="arxiv") for i in range(3)]
    monkeypatch.setattr(mirrors, "semantic_candidates", lambda *_: rows)
    dates = [("2026-01-02", "v1"), ("2026-01-03", "v2"), ("2026-01-04", "v1")]
    response = Mock()
    response.json.return_value = {
        "data": [
            {
                "id": "10.48550/arxiv." + r["id"],
                "attributes": {
                    "dates": [dict(date=day, dateType="Submitted", dateInformation=v)]
                },
            }
            for r, (day, v) in zip(rows, dates)
        ]
    }
    monkeypatch.setattr(mirrors.requests, "get", lambda *a, **k: response)
    verified = mirrors.verified_semantic_rows("x", "2026-01-01", "2026-01-04")
    assert [r["id"] for r in verified] == ["2601.00000"]


def test_rate_limit_switches_to_single_snapshot(tmp_path, monkeypatch):
    resp = requests.Response()
    resp.status_code = 429
    lookup = Mock(side_effect=requests.HTTPError(response=resp))
    db = Mock()
    db.execute.return_value.fetchone.return_value = ("2026-01-31",)
    build = Mock(return_value=db)
    monkeypatch.setattr(mirrors, "verified_semantic_rows", lookup)
    monkeypatch.setattr(mirrors, "build_snapshot", build)
    monkeypatch.setattr(mirrors, "snapshot_matches", lambda _, q: [q])
    provider = mirrors.TopicMirrors(tmp_path, "2026-01-01", "2026-02-01")
    assert provider.retrieve("a") == ("cornell_snapshot", ["a"])
    assert provider.retrieve("b") == ("cornell_snapshot", ["b"])
    lookup.assert_called_once()
    build.assert_called_once()
    provider.close()
    db.close.assert_called_once()
