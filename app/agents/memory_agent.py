from __future__ import annotations

from app.agents.base_agent import BaseAgent
from app.models.schemas import AgentLogEntry
from app.storage.repositories import InteractionRepository


class MemoryAgent(BaseAgent):
    name = "MemoryAgent"

    def __init__(self, repo: InteractionRepository) -> None:
        self.repo = repo

    def run(self, action: str, payload: dict | None = None, session_id: str | None = None):
        if action == "recall" and session_id:
            return self.recall(session_id)
        if action == "store" and payload is not None:
            return self.store(payload)
        raise ValueError("Unsupported memory action")

    def recall(self, session_id: str) -> tuple[dict, list[AgentLogEntry]]:
        recent = self.repo.get_recent_by_session(session_id=session_id, limit=1)
        memory = recent[0] if recent else {}
        logs = [
            AgentLogEntry(
                agent=self.name,
                step="recall",
                detail="Loaded recent interaction context for personalization",
                confidence=0.82,
            )
        ]
        return memory, logs

    def store(self, payload: dict) -> list[AgentLogEntry]:
        self.repo.insert_interaction(payload)
        return [
            AgentLogEntry(
                agent=self.name,
                step="store",
                detail="Persisted interaction to memory store",
                confidence=0.9,
            )
        ]
