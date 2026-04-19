from __future__ import annotations

import re
from typing import List, Tuple

from app.agents.base_agent import BaseAgent
from app.models.enums import DomainType
from app.models.schemas import AgentLogEntry, UserProfile
from app.services.validation_service import detect_missing_fields


# -----------------------------
# TEXT CLEANING (OPTIONAL BOOST)
# -----------------------------
STOP_WORDS = ["also", "then"]

def clean_text(text: str) -> str:
    for word in STOP_WORDS:
        text = text.replace(word, "")
    return text.strip()


# -----------------------------
# SENTENCE SPLITTING (CRITICAL FIX)
# -----------------------------
def split_sentences(text: str) -> List[str]:
    return [s.strip() for s in re.split(r"[.,]| and ", text) if s.strip()]


# -----------------------------
# SKILL EXTRACTION (STRICT)
# -----------------------------
def extract_skills(sentences: List[str]) -> List[str]:
    skills = []
    for sent in sentences:
        if "know" in sent.lower():
            match = re.search(r"know\s+([a-zA-Z0-9 +\-]+)", sent, re.IGNORECASE)
            if match:
                skill_text = match.group(1)
                skills.extend([s.strip() for s in skill_text.split(",") if s.strip()])
    return skills


# -----------------------------
# GOAL EXTRACTION (CLEAN)
# -----------------------------
def extract_goal(sentences: List[str]) -> str | None:
    for sent in sentences:
        if any(k in sent.lower() for k in ["want", "goal", "need"]):
            return sent.strip()
    return None


# -----------------------------
# TIMELINE EXTRACTION
# -----------------------------
def extract_timeline(text: str) -> int | None:
    match = re.search(r"(\d+)\s*(month|months)", text)
    return int(match.group(1)) if match else None


# -----------------------------
# DAILY HOURS EXTRACTION
# -----------------------------
def extract_daily_hours(text: str) -> int | None:
    match = re.search(r"(\d+)\s*(hour|hours|hr|hrs)", text)
    return int(match.group(1)) if match else None


# -----------------------------
# COLLECTOR AGENT
# -----------------------------
class CollectorAgent(BaseAgent):
    name = "CollectorAgent"

    def run(self, user_text: str, domain: str) -> Tuple[UserProfile, List[AgentLogEntry]]:

        # 🔹 Clean input
        cleaned = clean_text(user_text)
        lower_text = cleaned.lower()

        # 🔹 Sentence segmentation (CRITICAL FIX)
        sentences = split_sentences(cleaned)

        # 🔹 Structured extraction
        skills = extract_skills(sentences)
        goal = extract_goal(sentences)
        timeline = extract_timeline(cleaned)
        daily_hours = extract_daily_hours(cleaned)

        # 🔹 Budget detection
        budget_level = None
        if any(token in lower_text for token in ["low budget", "budget is low", "cheap", "free"]):
            budget_level = "low"
        elif any(token in lower_text for token in ["medium budget", "moderate budget"]):
            budget_level = "medium"
        elif "high budget" in lower_text:
            budget_level = "high"

        # 🔹 Constraints detection
        constraints = []
        if "job" in lower_text or "working" in lower_text:
            constraints.append("balancing job and study")
        if "college" in lower_text:
            constraints.append("college workload")
        if "exam" in lower_text:
            constraints.append("exam pressure")

        # 🔹 Preferences detection
        preferences = []
        if "project" in lower_text:
            preferences.append("project-based learning")
        if "video" in lower_text:
            preferences.append("video-first resources")
        if "certificate" in lower_text:
            preferences.append("certificate-oriented progression")

        # 🔹 Build user profile (FIXED FIELD NAME: skills)
        profile = UserProfile(
            raw_input=cleaned,
            domain=DomainType(domain),
            goal=goal,
            skills=sorted(set(skills)),
            constraints=constraints,
            preferences=preferences,
            timeline_months=timeline,
            daily_time_hours=daily_hours,
            budget_level=budget_level,
        )

        # 🔹 Validation
        missing = detect_missing_fields(profile)
        profile.missing_fields = missing
        profile.follow_up_questions = self._build_questions(missing, profile.domain.value)

        # 🔹 Logs
        logs = [
            AgentLogEntry(
                agent=self.name,
                step="extract",
                detail="Performed sentence-level parsing and structured field extraction",
                confidence=0.92,
            ),
            AgentLogEntry(
                agent=self.name,
                step="validate",
                detail=f"Detected missing fields: {', '.join(missing) if missing else 'none'}",
                confidence=0.9,
            ),
        ]

        return profile, logs


    # -----------------------------
    # FOLLOW-UP QUESTIONS
    # -----------------------------
    def _build_questions(self, missing_fields: List[str], domain: str) -> List[str]:
        prompts = {
            "goal": f"What is your exact {domain} target outcome?",
            "timeline_months": "What is your target timeline in months?",
            "daily_time_hours": "How many hours per day can you consistently invest?",
        }

        return [prompts.get(key, f"Please provide {key} details.") for key in missing_fields]