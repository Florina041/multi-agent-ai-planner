from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from typing import Any


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def safe_json_dumps(payload: Any) -> str:
    return json.dumps(payload, indent=2, ensure_ascii=True)


def keyword_score(text: str, keywords: list[str]) -> int:
    lower_text = text.lower()
    return sum(1 for item in keywords if item in lower_text)


def extract_first_number(text: str, pattern: str) -> int | None:
    match = re.search(pattern, text, flags=re.IGNORECASE)
    if not match:
        return None
    try:
        return int(match.group(1))
    except (TypeError, ValueError):
        return None
