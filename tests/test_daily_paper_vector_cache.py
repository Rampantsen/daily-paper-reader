from pathlib import Path
import sys
from types import SimpleNamespace

import numpy as np
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from filter import compute_embeddings


class Encoder:
    model_name = "test-model-v1"
    endpoint = "https://example.invalid/embed"
    max_text_chars = 2000
    allow_local_fallback = False

    def __init__(self):
        self.batches = []
        self.fail_batch = None

    def encode(self, texts, **kwargs):
        self.batches.append(texts)
        if self.fail_batch == len(self.batches):
            raise RuntimeError("interrupted")
        return np.array([[len(t), ord(t[0])] for t in texts], dtype=np.float32)


def test_interruption_resume_in_new_order_and_invalidation(tmp_path, monkeypatch):
    monkeypatch.setenv(
        "DPR_PAPER_VECTOR_CACHE", str(tmp_path / "cache" / "vectors.sqlite")
    )
    items = [
        SimpleNamespace(id=t, text_for_embedding=t)
        for t in ["one", "two", "three", "four"]
    ]
    model = Encoder()
    model.fail_batch = 2
    with pytest.raises(RuntimeError, match="interrupted"):
        compute_embeddings(model, items, batch_size=2)
    model = Encoder()
    reordered = [items[2], items[0], items[3], items[1], items[2]]
    result = compute_embeddings(model, reordered, batch_size=2)
    assert model.batches == [["three", "four"]]
    np.testing.assert_array_equal(
        result, Encoder().encode([p.text_for_embedding for p in reordered])
    )
    items[0].text_for_embedding = "changed"
    compute_embeddings(model, items, batch_size=2)
    assert model.batches[-1] == ["changed"]
    model.model_name = "test-model-v2"
    model.batches.clear()
    compute_embeddings(model, items, batch_size=2)
    assert model.batches == [["changed", "two"], ["three", "four"]]
