from __future__ import annotations

import json

from app.storage.db import get_connection


class InteractionRepository:
    def __init__(self, db_path: str) -> None:
        self.db_path = db_path

    def insert_interaction(self, payload: dict) -> None:
        conn = get_connection(self.db_path)
        cur = conn.cursor()
        cur.execute(
            """
            INSERT INTO interactions (
                session_id, timestamp, domain, raw_input,
                extracted_json, analysis_json, plans_json,
                decision_json, response_json
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                payload["session_id"],
                payload["timestamp"],
                payload["domain"],
                payload["raw_input"],
                json.dumps(payload["extracted_json"]),
                json.dumps(payload["analysis_json"]),
                json.dumps(payload["plans_json"]),
                json.dumps(payload["decision_json"]),
                json.dumps(payload["response_json"]),
            ),
        )
        conn.commit()
        conn.close()

    def get_recent(self, limit: int = 10) -> list[dict]:
        conn = get_connection(self.db_path)
        cur = conn.cursor()
        cur.execute(
            """
            SELECT * FROM interactions ORDER BY id DESC LIMIT ?
            """,
            (limit,),
        )
        rows = cur.fetchall()
        conn.close()
        return [dict(row) for row in rows]

    def get_recent_by_session(self, session_id: str, limit: int = 5) -> list[dict]:
        conn = get_connection(self.db_path)
        cur = conn.cursor()
        cur.execute(
            """
            SELECT * FROM interactions
            WHERE session_id = ?
            ORDER BY id DESC
            LIMIT ?
            """,
            (session_id, limit),
        )
        rows = cur.fetchall()
        conn.close()
        return [dict(row) for row in rows]
