# Multi-Agent AI Decision and Planning System

## Title Page
- Project Title
- Student Name
- Roll Number
- Department
- Institution
- Guide Name
- Academic Year

## Abstract
This project proposes and implements a modular multi-agent AI system for decision support and planning in career/study domains. The system accepts natural language goals, extracts structured intent, performs analysis, generates multiple plan options, and recommends the best roadmap using weighted decision logic. It includes explainable outputs, confidence scoring, activity logs, and memory/history support.

## Problem Statement
Students and early professionals struggle to convert high-level goals into actionable, realistic roadmaps under constraints like limited time, weak foundations, and budget limits. Conventional chatbots provide generic responses and do not clearly separate reasoning stages.

## Objectives
- Design a true multi-agent planning workflow.
- Extract structured information from natural language input.
- Generate and compare multiple candidate plans.
- Provide explainable recommendation with confidence score.
- Store history and support repeat interactions.

## Importance of the Project
- Improves decision quality and planning clarity.
- Demonstrates practical agentic AI architecture.
- Supports personalized and iterative user guidance.

## System Architecture
- UI Layer: Streamlit dashboard
- Orchestration Layer: workflow controller
- Agent Layer: Collector, Analyzer, Planner, Decision, Response, Memory
- Data Layer: SQLite persistence

## Agent Responsibilities
- Collector Agent: data extraction + clarification detection
- Analyzer Agent: needs/priorities/risks interpretation
- Planner Agent: generates 3 roadmap options
- Decision Agent: weighted plan comparison and selection
- Response Agent: human-readable final response
- Memory Agent: persistence and recall

## Workflow Explanation
1. User submits input.
2. Collector extracts profile and asks missing details.
3. Analyzer builds analytical understanding.
4. Planner generates options.
5. Decision ranks and recommends.
6. Response produces structured final output.
7. Memory stores session data.

## Technology Stack
- Python
- Streamlit
- Dataclasses
- SQLite
- Optional OpenAI model adapter

## Implementation Details
- Dataclass schemas enforce data contracts.
- Orchestrator coordinates all agents.
- Decision uses weighted utility formula.
- Exports available in JSON and text formats.

## Screenshots and UI Explanation
Insert screenshots from docs/screenshots with labels and descriptions.

## Sample Inputs and Outputs
Include 3 representative cases from docs/samples/sample_inputs_outputs.md.

## Testing and Results
- Unit tests for all key agents.
- Integration test for full workflow.
- Observed stable responses for repeated runs.

## Limitations
- Heuristic extraction may miss unusual language patterns.
- LLM enhancement is optional and key-dependent.
- Single-user local persistence by default.

## Future Scope
- Add FastAPI service layer.
- Add role-based user accounts.
- Use stronger model-based semantic extraction.
- Add calendar integration and reminders.

## Conclusion
The project demonstrates a robust and explainable multi-agent planning system suitable for academic evaluation and practical deployment in educational guidance scenarios.

## References
1. Streamlit Documentation
2. Python Dataclasses Documentation
3. SQLite Documentation
4. OpenAI API Documentation

## Appendix
- Folder structure
- Run instructions
- Dependency list
- Test cases
