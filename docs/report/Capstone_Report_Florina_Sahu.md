# Multi-Agent AI Decision and Planning System

**Personal Planning and Decision Making**

---

**Student Name:** Florina Sahu
**Roll Number:** 2329030
**Batch/Program:** B.Tech CSE, 2023–2027
**Department:** Computer Science
**Institution:** Kalinga Institute of Industrial Technology (KIIT), Bhubaneswar
**Academic Year:** 2025–26

---

## 1. Problem Statement

Students and early-career professionals frequently struggle to convert broad, ambiguous goals—such as "I want to become a data scientist" or "I need to prepare for placements"—into realistic, actionable plans. The challenges are compounded by real-world constraints: limited daily study hours, weak prerequisite skills, tight budgets, and looming deadlines.

Existing tools and chatbot-style assistants typically return generic, one-size-fits-all advice without separating distinct reasoning stages or explaining *why* a particular recommendation was made. There is no transparency in how options were compared or which trade-offs were considered. This project addresses that gap by building a **true multi-agent AI pipeline** where each stage has a clearly defined role, and the final recommendation is fully explainable and auditable.

## 2. Solution and Features

The system is a **modular multi-agent AI application** that accepts natural language user goals and produces personalized, explainable planning recommendations through a structured pipeline of six specialized agents:

### Core Features

- **Natural Language Input:** Users describe their goals in plain English (e.g., "I want a backend developer role in 10 months, I know Python basics, can study 3 hours daily").
- **Structured Profile Extraction:** The Collector Agent parses the input to extract goal, timeline, daily available hours, current skills, constraints, and preferences.
- **Smart Clarification Loop:** If critical fields are missing, the system automatically generates follow-up questions before proceeding.
- **Context-Aware Analysis:** The Analyzer Agent evaluates readiness, identifies priorities, detects risks, and flags assumptions.
- **Multi-Option Plan Generation:** The Planner Agent creates three distinct roadmap options, each with milestones and weekly study/work blocks.
- **Weighted Decision Scoring:** The Decision Agent ranks all options using a transparent formula:

  `Score = 0.35 × GoalAlignment + 0.25 × TimeFeasibility + 0.20 × SkillGapFit + 0.20 × Sustainability − RiskPenalty`

- **Explainable Recommendations:** The Response Agent generates a human-readable final output including the recommended plan, action steps, and risk warnings.
- **Session Memory:** The Memory Agent stores all interactions in a local SQLite database, enabling history review and repeat sessions.
- **Export Support:** Complete results can be downloaded in JSON and plain-text formats.

### Agent Pipeline Workflow

1. User submits a natural language prompt via the Streamlit dashboard.
2. **Collector Agent** extracts structured profile fields.
3. If required fields are missing, clarification questions are generated.
4. **Analyzer Agent** creates an interpretation of needs, risks, and priorities.
5. **Planner Agent** produces three roadmap alternatives.
6. **Decision Agent** scores, ranks, and selects the best option.
7. **Response Agent** creates the final user-facing structured recommendation.
8. **Memory Agent** stores interaction payloads for retrieval and review.

## 3. Screenshots

*(Screenshots captured from the running Streamlit application)*

- **Home Screen:** The input panel with domain selector, goal text area, and quick-start tips.
- **Clarification View:** Follow-up questions generated when the user provides incomplete input.
- **Plan Comparison:** Side-by-side comparison of three generated roadmap options with scores.
- **Final Recommendation:** The selected plan with action steps, weekly schedule, and risk warnings.
- **History View:** Table of recent interactions retrieved from the SQLite database.

> *Note: Screenshot image files (ui_home.png, ui_clarification.png, ui_plan_comparison.png, ui_final_recommendation.png, ui_history.png) are located in `docs/screenshots/`.*

## 4. Tech Stack

| Layer           | Technology                                      |
|-----------------|--------------------------------------------------|
| Language        | Python 3.10+                                     |
| UI Framework    | Streamlit                                        |
| Data Modeling   | Python Dataclasses / Pydantic-style contracts    |
| Persistence     | SQLite                                           |
| Testing         | Pytest                                           |
| LLM Integration | OpenAI API adapter, Gemini provider scaffolding (optional) |
| Environment     | python-dotenv for configuration management       |
| Deployment      | Render, Streamlit Cloud, Docker                  |

## 5. Unique Points

- **True Multi-Agent Architecture:** Unlike single-chatbot projects, this system decomposes the planning task into six distinct agents with clear role separation and structured data contracts between stages.
- **Explainable Decision Logic:** Every recommendation comes with a transparent weighted score breakdown, making it easy to understand *why* a particular plan was chosen over alternatives.
- **Clarification Loop:** The system proactively detects missing information and asks targeted follow-up questions, mimicking how a human advisor would handle incomplete requests.
- **Deterministic and Auditable:** The scoring formula and agent activity logs ensure that outputs are repeatable and can be reviewed stage by stage for academic evaluation.
- **Structured Inter-Agent Communication:** Typed dataclass schemas (UserProfile, AnalysisReport, PlanOption, DecisionReport, FinalResponse) enforce predictable data handoff and reduce integration errors.
- **Session Persistence:** SQLite-backed memory allows users to revisit past planning sessions and track how their goals evolve over time.

## 6. Future Improvements

- **API Layer:** Add a FastAPI service layer for programmatic access and third-party integration.
- **Authentication:** Implement user authentication and role-based multi-user support.
- **Stronger NLP:** Improve semantic extraction using advanced language models for better understanding of nuanced or implicitly stated goals.
- **Calendar Integration:** Connect with Google Calendar or similar services for milestone reminders and deadline tracking.
- **Adaptive Feedback:** Introduce feedback loops where outcomes from past plans inform and improve future recommendations.
- **Enterprise Scaling:** Migrate from SQLite to PostgreSQL for concurrent multi-user production deployment.

## 7. References

1. Streamlit Documentation — https://docs.streamlit.io
2. Python Documentation — https://docs.python.org/3/
3. Pytest Documentation — https://docs.pytest.org
4. SQLite Documentation — https://www.sqlite.org/docs.html
5. OpenAI API Reference — https://platform.openai.com/docs

---

*Project Repository: GitHub (public link submitted via Google Form)*
*All source code, tests, documentation, and deployment files are included in the submitted ZIP.*
