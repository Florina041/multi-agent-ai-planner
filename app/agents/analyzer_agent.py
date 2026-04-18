from __future__ import annotations

from app.agents.base_agent import BaseAgent
from app.models.schemas import AnalysisReport, AgentLogEntry, UserProfile


class AnalyzerAgent(BaseAgent):
    name = "AnalyzerAgent"

    def run(self, profile: UserProfile) -> tuple[AnalysisReport, list[AgentLogEntry]]:
        needs = [
            "clear milestone roadmap",
            "practical execution plan",
            "risk-aware strategy",
        ]
        priorities = []

        if profile.timeline_months and profile.timeline_months <= 6:
            priorities.append("high urgency delivery")
        else:
            priorities.append("balanced long-term progression")

        if profile.daily_time_hours and profile.daily_time_hours <= 2:
            priorities.append("low daily load consistency")
        else:
            priorities.append("higher weekly intensity")

        if profile.preferences:
            priorities.append(f"respect preference: {profile.preferences[0]}")

        risks = []
        if not profile.current_skills:
            risks.append("skill baseline unclear")
        if profile.timeline_months and profile.timeline_months < 4:
            risks.append("timeline may be unrealistic for deep mastery")
        if "college workload" in profile.constraints:
            risks.append("schedule disruption due to academics")

        assumptions = [
            "user can maintain weekly consistency",
            "internet access available for resources",
        ]

        readiness = 0.55 + (0.1 if profile.current_skills else 0.0) + (0.05 if profile.daily_time_hours and profile.daily_time_hours >= 2 else 0.0)
        readiness = min(round(readiness, 2), 0.95)

        report = AnalysisReport(
            user_needs=needs,
            priorities=priorities,
            risks=risks,
            assumptions=assumptions,
            readiness_score=readiness,
        )

        logs = [
            AgentLogEntry(
                agent=self.name,
                step="analyze",
                detail="Interpreted user goals, priorities, and constraints",
                confidence=0.86,
            )
        ]
        return report, logs
