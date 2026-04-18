# Final Presentation Strategy (Viva + Demo)

## 12-15 Minute Flow
1. Problem and motivation (1.5 min)
2. Why this is multi-agent and not chatbot wrapper (2 min)
3. Architecture and agent roles (2 min)
4. Live demo on one career case (4 min)
5. Plan comparison and weighted decision logic (2 min)
6. Memory/history and export features (1 min)
7. Limitations and future scope (1.5 min)

## Demo Checklist
- Keep 3 prepared inputs (career, study, skill)
- Show clarification behavior with incomplete input
- Show ranked comparison table and selected plan
- Show activity logs from each agent
- Show history persistence and export

## Likely Viva Questions and Suggested Direction
1. Why multi-agent design?
- Clear module boundaries, explainability, testability.

2. How is recommendation justified?
- Weighted scoring over objective criteria and risk penalty.

3. What if input is incomplete?
- Collector asks dynamic clarification questions before analysis.

4. How is personalization done?
- Memory agent stores interaction history and recalls context.

5. How can this be extended?
- Add FastAPI backend, richer LLM extraction, user account profiles.
