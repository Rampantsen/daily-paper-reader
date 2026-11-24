from datetime import datetime, timezone
import json
from pathlib import Path
import sys
from unittest.mock import Mock

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from maintain.fetchers import fetch_arxiv as fetch


class Clock(datetime):
    @classmethod
    def now(cls, tz=None):
        return cls(2026, 11, 24, 1, 49, tzinfo=timezone.utc)


@pytest.mark.parametrize(
    ("days", "full_window", "first_minute"),
    [
        (30, True, "202610260000"),
        (1, True, "202611240000"),
        (9, False, "202611201859"),
    ],
)
def test_requested_window_keeps_seen_ids_and_incremental_cursor(
    tmp_path, monkeypatch, days, full_window, first_minute
):
    cursor = Clock(2026, 11, 20, 18, 59, 57, tzinfo=timezone.utc)
    monkeypatch.setattr(fetch, "datetime", Clock)
    monkeypatch.setattr(fetch, "CATEGORIES_TO_FETCH", ["cs"])
    monkeypatch.setattr(fetch, "load_config", lambda: {})
    monkeypatch.setattr(fetch, "load_seen_state", lambda: ({"seen"}, cursor))
    save = Mock()
    monkeypatch.setattr(fetch, "save_seen_state", save)
    monkeypatch.setattr(fetch, "save_last_crawl_at", Mock())
    older = Mock(
        title="Older paper",
        summary="Abstract",
        authors=[],
        pdf_url="url",
        primary_category="cs",
        categories=["cs"],
        published=Clock(2026, 11, 1, tzinfo=timezone.utc),
    )
    older.get_short_id.return_value = "older"
    seen = Mock()
    seen.get_short_id.return_value = "seen"
    queries = []

    def results(search):
        queries.append(search.query)
        return [older, seen] if "202610260000" in search.query else [seen]

    monkeypatch.setattr(fetch.arxiv, "Client", lambda **kwargs: Mock(results=results))
    output = tmp_path / "raw.json"
    fetch.fetch_all_domains_metadata_robust(
        days, str(output), full_window=full_window, disable_supabase_read=True
    )
    assert f"[{first_minute} TO " in queries[0]
    assert queries[-1].endswith(" TO 202611240149]")
    backfilled = full_window and days == 30
    assert [p["id"] for p in json.loads(output.read_text())] == (
        ["older"] if backfilled else []
    )
    save.assert_called_once_with({"seen", "older"} if backfilled else {"seen"}, cursor)
