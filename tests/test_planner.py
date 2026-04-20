from app.agents.planner_agent import PlannerAgent
from app.models.enums import DomainType
from app.models.schemas import AnalysisReport, UserProfile


def test_planner_generates_three_options() -> None:
    profile = UserProfile(
        domain=DomainType.SKILL,
        raw_input="sample",
        goal="learn python",
        timeline_months=6,
        daily_time_hours=2,
    )
    analysis = AnalysisReport(
        readiness_score=0.7,
        user_needs=["structured weekly practice"],
        priorities=["consistency"],
        risks=["limited daily time"],
        assumptions=["user can study daily"],
    )
    planner = PlannerAgent()
    options, _ = planner.run(profile, analysis)

    assert len(options) == 3
    assert {item.plan_id for item in options} == {"A", "B", "C"}
