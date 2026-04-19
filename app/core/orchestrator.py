from __future__ import annotations

import uuid

from app.agents.analyzer_agent import AnalyzerAgent
from app.agents.collector_agent import CollectorAgent
from app.agents.decision_agent import DecisionAgent
from app.agents.memory_agent import MemoryAgent
from app.agents.planner_agent import PlannerAgent
from app.agents.response_agent import ResponseAgent

from app.models.enums import WorkflowStatus
from app.models.schemas import WorkflowResult

from app.services.logging_service import AgentLogger
from app.services.rag_service import RAGService
from app.services.evaluation_service import EvaluationService
from app.services.tool_service import ToolService

from app.storage.migrations import run_migrations
from app.storage.repositories import InteractionRepository

from app.utils.constants import DEFAULT_DATABASE_PATH
from app.utils.helpers import now_iso


class MultiAgentOrchestrator:
    def __init__(self, db_path: str = DEFAULT_DATABASE_PATH) -> None:
        run_migrations(db_path)

        self.repo = InteractionRepository(db_path=db_path)

        self.collector = CollectorAgent()
        self.analyzer = AnalyzerAgent()
        self.planner = PlannerAgent()
        self.decision = DecisionAgent()
        self.response = ResponseAgent()
        self.memory = MemoryAgent(self.repo)

        # ✅ NEW
        self.rag = RAGService()
        self.evaluator = EvaluationService()
        self.tool = ToolService()

    def run(self, user_text: str, domain: str, session_id: str | None = None) -> WorkflowResult:
        session = session_id or str(uuid.uuid4())
        logger = AgentLogger()

        _, memory_logs = self.memory.recall(session)
        logger.add_many(memory_logs)

        profile, collector_logs = self.collector.run(user_text=user_text, domain=domain)
        logger.add_many(collector_logs)

        # 🔍 RAG
        context = self.rag.retrieve(user_text)

        if profile.missing_fields:
            return WorkflowResult(
                status=WorkflowStatus.NEED_CLARIFICATION.value,
                session_id=session,
                questions=profile.follow_up_questions,
                user_profile=profile,
                agent_logs=logger.dump(),
            )

        analysis, analyzer_logs = self.analyzer.run(profile)
        logger.add_many(analyzer_logs)

        options, planner_logs = self.planner.run(profile, analysis)
        logger.add_many(planner_logs)

        decision, decision_logs = self.decision.run(analysis, options)
        logger.add_many(decision_logs)

        final_response, response_logs = self.response.run(
            profile, analysis, options, decision, context
        )
        logger.add_many(response_logs)

        # 📊 Evaluation
        score = self.evaluator.evaluate(str(final_response), context)

        # 🛠 Tool
        tool_output = self.tool.estimate_study_hours(4, 24)

        memory_payload = {
            "session_id": session,
            "timestamp": now_iso(),
            "domain": profile.domain.value,
            "raw_input": profile.raw_input,
            "extracted_json": profile.model_dump(),
            "analysis_json": analysis.model_dump(),
            "plans_json": [item.model_dump() for item in options],
            "decision_json": decision.model_dump(),
            "response_json": final_response.model_dump(),
            "rag_context": context,
            "faithfulness_score": score,
            "tool_output": tool_output,
        }

        memory_logs = self.memory.store(memory_payload)
        logger.add_many(memory_logs)

        result = WorkflowResult(
            status=WorkflowStatus.COMPLETE.value,
            session_id=session,
            user_profile=profile,
            analysis_report=analysis,
            plan_options=options,
            decision_report=decision,
            final_response=final_response,
            agent_logs=logger.dump(),
        )

        # attach extra fields
        result.rag_context = context
        result.faithfulness_score = score
        result.tool_output = tool_output

        return result

    def get_history(self, limit: int = 20) -> list[dict]:
        return self.repo.get_recent(limit=limit)