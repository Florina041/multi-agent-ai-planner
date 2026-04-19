from __future__ import annotations

import json
import streamlit as st

from app.core.orchestrator import MultiAgentOrchestrator
from app.services.export_service import ExportService
from app.ui.components.clarification_panel import render_clarification_panel
from app.ui.components.input_panel import render_input_panel
from app.ui.components.results_dashboard import render_results_dashboard
from app.utils.constants import DEFAULT_DATABASE_PATH


def _init_state() -> None:
    defaults = {
        "session_id": None,
        "pending_questions": [],
        "last_domain": "career",
        "last_user_text": "",
        "last_result": None,
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def main() -> None:
    st.set_page_config(
        page_title="Multi-Agent AI Decision and Planning System",
        layout="wide",
    )
    _init_state()

    st.title("Multi-Agent AI Decision and Planning System")
    st.caption(
        "Collector -> Analyzer -> Planner -> Decision -> Response (+ Memory)"
    )

    orchestrator = MultiAgentOrchestrator(db_path=DEFAULT_DATABASE_PATH)
    exporter = ExportService()

    col1, col2 = st.columns([2, 1])
    with col1:
        domain, user_text, submit = render_input_panel()
    with col2:
        st.subheader("Quick Tips")
        st.write("- Include timeline in months")
        st.write("- Mention available daily hours")
        st.write("- Add constraints and preferences")

    if submit and user_text.strip():
        st.session_state["last_domain"] = domain
        st.session_state["last_user_text"] = user_text.strip()

        result = orchestrator.run(
            user_text=user_text.strip(),
            domain=domain,
            session_id=st.session_state["session_id"],
        )
        st.session_state["session_id"] = result.session_id
        st.session_state["last_result"] = result

        if result.status == "need_clarification":
            st.session_state["pending_questions"] = result.questions
        else:
            st.session_state["pending_questions"] = []

    if st.session_state["pending_questions"]:
        st.subheader("Clarification Required")
        clarification = render_clarification_panel(st.session_state["pending_questions"])
        if st.button("Submit Clarifications") and clarification.strip():
            merged_input = (
                st.session_state["last_user_text"] + " " + clarification.strip()
            )
            result = orchestrator.run(
                user_text=merged_input,
                domain=st.session_state["last_domain"],
                session_id=st.session_state["session_id"],
            )
            st.session_state["last_result"] = result
            st.session_state["pending_questions"] = (
                result.questions if result.status == "need_clarification" else []
            )

    result = st.session_state.get("last_result")

    # 🔥 UPDATED SECTION (RAG + Evaluation + Tool)
    if result and result.status == "complete":
        render_results_dashboard(result)

        st.subheader("🔍 Retrieved Knowledge")
        st.write(getattr(result, "rag_context", "Not available"))

        st.subheader("📊 Faithfulness Score")
        st.write(getattr(result, "faithfulness_score", "Not available"))

        st.subheader("🛠 Tool Insight")
        st.write(getattr(result, "tool_output", "Not available"))

        # Export Section
        st.subheader("Export")
        payload = result.final_response.model_dump() if result.final_response else {}
        json_text = json.dumps(payload, indent=2)

        st.download_button(
            label="Download JSON",
            data=json_text,
            file_name=f"plan_result_{result.session_id}.json",
            mime="application/json",
        )

        text_report = (
            f"Summary: {payload.get('summary', '')}\n"
            f"Recommendation: {payload.get('recommendation', {})}\n"
            f"Action Plan: {payload.get('action_plan', [])}\n"
            f"Warnings: {payload.get('warnings', [])}\n"
        )

        st.download_button(
            label="Download Text Report",
            data=text_report,
            file_name=f"plan_result_{result.session_id}.txt",
            mime="text/plain",
        )

        if st.button("Save Export Files on Disk"):
            exporter.export_json(result.session_id, payload)
            exporter.export_text(result.session_id, text_report)
            st.success("Files exported to local exports folder.")

    # History Section
    st.subheader("Recent Interaction History")
    history = orchestrator.get_history(limit=10)
    if history:
        st.dataframe(history, use_container_width=True, hide_index=True)
    else:
        st.info("No interactions stored yet.")


if __name__ == "__main__":
    main()