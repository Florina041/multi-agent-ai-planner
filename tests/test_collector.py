from app.agents.collector_agent import CollectorAgent


def test_collector_extracts_core_fields() -> None:
    agent = CollectorAgent()
    text = (
        "I am in 3rd year CSE, know Python basics, want to become a data analyst "
        "in 8 months, can study 2 hours daily, and prefer project-based learning."
    )
    profile, logs = agent.run(text, "career")

    assert profile.timeline_months == 8
    assert profile.daily_time_hours == 2
    assert profile.goal is not None
    assert len(logs) >= 1
