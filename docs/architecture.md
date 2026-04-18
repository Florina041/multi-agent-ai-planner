# Detailed Architecture

## Components
- Streamlit UI
- MultiAgentOrchestrator
- Six agents (Collector, Analyzer, Planner, Decision, Response, Memory)
- SQLite interaction repository
- Export and logging services

## Data Contracts
Dataclass models are used to enforce reliable data handoff:
- UserProfile
- AnalysisReport
- PlanOption
- DecisionReport
- FinalResponse
- WorkflowResult

## Sequence
1. Input -> Collector
2. Collector -> Clarification (if needed)
3. Collector -> Analyzer
4. Analyzer -> Planner
5. Planner -> Decision
6. Decision + previous outputs -> Response
7. Response -> UI + Memory storage

## Explainability
- Each stage logs agent actions and confidence
- Decision exposes ranked options with weighted scores
- Final response includes recommendation reasoning and warnings
