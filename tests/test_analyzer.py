from app.agents.analyzer_agent import AnalyzerAgent
from app.models.schemas import UserProfile


def test_analyzer_creates_risks_and_priorities() -> None:
    profile = UserProfile(
        raw_input="sample",
        goal="crack exam",
        timeline_months=5,
        daily_time_hours=2,
        skills=["math basics"],
        constraints=["college workload"],
    )
    agent = AnalyzerAgent()
    report, _ = agent.run(profile)

    assert report.priorities
    assert isinstance(report.readiness_score, float)
