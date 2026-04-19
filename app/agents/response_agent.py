from __future__ import annotations

from app.agents.base_agent import BaseAgent
from app.models.schemas import (
    AgentLogEntry,
    AnalysisReport,
    DecisionReport,
    FinalResponse,
    PlanOption,
    UserProfile,
)


class ResponseAgent(BaseAgent):
    name = "ResponseAgent"

    def run(
        self,
        profile: UserProfile,
        analysis: AnalysisReport,
        options: list[PlanOption],
        decision: DecisionReport,
        context: str | None = None,
    ) -> tuple[FinalResponse, list[AgentLogEntry]]:

        selected = next(
            (opt for opt in options if opt.plan_id == decision.selected_plan_id),
            options[0],
        )

        action_plan = []
        for milestone in selected.milestones:
            action_plan.append(
                f"{milestone.phase} ({milestone.duration_weeks} weeks): "
                + "; ".join(milestone.tasks)
            )

        warnings = (
            analysis.risks[:]
            if analysis.risks
            else ["No critical risks detected, but weekly consistency is essential."]
        )

        retrieved_knowledge = context if context else "No external knowledge used"

        response = FinalResponse(
            summary=f"{profile.domain.value.title()} planning recommendation generated for: {profile.goal or 'user goal'}.",
            extracted_information=profile.model_dump(),
            analysis=analysis.model_dump(),
            options=[{
                "plan_id": item.plan_id,
                "title": item.title,
                "description": item.description,
                "weekly_schedule": item.weekly_schedule,
            } for item in options],
            recommendation={
                "selected_plan_id": decision.selected_plan_id,
                "reasoning": decision.reasoning,
                "confidence_score": decision.confidence_score,
            },
            action_plan=action_plan,
            warnings=warnings,
            next_steps=[
                "Start week-1 tasks within 24 hours",
                "Track progress every Sunday",
                "Re-run planner after 2 weeks with updated constraints",
            ],
            retrieved_knowledge=retrieved_knowledge,
        )

        logs = [
            AgentLogEntry(
                agent=self.name,
                step="format_response",
                detail="Compiled all agent outputs into structured final response",
                confidence=0.91,
            )
        ]

        return response, logs