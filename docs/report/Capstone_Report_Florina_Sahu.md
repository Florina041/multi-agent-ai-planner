# Multi-Agent AI Decision and Planning System

## Title Page
- Project Title: Personal Planning and Decision Making
- Student Name: Florina Sahu
- Roll Number: 2329030
- Department: Computer Science
- Institution: Kalinga Institute of Industria Technology
- Academic Year: 2025-26

## Abstract
This capstone project presents a modular multi-agent AI system for personalized planning and decision support in career, study, and skill-development domains. The system accepts natural language user goals, extracts structured intent, performs context-aware analysis, generates multiple plan options, and recommends the best roadmap using weighted decision logic. The workflow is explainable, stage-wise, and auditable through agent logs, confidence-linked outputs, and interaction history persistence. The implementation uses Python, Streamlit, dataclass/Pydantic-style schema contracts, and SQLite for local storage. The system also supports clarification loops, export in JSON/text formats, and optional LLM integration through provider adapters.

## Problem Statement
Students and early professionals often struggle to convert broad goals into realistic action plans under constraints such as limited time, weak prerequisites, and low budget. Conventional chatbot-style systems typically return generic advice without separating reasoning stages or exposing why a recommendation was made. This project addresses that gap by designing a true multi-agent pipeline where each stage has a specific role and contributes to an explainable final decision.

## Objectives
- Design and implement a true multi-agent planning workflow.
- Extract structured user profile details from natural language input.
- Detect missing critical information and trigger clarification questions.
- Generate multiple candidate roadmap options.
- Compare options using weighted and explainable decision scoring.
- Provide a human-readable final recommendation with actionable steps.
- Store interaction history and support repeat sessions.

## Importance of the Project
- Improves planning clarity for users with ambiguous or high-level goals.
- Demonstrates practical agentic AI architecture with role decomposition.
- Supports personalized guidance based on constraints and priorities.
- Provides explainable recommendations suitable for academic evaluation.
- Establishes a scalable foundation for future service/API deployment.

## System Architecture
The system follows a layered modular architecture:
- UI Layer: Streamlit dashboard for user interaction and visualization.
- Orchestration Layer: MultiAgentOrchestrator coordinates all stages.
- Agent Layer: Collector, Analyzer, Planner, Decision, Response, and Memory agents.
- Service Layer: Logging, evaluation, RAG retrieval, tool utilities, export, and validation.
- Data Layer: SQLite-based persistence and repository access.

Key architectural characteristics:
- Strict stage-wise processing with clear handoff contracts.
- Structured schemas for reliable inter-agent communication.
- Deterministic scoring logic for plan comparison.
- Session-oriented memory for history and continuity.

## Agent Responsibilities
- Collector Agent: Extracts goal, timeline, available daily hours, skills, constraints, and preferences; detects missing fields; prepares follow-up questions.
- Analyzer Agent: Interprets readiness, priorities, risks, and assumptions from collected profile.
- Planner Agent: Generates three feasible roadmap options with milestones and weekly blocks.
- Decision Agent: Computes weighted scores, ranks plans, and selects recommended option.
- Response Agent: Produces final structured explanation with recommendation, action plan, and warnings.
- Memory Agent: Stores and retrieves interactions for continuity and history views.

## Workflow Explanation
1. User submits a natural language prompt.
2. Collector extracts structured profile fields.
3. If required fields are missing, clarification questions are generated.
4. Analyzer creates an interpretation of needs, risks, and priorities.
5. Planner produces multiple roadmap alternatives.
6. Decision agent scores and ranks alternatives.
7. Response agent creates the final user-facing output.
8. Memory stores interaction payloads for retrieval and review.

## Technology Stack
- Language: Python
- UI: Streamlit
- Data Modeling: Dataclass/Pydantic-style schema contracts
- Persistence: SQLite
- Testing: Pytest
- Optional LLM Integration: OpenAI adapter and Gemini provider scaffolding
- Supporting Utilities: dotenv-based environment handling

## Implementation Details
### 1. Orchestration
The `MultiAgentOrchestrator` controls end-to-end workflow execution, including clarification loop handling, RAG retrieval, evaluation scoring, tool usage, and persistence.

