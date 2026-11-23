"""Convert a public PDF with the MinerU precision parsing API."""

from pathlib import PurePosixPath
import tempfile
import time
import zipfile

import requests

API = "https://mineru.net/api/v4/extract/task"


def _data(response):
    response.raise_for_status()
    payload = response.json()
    if payload.get("code") != 0:
        raise ValueError("MinerU refused the request")
    return payload["data"]


def extract_markdown(pdf_url, token):
    headers = {"Authorization": f"Bearer {token}"}
    task = _data(
        requests.post(
            API,
            headers=headers,
            json={"url": pdf_url, "model_version": "vlm"},
            timeout=30,
            allow_redirects=False,
        )
    )
    deadline = time.monotonic() + 180
    while time.monotonic() < deadline:
        result = _data(
            requests.get(
                f"{API}/{task['task_id']}",
                headers=headers,
                timeout=20,
                allow_redirects=False,
            )
        )
        if result["state"] == "done":
            break
        if result["state"] == "failed":
            raise ValueError("MinerU parsing failed")
        time.sleep(5)
    else:
        raise TimeoutError("MinerU polling deadline exceeded")

    with (
        tempfile.TemporaryFile() as archive,
        requests.get(result["full_zip_url"], stream=True, timeout=30) as download,
    ):
        download.raise_for_status()
        for chunk in download.iter_content(1024 * 1024):
            archive.write(chunk)
            if archive.tell() > 256 * 1024 * 1024:
                raise ValueError("MinerU result exceeds the archive size limit")
        with zipfile.ZipFile(archive) as contents:
            for entry in contents.infolist():
                if PurePosixPath(entry.filename).name == "full.md":
                    if entry.file_size > 16 * 1024 * 1024:
                        raise ValueError("MinerU Markdown exceeds the text size limit")
                    return contents.read(entry).decode("utf-8")
    raise ValueError("MinerU archive is missing full.md")
