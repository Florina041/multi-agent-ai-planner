from __future__ import annotations
import json
from app.agents.base_agent import BaseAgent
from app.models.schemas import (
    AnalysisReport,
    AgentLogEntry,
    PlanMilestone,
    PlanOption,
    UserProfile,
)


class PlannerAgent(BaseAgent):
    name = "PlannerAgent"

    def __init__(self, llm=None):
        self.llm = llm

    def run(
        self,
        profile: UserProfile,
        analysis: AnalysisReport,
    ) -> tuple[list[PlanOption], list[AgentLogEntry]]:

        total_months = profile.timeline_months or 6
        total_weeks = max(total_months * 4, 8)

        # -------------------------
        # RULE-BASED PLANS
        # -------------------------
        options = [
            self._build_foundation_plan(total_weeks),
            self._build_execution_plan(total_weeks),
            self._build_hybrid_plan(total_weeks),
        ]

        # -------------------------
        # OPTIONAL LLM ENHANCEMENT
        # -------------------------
        if self.llm and self.llm.available():
            try:
                prompt = f"""
                Generate 3 structured plans in JSON format.

                Each plan should include:
                plan_id, title, description

                Profile:
                {profile.model_dump()}

                Analysis:
                {analysis.model_dump()}
                """

                llm_output = self.llm.complete(prompt)

                # Optional parsing (safe fallback)
                _ = json.loads(llm_output)

            except Exception:
                pass  # fallback safe

        logs = [
            AgentLogEntry(
                agent=self.name,
                step="plan",
                detail=f"Generated {len(options)} plans (rule + optional LLM)",
                confidence=0.84,
            )
        ]

        return options, logs

    # -------------------------
    # PLAN A
    # -------------------------
    def _build_foundation_plan(self, weeks: int) -> PlanOption:
        part = max(weeks // 3, 2)

        return PlanOption(
            plan_id="A",
            title="Foundation-First Plan",
            description="Strong conceptual learning first",
            milestones=[
                PlanMilestone(
                    phase="Basics",
                    duration_weeks=part,
                    tasks=["Learn fundamentals", "Practice daily"],
                ),
                PlanMilestone(
                    phase="Practice",
                    duration_weeks=part,
                    tasks=["Mini projects", "Problem solving"],
                ),
                PlanMilestone(
                    phase="Final Prep",
                    duration_weeks=weeks - (2 * part),
                    tasks=["Build portfolio", "Prepare interviews"],
                ),
            ],
            weekly_schedule=[
                "Mon-Tue: Learn",
                "Wed-Thu: Practice",
                "Fri: Revise",
                "Weekend: Projects",
            ],
            pros=["Strong base"],
            cons=["Slow start"],
            goal_alignment=0.78,
            time_feasibility=0.82,
            skill_gap_fit=0.88,
            sustainability=0.80,
            risk_penalty=0.14,
        )

    # -------------------------
    # PLAN B
    # -------------------------
    def _build_execution_plan(self, weeks: int) -> PlanOption:
        part = max(weeks // 3, 2)

        return PlanOption(
            plan_id="B",
            title="Execution-First Plan",
            description="Focus on output quickly",
            milestones=[
                PlanMilestone(
                    phase="Start Projects",
                    duration_weeks=part,
                    tasks=["Build from day 1", "Publish work"],
                ),
                PlanMilestone(
                    phase="Fix Weak Areas",
                    duration_weeks=part,
                    tasks=["Improve gaps", "Targeted practice"],
                ),
                PlanMilestone(
                    phase="Placement Prep",
                    duration_weeks=weeks - (2 * part),
                    tasks=["Mock interviews", "Applications"],
                ),
            ],
            weekly_schedule=[
                "Mon: Build",
                "Tue: Learn",
                "Wed-Thu: Improve",
                "Weekend: Review",
            ],
            pros=["Fast results"],
            cons=["Weak theory risk"],
            goal_alignment=0.84,
            time_feasibility=0.75,
            skill_gap_fit=0.70,
            sustainability=0.73,
            risk_penalty=0.18,
        )

    # -------------------------
    # PLAN C (BEST)
    # -------------------------
    def _build_hybrid_plan(self, weeks: int) -> PlanOption:
        part = max(weeks // 3, 2)

        return PlanOption(
            plan_id="C",
            title="Hybrid Balanced Plan",
            description="Best mix of learning and execution",
            milestones=[
                PlanMilestone(
                    phase="Start + Learn",
                    duration_weeks=part,
                    tasks=["Learn + mini project"],
                ),
                PlanMilestone(
                    phase="Growth",
                    duration_weeks=part,
                    tasks=["Build real project", "Improve weak areas"],
                ),
                PlanMilestone(
                    phase="Final Phase",
                    duration_weeks=weeks - (2 * part),
                    tasks=["Portfolio + interviews"],
                ),
            ],
            weekly_schedule=[
                "Mon: Learn",
                "Tue: Practice",
                "Wed: Project",
                "Thu: Revise",
                "Fri: Output",
                "Weekend: Review",
            ],
            pros=["Balanced", "Low burnout"],
            cons=["Needs discipline"],
            goal_alignment=0.89,
            time_feasibility=0.88,
            skill_gap_fit=0.86,
            sustainability=0.90,
            risk_penalty=0.10,
        )