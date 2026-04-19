from __future__ import annotations

import re
import json
from typing import Optional, List

from app.agents.base_agent import BaseAgent
from app.models.enums import DomainType
from app.models.schemas import AgentLogEntry, UserProfile
from app.services.validation_service import detect_missing_fields


def clean_json(text: str) -> str:
    text = re.sub(r"```json", "", text)
    text = re.sub(r"```", "", text)
    return text.strip()


class CollectorAgent(BaseAgent):
    name = "CollectorAgent"

    def __init__(self, llm=None):
        self.llm = llm

    def run(self, user_text: str, domain: str):
        cleaned = user_text.strip()

        # -------------------------
        # STEP 1: Sentence Split
        # -------------------------
        sentences = re.split(r"[.,]| and ", cleaned)

        # -------------------------
        # STEP 2: Skills
        # -------------------------
        skills: List[str] = []
        for sent in sentences:
            if "know" in sent.lower():
                match = re.search(r"know\s+([a-zA-Z0-9 +\-]+)", sent, re.IGNORECASE)
                if match:
                    skills.extend([s.strip() for s in match.group(1).split(",")])

        # -------------------------
        # STEP 3: Goal
        # -------------------------
        goal: Optional[str] = None
        for sent in sentences:
            if any(k in sent.lower() for k in ["want", "goal", "need"]):
                goal = sent.strip()

        # -------------------------
        # STEP 4: Timeline
        # -------------------------
        timeline = None
        match = re.search(r"(\d+)\s*(month|months)", cleaned)
        if match:
            timeline = int(match.group(1))

        # -------------------------
        # STEP 5: Daily Hours
        # -------------------------
        daily_hours = None
        match = re.search(r"(\d+)\s*(hour|hours)", cleaned)
        if match:
            daily_hours = int(match.group(1))

        constraints = []
        if "college" in cleaned.lower():
            constraints.append("college workload")

        # -------------------------
        # STEP 6: LLM Enhancement
        # -------------------------
        if self.llm and self.llm.available():
            try:
                prompt = f"""
Return JSON only with:
goal, skills, timeline_months, daily_time_hours, constraints

Input:
{user_text}
"""
                response = self.llm.complete(prompt)
                response = clean_json(response)

                data = json.loads(response)

                skills = data.get("skills") or skills
                goal = data.get("goal") or goal
                timeline = data.get("timeline_months") or timeline
                daily_hours = data.get("daily_time_hours") or daily_hours
                constraints = data.get("constraints") or constraints

            except Exception:
                pass

        # -------------------------
        # FINAL PROFILE
        # -------------------------
        profile = UserProfile(
            raw_input=cleaned,
            domain=DomainType(domain),
            goal=goal,
            skills=list(set(skills)),
            constraints=constraints,
            timeline_months=timeline,
            daily_time_hours=daily_hours,
        )

        missing = detect_missing_fields(profile)
        profile.missing_fields = missing
        profile.follow_up_questions = [f"Please provide {f}" for f in missing]

        logs = [
            AgentLogEntry(
                agent=self.name,
                step="extract",
                detail="Hybrid extraction (rule + LLM)",
                confidence=0.9,
            )
        ]

        return profile, logs