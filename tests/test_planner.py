from app.agents.planner_agent import PlannerAgent
from app.models.schemas import AnalysisReport, UserProfile


def test_planner_generates_three_options() -> None:
    profile = UserProfile(
        raw_input="sample",
        goal="learn python",
        timeline_months=6,
        daily_time_hours=2,
    )
    analysis = AnalysisReport()
    planner = PlannerAgent()
    options, _ = planner.run(profile, analysis)

    assert len(options) == 3
    assert {item.plan_id for item in options} == {"A", "B", "C"}
