from __future__ import annotations

import streamlit as st


def render_input_panel() -> tuple[str, str, bool]:
    st.subheader("Input / Collector Agent")
    domain = st.selectbox(
        "Select planning domain",
        options=["career", "study", "skill"],
        help="Choose the primary decision context.",
    )
    user_text = st.text_area(
        "Describe your goal, current status, timeline, constraints, and preferences",
        height=160,
        placeholder="Example: I am in 3rd year CSE, know Python basics, and want a data science job in 8 months...",
    )
    submit = st.button("Run Multi-Agent Planning", type="primary")
    return domain, user_text, submit
