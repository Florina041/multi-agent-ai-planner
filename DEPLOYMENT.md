# Deployment Guide

This project is deployment-ready for both Render and Streamlit Community Cloud.

## Option 1: Render (Recommended)

1. Push this project to a GitHub repository.
2. Open Render dashboard and click New > Blueprint.
3. Connect the repository and select this project.
4. Render auto-detects `render.yaml`.
5. Add environment variable in Render:
   - `OPENAI_API_KEY` (optional if running heuristic-only mode)
6. Deploy.

Start command used:

```bash
streamlit run run.py --server.port=$PORT --server.address=0.0.0.0
```

## Option 2: Streamlit Community Cloud

1. Push this project to GitHub.
2. Open Streamlit Community Cloud and click Create app.
3. Select repository and branch.
4. Set main file path to:

```text
app/ui/streamlit_app.py
```

5. Add secrets in Streamlit settings (optional):
   - `OPENAI_API_KEY`
   - `OPENAI_MODEL`

## Option 3: Docker (Any VM / Cloud Run / Azure / ECS)

Build image:

```bash
docker build -t multi-agent-ai-planner .
```

Run container:

```bash
docker run -p 8501:8501 -e OPENAI_API_KEY=your_key multi-agent-ai-planner
```

## Health and Verification Checklist

- App opens successfully at deployed URL.
- Clarification flow appears for incomplete input.
- Full run produces plan comparison and recommendation.
- Export buttons work.
- History table persists interactions.

## Production Notes

- SQLite is fine for demo and viva deployment.
- For multi-user production, switch to managed PostgreSQL.
- Keep API keys in platform secret manager, never commit `.env`.
