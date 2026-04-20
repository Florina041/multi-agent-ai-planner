from app.agents.decision_agent import DecisionAgent
from app.models.schemas import AnalysisReport, PlanMilestone, PlanOption


def _option(plan_id: str, score_offset: float) -> PlanOption:
    return PlanOption(
        plan_id=plan_id,
        title=f"Plan {plan_id}",
        description="desc",
        milestones=[PlanMilestone(phase="P", duration_weeks=2, tasks=["t"])],
        weekly_schedule=["Mon"],
        pros=["p"],
        cons=["c"],
        goal_alignment=0.8 + score_offset,
        time_feasibility=0.8,
        skill_gap_fit=0.8,
        sustainability=0.8,
        risk_penalty=0.1,
    )


def test_decision_ranks_plans() -> None:
    agent = DecisionAgent()
    analysis = AnalysisReport(
        readiness_score=0.7,
        user_needs=["clear roadmap"],
        priorities=["time efficiency"],
        risks=["consistency risk"],
        assumptions=["user follows weekly plan"],
    )
    report, _ = agent.run(analysis, [_option("A", 0.0), _option("B", 0.1)])
    assert report.ranking[0]["plan_id"] == "B"
