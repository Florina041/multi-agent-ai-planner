# Sample Inputs and Outputs

## Case 1: Career Planning
Input:
I am in 3rd year CSE, know Python basics, want data science role in 8 months, can study 2 hours daily, budget is low.

Expected behavior:
- Collector extracts goal, timeline, daily time, skills, constraints.
- Analyzer detects urgency, readiness, and schedule risk.
- Planner generates 3 roadmap options.
- Decision selects one plan with weighted score.
- Response returns step-by-step action plan.

## Case 2: Exam Study Schedule
Input:
I have exam in 5 months, can study 4 hours daily, weak in reasoning and quant.

Expected behavior:
- Balanced weekly study blocks by subject.
- Risk warning if targets are unrealistic.
- Recommended mock-test strategy.

## Case 3: Skill Roadmap Comparison
Input:
I want web development roadmap in 7 months with low budget and project-based preference.

Expected behavior:
- Plan A: Fundamentals-first.
- Plan B: Build-first.
- Plan C: Hybrid.
- Decision chooses highest weighted fit.
