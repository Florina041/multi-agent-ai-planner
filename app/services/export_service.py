from __future__ import annotations

from pathlib import Path

from app.utils.constants import DEFAULT_EXPORT_DIR
from app.utils.helpers import now_iso, safe_json_dumps


class ExportService:
    def __init__(self, export_dir: str = DEFAULT_EXPORT_DIR) -> None:
        self.export_dir = Path(export_dir)
        self.export_dir.mkdir(parents=True, exist_ok=True)

    def export_json(self, session_id: str, payload: dict) -> str:
        filename = self.export_dir / f"{session_id}_{now_iso().replace(':', '-')}.json"
        filename.write_text(safe_json_dumps(payload), encoding="utf-8")
        return str(filename)

    def export_text(self, session_id: str, content: str) -> str:
        filename = self.export_dir / f"{session_id}_{now_iso().replace(':', '-')}.txt"
        filename.write_text(content, encoding="utf-8")
        return str(filename)
