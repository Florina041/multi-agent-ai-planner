from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any

from app.models.enums import DomainType


@dataclass
class DumpableModel:
    def model_dump(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class AgentLogEntry(DumpableModel):
    agent: str
    step: str
    detail: str
    confidence: float = 0.0


@dataclass
class UserProfile(DumpableModel):
    raw_input: str
    domain: DomainType = DomainType.CAREER
    goal: str | None = None
    current_skills: list[str] = field(default_factory=list)
    constraints: list[str] = field(default_factory=list)
    preferences: list[str] = field(default_factory=list)
    timeline_months: int | None = None
    daily_time_hours: int | None = None
    budget_level: str | None = None
    missing_fields: list[str] = field(default_factory=list)
    follow_up_questions: list[str] = field(default_factory=list)


@dataclass
class AnalysisReport(DumpableModel):
    user_needs: list[str] = field(default_factory=list)
    priorities: list[str] = field(default_factory=list)
    risks: list[str] = field(default_factory=list)
    assumptions: list[str] = field(default_factory=list)
    readiness_score: float = 0.0


@dataclass
class PlanMilestone(DumpableModel):
    phase: str
    duration_weeks: int
    tasks: list[str]


@dataclass
class PlanOption(DumpableModel):
    plan_id: str
    title: str
    description: str
    milestones: list[PlanMilestone]
    weekly_schedule: list[str]
    pros: list[str]
    cons: list[str]
    goal_alignment: float
    time_feasibility: float
    skill_gap_fit: float
    sustainability: float
    risk_penalty: float


@dataclass
class DecisionReport(DumpableModel):
    ranking: list[dict[str, Any]]
    selected_plan_id: str
    reasoning: str
    confidence_score: float


@dataclass
class FinalResponse(DumpableModel):
    summary: str
    extracted_information: dict[str, Any]
    analysis: dict[str, Any]
    options: list[dict[str, Any]]
    recommendation: dict[str, Any]
    action_plan: list[str]
    warnings: list[str]
    next_steps: list[str]


@dataclass
class WorkflowResult(DumpableModel):
    status: str
    session_id: str
    questions: list[str] = field(default_factory=list)
    user_profile: UserProfile | None = None
    analysis_report: AnalysisReport | None = None
    plan_options: list[PlanOption] = field(default_factory=list)
    decision_report: DecisionReport | None = None
    final_response: FinalResponse | None = None
    agent_logs: list[AgentLogEntry] = field(default_factory=list)
