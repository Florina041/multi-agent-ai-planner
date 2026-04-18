from __future__ import annotations

from app.models.schemas import PlanOption


def score_plan(plan: PlanOption) -> float:
    weighted = (
        (0.35 * plan.goal_alignment)
        + (0.25 * plan.time_feasibility)
        + (0.20 * plan.skill_gap_fit)
        + (0.20 * plan.sustainability)
    )
    return round(weighted - plan.risk_penalty, 3)
