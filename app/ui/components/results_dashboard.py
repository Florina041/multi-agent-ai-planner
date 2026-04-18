from __future__ import annotations

import json

import streamlit as st

from app.models.schemas import WorkflowResult
from app.ui.components.comparison_table import render_comparison_table


def render_results_dashboard(result: WorkflowResult) -> None:
    if not result.final_response:
        return

    st.success("Workflow complete. Final recommendation generated.")

    tab1, tab2, tab3, tab4, tab5 = st.tabs(
        [
            "Summary",
            "Extracted Info",
            "Analysis",
            "Plan Comparison",
            "Final Action Plan",
        ]
    )

    with tab1:
        st.markdown(f"### {result.final_response.summary}")
        st.markdown(f"**Session ID:** {result.session_id}")

    with tab2:
        st.json(result.final_response.extracted_information)

    with tab3:
        st.json(result.final_response.analysis)

    with tab4:
        if result.decision_report:
            render_comparison_table(result.decision_report.ranking)
            st.markdown("### Selected Recommendation")
            st.json(result.final_response.recommendation)

    with tab5:
        for idx, step in enumerate(result.final_response.action_plan, start=1):
            st.write(f"{idx}. {step}")

        if result.final_response.warnings:
            st.markdown("### Warnings")
            for warning in result.final_response.warnings:
                st.write(f"- {warning}")

        st.markdown("### Next Steps")
        for item in result.final_response.next_steps:
            st.write(f"- {item}")

    with st.expander("Agent Activity Logs"):
        for entry in result.agent_logs:
            st.write(
                f"[{entry.agent}] {entry.step} | confidence={entry.confidence} | {entry.detail}"
            )

    with st.expander("Structured JSON Output"):
        st.code(json.dumps(result.final_response.model_dump(), indent=2), language="json")
