from __future__ import annotations

import re

from app.agents.base_agent import BaseAgent
from app.models.enums import DomainType
from app.models.schemas import AgentLogEntry, UserProfile
from app.services.validation_service import detect_missing_fields
from app.utils.helpers import extract_first_number


class CollectorAgent(BaseAgent):
    name = "CollectorAgent"

    def run(self, user_text: str, domain: str) -> tuple[UserProfile, list[AgentLogEntry]]:
        cleaned = user_text.strip()
        lower_text = cleaned.lower()

        timeline = extract_first_number(lower_text, r"(\d+)\s*(month|months)")
        daily_hours = extract_first_number(lower_text, r"(\d+)\s*(hour|hours|hr|hrs)\s*(daily|per day)?")

        budget_level = None
        if any(token in lower_text for token in ["low budget", "budget is low", "cheap", "free"]):
            budget_level = "low"
        elif any(token in lower_text for token in ["medium budget", "moderate budget"]):
            budget_level = "medium"
        elif "high budget" in lower_text:
            budget_level = "high"

        skill_chunks = re.findall(r"know\s+([a-zA-Z0-9,\s+\-]+)", cleaned, flags=re.IGNORECASE)
        skills = []
        for chunk in skill_chunks:
            for part in chunk.split(","):
                text = part.strip()
                if text:
                    skills.append(text)

        constraints = []
        if "job" in lower_text or "working" in lower_text:
            constraints.append("balancing job and study")
        if "college" in lower_text:
            constraints.append("college workload")
        if "exam" in lower_text:
            constraints.append("exam pressure")

        preferences = []
        if "project" in lower_text:
            preferences.append("project-based learning")
        if "video" in lower_text:
            preferences.append("video-first resources")
        if "certificate" in lower_text:
            preferences.append("certificate-oriented progression")

        goal = None
        for starter in ["want to", "goal is", "i need", "i want to"]:
            idx = lower_text.find(starter)
            if idx >= 0:
                goal = cleaned[idx + len(starter) :].strip().strip(".")
                break

        profile = UserProfile(
            raw_input=cleaned,
            domain=DomainType(domain),
            goal=goal,
            current_skills=sorted(set(skills)),
            constraints=constraints,
            preferences=preferences,
            timeline_months=timeline,
            daily_time_hours=daily_hours,
            budget_level=budget_level,
        )

        missing = detect_missing_fields(profile)
        profile.missing_fields = missing
        profile.follow_up_questions = self._build_questions(missing, profile.domain.value)

        logs = [
            AgentLogEntry(
                agent=self.name,
                step="extract",
                detail="Extracted structured fields from natural language input",
                confidence=0.83,
            ),
            AgentLogEntry(
                agent=self.name,
                step="validate",
                detail=f"Detected missing fields: {', '.join(missing) if missing else 'none'}",
                confidence=0.9,
            ),
        ]
        return profile, logs

    def _build_questions(self, missing_fields: list[str], domain: str) -> list[str]:
        questions = []
        prompts = {
            "goal": f"What is your exact {domain} target outcome?",
            "timeline_months": "What is your target timeline in months?",
            "daily_time_hours": "How many hours per day can you consistently invest?",
        }
        for key in missing_fields:
            questions.append(prompts.get(key, f"Please provide {key} details."))
        return questions
