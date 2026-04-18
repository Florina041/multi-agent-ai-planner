from __future__ import annotations

import streamlit as st


def render_comparison_table(ranking: list[dict]) -> None:
    st.subheader("Decision Agent: Plan Comparison")
    st.dataframe(ranking, use_container_width=True, hide_index=True)
