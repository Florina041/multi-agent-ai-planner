from __future__ import annotations

from app.agents.base_agent import BaseAgent
from app.core.scoring_engine import score_plan
from app.models.schemas import AgentLogEntry, AnalysisReport, DecisionReport, PlanOption


class DecisionAgent(BaseAgent):
    name = "DecisionAgent"

    def run(self, analysis: AnalysisReport, options: list[PlanOption]) -> tuple[DecisionReport, list[AgentLogEntry]]:
        ranked = []
        for option in options:
            score = score_plan(option)
            ranked.append(
                {
                    "plan_id": option.plan_id,
                    "title": option.title,
                    "score": score,
                    "pros": option.pros,
                    "cons": option.cons,
                }
            )

        ranked.sort(key=lambda item: item["score"], reverse=True)
        selected = ranked[0]

        reasoning = (
            f"Selected Plan {selected['plan_id']} ({selected['title']}) because it has the highest weighted score "
            f"while balancing time feasibility, sustainability, and goal alignment under the given constraints."
        )
        confidence = min(0.65 + (analysis.readiness_score * 0.3), 0.95)

        report = DecisionReport(
            ranking=ranked,
            selected_plan_id=selected["plan_id"],
            reasoning=reasoning,
            confidence_score=round(confidence, 2),
        )

        logs = [
            AgentLogEntry(
                agent=self.name,
                step="decide",
                detail=f"Scored and ranked {len(options)} plans; selected plan {selected['plan_id']}",
                confidence=round(confidence, 2),
            )
        ]
        return report, logs
