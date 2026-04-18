from __future__ import annotations

from app.agents.base_agent import BaseAgent
from app.models.schemas import AnalysisReport, AgentLogEntry, PlanMilestone, PlanOption, UserProfile


class PlannerAgent(BaseAgent):
    name = "PlannerAgent"

    def run(self, profile: UserProfile, analysis: AnalysisReport) -> tuple[list[PlanOption], list[AgentLogEntry]]:
        total_months = profile.timeline_months or 6
        total_weeks = max(total_months * 4, 8)

        options = [
            self._build_foundation_plan(total_weeks),
            self._build_execution_plan(total_weeks),
            self._build_hybrid_plan(total_weeks),
        ]

        logs = [
            AgentLogEntry(
                agent=self.name,
                step="plan",
                detail=f"Generated {len(options)} candidate plans with milestones",
                confidence=0.84,
            )
        ]
        return options, logs

    def _build_foundation_plan(self, weeks: int) -> PlanOption:
        part = max(weeks // 3, 2)
        milestones = [
            PlanMilestone(
                phase="Fundamentals",
                duration_weeks=part,
                tasks=["Strengthen core concepts", "Complete structured tutorials", "Weekly revision"],
            ),
            PlanMilestone(
                phase="Intermediate Practice",
                duration_weeks=part,
                tasks=["Guided mini-projects", "Solve curated problems", "Track weak areas"],
            ),
            PlanMilestone(
                phase="Portfolio and Readiness",
                duration_weeks=weeks - (2 * part),
                tasks=["Build capstone projects", "Prepare resume/notes", "Mock interviews/tests"],
            ),
        ]
        return PlanOption(
            plan_id="A",
            title="Foundation-First Roadmap",
            description="Prioritizes strong fundamentals before intensive output.",
            milestones=milestones,
            weekly_schedule=[
                "Mon-Tue: concept learning",
                "Wed-Thu: hands-on exercises",
                "Fri: recap and notes",
                "Sat: mini deliverable",
                "Sun: review and planning",
            ],
            pros=["Strong conceptual base", "Lower long-term confusion"],
            cons=["Slower visible outcomes in first month"],
            goal_alignment=0.78,
            time_feasibility=0.82,
            skill_gap_fit=0.88,
            sustainability=0.80,
            risk_penalty=0.14,
        )

    def _build_execution_plan(self, weeks: int) -> PlanOption:
        part = max(weeks // 3, 2)
        milestones = [
            PlanMilestone(
                phase="Fast Output Start",
                duration_weeks=part,
                tasks=["Start practical tasks from week 1", "Build public progress artifacts", "Get early feedback"],
            ),
            PlanMilestone(
                phase="Targeted Skill Patch",
                duration_weeks=part,
                tasks=["Fix gaps as needed", "Practice assessment patterns", "Time-boxed improvement"],
            ),
            PlanMilestone(
                phase="Outcome Push",
                duration_weeks=weeks - (2 * part),
                tasks=["Refine top projects", "Intensive interview prep", "Applications/exam simulations"],
            ),
        ]
        return PlanOption(
            plan_id="B",
            title="Execution-First Roadmap",
            description="Focuses on quick visible output and market/exam readiness.",
            milestones=milestones,
            weekly_schedule=[
                "Mon: practical build sprint",
                "Tue: targeted theory",
                "Wed-Thu: project enhancement",
                "Fri: feedback integration",
                "Sat-Sun: simulation and review",
            ],
            pros=["Early tangible results", "Strong demo/interview story"],
            cons=["Higher risk of conceptual gaps"],
            goal_alignment=0.84,
            time_feasibility=0.75,
            skill_gap_fit=0.70,
            sustainability=0.73,
            risk_penalty=0.18,
        )

    def _build_hybrid_plan(self, weeks: int) -> PlanOption:
        part = max(weeks // 3, 2)
        milestones = [
            PlanMilestone(
                phase="Core + Quick Wins",
                duration_weeks=part,
                tasks=["Daily concept-practice split", "One small project", "Weekly checkpoint"],
            ),
            PlanMilestone(
                phase="Balanced Growth",
                duration_weeks=part,
                tasks=["Build medium project", "Strengthen weak topics", "Peer/community feedback"],
            ),
            PlanMilestone(
                phase="Final Optimization",
                duration_weeks=weeks - (2 * part),
                tasks=["Finalize portfolio/revision set", "Mock interviews/exams", "Application strategy"],
            ),
        ]
        return PlanOption(
            plan_id="C",
            title="Hybrid Balanced Roadmap",
            description="Balances conceptual depth and practical outcomes.",
            milestones=milestones,
            weekly_schedule=[
                "Mon: concept block",
                "Tue: applied exercises",
                "Wed: project work",
                "Thu: concept reinforcement",
                "Fri: output review",
                "Sat: milestone tasks",
                "Sun: rest + reflection",
            ],
            pros=["Balanced pace", "Lower burnout risk", "Good explanation power in viva/interviews"],
            cons=["Requires discipline and weekly tracking"],
            goal_alignment=0.89,
            time_feasibility=0.88,
            skill_gap_fit=0.86,
            sustainability=0.90,
            risk_penalty=0.10,
        )
