from __future__ import annotations

from app.models.schemas import AgentLogEntry


class AgentLogger:
    def __init__(self) -> None:
        self._entries: list[AgentLogEntry] = []

    def add_many(self, entries: list[AgentLogEntry]) -> None:
        self._entries.extend(entries)

    def dump(self) -> list[AgentLogEntry]:
        return self._entries[:]
