from __future__ import annotations

from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field


# -----------------------------
# Agent Logs
# -----------------------------
class AgentLogEntry(BaseModel):
    agent: str
    step: str
    detail: str
    confidence: float


# -----------------------------
# User Profile (FIXED)
# -----------------------------
class UserProfile(BaseModel):
    domain: Any
    raw_input: str

    goal: Optional[str] = None

    # ✅ FIXED NAME + SAFE DEFAULTS
    current_skills: List[str] = Field(default_factory=list)
    constraints: List[str] = Field(default_factory=list)

    timeline_months: Optional[int] = None
    daily_time_hours: Optional[int] = None
    budget_level: Optional[str] = None

    preferences: List[str] = Field(default_factory=list)
    missing_fields: List[str] = Field(default_factory=list)
    follow_up_questions: List[str] = Field(default_factory=list)


# -----------------------------
# Analysis
# -----------------------------
class AnalysisReport(BaseModel):
    readiness_score: float
    user_needs: List[str]
    priorities: List[str]
    risks: List[str]
    assumptions: List[str]


# -----------------------------
# Plan Milestone
# -----------------------------
class PlanMilestone(BaseModel):
    phase: str
    duration_weeks: int
    tasks: List[str]


# -----------------------------
# Plan Options (FIXED)
# -----------------------------
class PlanOption(BaseModel):
    plan_id: str
    title: str
    description: str
    milestones: List[PlanMilestone]
    weekly_schedule: List[str]
    pros: List[str]
    cons: List[str]

    # ✅ CRITICAL FOR SCORING ENGINE
    goal_alignment: float
    time_feasibility: float
    skill_gap_fit: float
    sustainability: float
    risk_penalty: float


# -----------------------------
# Decision
# -----------------------------
class DecisionReport(BaseModel):
    ranking: List[Dict[str, Any]]
    selected_plan_id: str
    reasoning: str
    confidence_score: float


# -----------------------------
# Final Response
# -----------------------------
class FinalResponse(BaseModel):
    summary: str
    extracted_information: Dict[str, Any]
    analysis: Dict[str, Any]
    options: List[Dict[str, Any]]
    recommendation: Dict[str, Any]
    action_plan: List[str]
    warnings: List[str]
    next_steps: List[str]

    # ✅ RAG support
    retrieved_knowledge: Optional[str] = None


# -----------------------------
# Workflow Result (FIXED)
# -----------------------------
class WorkflowResult(BaseModel):
    status: str
    session_id: str

    # ✅ REQUIRED FOR CLARIFICATION FLOW
    questions: Optional[List[str]] = None

    user_profile: Optional[UserProfile] = None
    analysis_report: Optional[AnalysisReport] = None
    plan_options: Optional[List[PlanOption]] = None
    decision_report: Optional[DecisionReport] = None
    final_response: Optional[FinalResponse] = None

    agent_logs: List[AgentLogEntry]

    # ✅ EXTRA OUTPUTS
    rag_context: Optional[str] = None
    faithfulness_score: Optional[float] = None
    tool_output: Optional[Any] = None