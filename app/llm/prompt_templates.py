COLLECTOR_PROMPT = """
Extract goal, skills, constraints, preferences, timeline in months, and daily hours.
Return compact JSON only.
"""

ANALYZER_PROMPT = """
Analyze user profile and identify needs, priorities, risks, assumptions.
Return compact JSON only.
"""

PLANNER_PROMPT = """
Generate three plan options with milestones and weekly schedule.
Return compact JSON only.
"""

DECISION_PROMPT = """
Compare plans and choose best option using weighted criteria.
Return compact JSON only.
"""
