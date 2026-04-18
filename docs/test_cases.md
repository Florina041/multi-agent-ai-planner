# Test Cases

## Functional Tests
1. Missing timeline and daily hours
- Input: "I want to become a data analyst."
- Expected: collector asks clarification questions.

2. Complete career case
- Input: "I want backend role in 10 months, can study 3 hours daily, know Python basics."
- Expected: complete workflow with ranked plans and recommendation.

3. Study planning case
- Input: "I have exam in 6 months, weak in quant, can study 4 hours daily."
- Expected: study-focused plan options and warning list.

4. Skill roadmap low budget
- Input: "I want full-stack roadmap in 8 months with low budget and 2 hours daily."
- Expected: budget-aware recommendation and feasible weekly schedule.

## Non-Functional Tests
1. Repeatability
- Same input should produce stable structure and deterministic ranking.

2. Persistence
- Complete interactions should appear in history table.

3. Export
- JSON and text download should be available after complete run.

## Automated Tests Included
- tests/test_collector.py
- tests/test_analyzer.py
- tests/test_planner.py
- tests/test_decision.py
- tests/test_orchestrator.py
