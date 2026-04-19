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

        # urgency
        if profile.timeline_months and profile.timeline_months <= 6:
            priorities.append("high urgency delivery")
        else:
            priorities.append("balanced long-term progression")

        # workload
        if profile.daily_time_hours and profile.daily_time_hours <= 2:
            priorities.append("low daily load consistency")
        else:
            priorities.append("higher weekly intensity")

        # preferences
        if profile.preferences:
            priorities.append(f"respect preference: {profile.preferences[0]}")

        # risks
        risks = []

        # ✅ IMPORTANT FIX HERE
        if not profile.current_skills:
            risks.append("skill baseline unclear")

        if profile.timeline_months and profile.timeline_months < 4:
            risks.append("timeline may be unrealistic")

        if "college workload" in profile.constraints:
            risks.append("schedule disruption due to academics")

        assumptions = [
            "user can maintain consistency",
            "internet access available",
        ]

        readiness = 0.5

        if profile.current_skills:
            readiness += 0.1

        if profile.daily_time_hours and profile.daily_time_hours >= 2:
            readiness += 0.1

        readiness = min(round(readiness, 2), 0.95)

        report = AnalysisReport(
            readiness_score=readiness,
            user_needs=needs,
            priorities=priorities,
            risks=risks,
            assumptions=assumptions,
        )

        logs = [
            AgentLogEntry(
                agent=self.name,
                step="analyze",
                detail="Generated priorities, risks, and readiness score",
                confidence=0.87,
            )
        ]

        return report, logs