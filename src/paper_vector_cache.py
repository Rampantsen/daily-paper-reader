"""Resumable, ordered encoding of paper batches for the daily remote embedding job."""

from contextlib import closing
import hashlib
import json
from pathlib import Path
import sqlite3

import numpy as np


def encode_with_checkpoints(path, model, ids, texts, encode_kwargs, max_length, log):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    # Store only a digest of the endpoint; some custom URLs contain credentials.
    identity = [
        1,
        model.model_name,
        model.endpoint,
        model.max_text_chars,
        max_length,
        encode_kwargs["normalize_embeddings"],
    ]
    namespace = hashlib.sha256(json.dumps(identity).encode()).hexdigest()
    keys = [
        (pid, hashlib.sha256(text.encode()).digest()) for pid, text in zip(ids, texts)
    ]
    vectors = {}
    missing = {}
    batch_size = encode_kwargs["batch_size"]

    with closing(sqlite3.connect(path, timeout=30)) as db:
        db.execute("""CREATE TABLE IF NOT EXISTS vectors (
            model TEXT, paper TEXT, content BLOB, vector BLOB NOT NULL,
            PRIMARY KEY (model, paper, content)) WITHOUT ROWID""")
        for key, text in zip(keys, texts):
            if key in vectors or key in missing:
                continue
            row = db.execute(
                "SELECT vector FROM vectors WHERE model=? AND paper=? AND content=?",
                (namespace, *key),
            ).fetchone()
            if row is None:
                missing[key] = text
            else:
                vectors[key] = np.frombuffer(row[0], dtype="<f4")
        entries = list(missing.items())
        log(
            f"论文向量缓存：命中 {len(vectors)}，待计算 {len(entries)}（按唯一论文和文本计）"
        )
        for offset in range(0, len(entries), batch_size):
            batch = entries[offset : offset + batch_size]
            values = np.asarray(
                model.encode([text for _, text in batch], **encode_kwargs), dtype="<f4"
            )
            if (
                values.ndim != 2
                or values.shape[0] != len(batch)
                or not values.shape[1]
                or not np.isfinite(values).all()
            ):
                raise ValueError("远程论文向量批次不完整或包含无效值")
            with db:
                db.executemany(
                    "INSERT OR REPLACE INTO vectors VALUES (?,?,?,?)",
                    [
                        (namespace, *key, value.tobytes())
                        for (key, _), value in zip(batch, values)
                    ],
                )
            for (key, _), value in zip(batch, values):
                vectors[key] = value
            completed = offset + len(batch)
            if completed == len(entries) or completed % (20 * batch_size) == 0:
                log(f"本轮新增论文向量已保存：{completed}/{len(entries)}")
    return np.stack([vectors[key] for key in keys])
