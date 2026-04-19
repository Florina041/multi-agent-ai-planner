from __future__ import annotations

import uuid

from app.storage.migrations import run_migrations
from app.storage.repositories import InteractionRepository
from app.utils.constants import DEFAULT_DATABASE_PATH

from app.agents.collector_agent import CollectorAgent
from app.agents.analyzer_agent import AnalyzerAgent
from app.agents.planner_agent import PlannerAgent
from app.agents.decision_agent import DecisionAgent
from app.agents.response_agent import ResponseAgent
from app.agents.memory_agent import MemoryAgent

from app.services.rag_service import RAGService
from app.services.evaluation_service import EvaluationService
from app.services.tool_service import ToolService

from app.llm.openai_provider import OpenAIProvider
from app.llm.gemini_provider import GeminiProvider


class MultiAgentOrchestrator:
    def __init__(self, db_path: str = DEFAULT_DATABASE_PATH) -> None:
        run_migrations(db_path)

        self.repo = InteractionRepository(db_path=db_path)

        # 🔥 LLM AUTO-SELECTION
        llm = OpenAIProvider()
        if not llm.available():
            llm = GeminiProvider()

        self.llm = llm

        # 🔥 PASS LLM TO AGENTS
        self.collector = CollectorAgent(llm=self.llm)
        self.analyzer = AnalyzerAgent(llm=self.llm)
        self.planner = PlannerAgent(llm=self.llm)

        self.decision = DecisionAgent()
        self.response = ResponseAgent()
        self.memory = MemoryAgent(self.repo)

        self.rag = RAGService()
        self.evaluator = EvaluationService()
        self.tool = ToolService()