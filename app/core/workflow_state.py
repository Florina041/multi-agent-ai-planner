from __future__ import annotations

from dataclasses import dataclass, field

from app.models.schemas import AgentLogEntry


@dataclass
class WorkflowState:
    session_id: str
    logs: list[AgentLogEntry] = field(default_factory=list)

    def append_logs(self, entries: list[AgentLogEntry]) -> None:
        self.logs.extend(entries)
