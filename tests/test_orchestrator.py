from app.core.orchestrator import MultiAgentOrchestrator


def test_orchestrator_complete_flow(tmp_path) -> None:
    db_path = str(tmp_path / "test.db")
    orchestrator = MultiAgentOrchestrator(db_path=db_path)

    text = (
        "I want to become a backend developer in 10 months. "
        "I can study 3 hours daily and already know Python basics."
    )
    result = orchestrator.run(user_text=text, domain="career")

    assert result.status == "complete"
    assert result.decision_report is not None
    assert result.final_response is not None