### 2. Data Contracts
Structured schema models enforce predictable data handoff between agents and reduce coupling errors between pipeline stages.

### 3. Decision Scoring Formula
The weighted decision score used by the decision engine is:

Score(plan) = 0.35 * GoalAlignment + 0.25 * TimeFeasibility + 0.20 * SkillGapFit + 0.20 * Sustainability - RiskPenalty

This formula balances desirability, feasibility, and risk awareness.

### 4. Explainability and Logging
Each stage contributes activity logs. Outputs include ranked options and rationale, making the recommendation auditable and presentation-ready.

### 5. Export and History
Complete outputs can be exported in JSON and text formats. Past interactions are shown through history retrieval from SQLite.

## Screenshots and UI Explanation
Add the following screenshots from `docs/screenshots` with captions:
- `ui_home.png`: Input panel, domain selector, quick tips.
- `ui_clarification.png`: Clarification questions when fields are missing.
- `ui_plan_comparison.png`: Multi-option comparison and ranking view.
- `ui_final_recommendation.png`: Recommended plan, action steps, warnings.
- `ui_history.png`: Recent interaction history table.

## Sample Inputs and Outputs
Representative examples included in `docs/samples/sample_inputs_outputs.md`:
- Case 1: Career Planning (data science target in 8 months, low budget, 2 h/day).
- Case 2: Exam Study Schedule (5-month prep with weak quant/reasoning).
- Case 3: Skill Roadmap Comparison (web development, project-based preference).

For each case, the expected sequence is extraction -> analysis -> multi-plan generation -> scoring -> recommendation.

## Testing and Results
### Test Design
The project includes functional and non-functional test cases in `docs/test_cases.md`:
- Missing-field clarification behavior.
- End-to-end completion behavior for full inputs.
- Domain-specific planning behavior (career/study/skills).
- Repeatability and persistence checks.
- Export availability checks.

### Automated Test Modules
- `tests/test_collector.py`
- `tests/test_analyzer.py`
- `tests/test_planner.py`
- `tests/test_decision.py`
- `tests/test_orchestrator.py`

### Observed Outcome Summary
Based on the defined workflow and test coverage files, the system is designed for stable and structured responses with deterministic ranking behavior and persistent history capture.

## Limitations
- Heuristic extraction may miss unusual phrasing or implicit user intent.
- LLM-enhanced behavior depends on API configuration and model availability.
- Local SQLite persistence is single-instance oriented by default.
- Current deployment focuses on academic/demo scale rather than enterprise concurrency.

## Future Scope
- Add FastAPI service layer for API-first integration.
- Add authentication and role-based multi-user support.
- Improve semantic extraction using stronger model-assisted understanding.
- Add calendar integration, reminders, and milestone tracking.
- Introduce adaptive feedback loops from past user outcomes.

## Conclusion
The project successfully demonstrates a robust and explainable multi-agent system for personal planning and decision making. By separating responsibilities across specialized agents and combining structured extraction, analysis, plan generation, weighted scoring, and memory support, the system provides practical, auditable, and user-centered recommendations. The implementation is academically suitable and technically extensible for future production-grade enhancements.

## References
1. Streamlit Documentation
2. Python Documentation
3. Pytest Documentation
4. SQLite Documentation
5. OpenAI API Documentation

## Appendix
### A. Folder Structure (Summary)
- `app/agents`: agent modules
- `app/core`: orchestrator and scoring engine
- `app/services`: logging, evaluation, RAG, tools, export, validation
- `app/storage`: migrations and repositories
- `app/ui`: Streamlit UI and components
- `data`: seeded examples
- `docs`: architecture, samples, report, screenshots, tests
- `tests`: automated unit/integration-oriented tests

### B. Run Instructions
1. Create virtual environment.
2. Install dependencies from `requirements.txt`.
3. Launch Streamlit app via `streamlit run run.py`.

### C. Dependency List
Core dependencies include Streamlit, python-dotenv, OpenAI SDK, and pytest.

### D. Test Case Source
Detailed test definitions are documented in `docs/test_cases.md`.
