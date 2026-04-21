# Multi-Agent AI Decision and Planning System

A complete, original capstone project that demonstrates true agentic behavior for career/study/skill planning. The system accepts natural language goals, extracts structured details, analyzes user context, generates multiple roadmap options, compares them, and outputs a final explainable recommendation.

## Features
- Multi-agent architecture with clear role separation
- Collector agent for structured extraction and follow-up questions
- Analyzer agent for priorities, risks, and readiness
- Planner agent for multiple roadmap options
- Decision agent for weighted plan ranking and recommendation
- Response agent for clean human-readable output
- Memory agent for session history and recall
- Agent activity logs and confidence score
- JSON/text export support
- Streamlit dashboard with comparison and history views

## Architecture
The project follows layered modular architecture:
1. UI Layer: Streamlit dashboard
2. Orchestration Layer: coordinates all agent stages
3. Agent Layer: six focused agents
4. Data Layer: SQLite persistence
5. Service Layer: export, validation, logging

Typed schema contracts are implemented with Python dataclasses for compatibility and clarity.

Decision score formula:

Score(plan) = 0.35*GoalAlignment + 0.25*TimeFeasibility + 0.20*SkillGapFit + 0.20*Sustainability - RiskPenalty

## Folder Structure
```text
capstone_multi_agent_planner/
  app/
    agents/
    core/
    llm/
    models/
    services/
    storage/
    ui/
    utils/
  data/
  tests/
  requirements.txt
  README.md
  run.py
```

## Agent Responsibilities
- Collector Agent: extracts goal, skills, constraints, timeline, preferences; asks clarifications
- Analyzer Agent: identifies needs, priorities, risks, assumptions
- Planner Agent: creates 3 plan options with milestones and weekly blocks
- Decision Agent: scores and selects best option
- Response Agent: generates final structured recommendation
- Memory Agent: stores/retrieves session interactions

## Workflow
1. User submits natural language input
2. Collector extracts structured profile
3. Missing fields trigger clarification questions
4. Analyzer interprets user context
5. Planner generates candidate plans
6. Decision ranks and selects best plan
7. Response formats final output
8. Memory stores complete interaction

## Setup and Run
1. Create virtual environment
2. Install dependencies
3. Run Streamlit app

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run run.py
```

Optional environment file:
- Copy `.env.example` to `.env`
- Add `OPENAI_API_KEY` if you want model-backed extensions

## Run Tests
```powershell
pytest -q
```
## Originality Note
This codebase is designed specifically for this capstone prompt with explicit multi-agent modules and explainable workflow, not a single-chatbot wrapper.
