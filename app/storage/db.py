from __future__ import annotations

import sqlite3
from pathlib import Path

from app.utils.constants import DEFAULT_DATABASE_PATH


def get_connection(db_path: str = DEFAULT_DATABASE_PATH) -> sqlite3.Connection:
    Path(db_path).parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn


def init_db(db_path: str = DEFAULT_DATABASE_PATH) -> None:
    conn = get_connection(db_path)
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS interactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            session_id TEXT NOT NULL,
            timestamp TEXT NOT NULL,
            domain TEXT NOT NULL,
            raw_input TEXT NOT NULL,
            extracted_json TEXT NOT NULL,
            analysis_json TEXT NOT NULL,
            plans_json TEXT NOT NULL,
            decision_json TEXT NOT NULL,
            response_json TEXT NOT NULL
        );
        """
    )
    conn.commit()
    conn.close()
