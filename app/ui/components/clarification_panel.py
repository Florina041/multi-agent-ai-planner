from __future__ import annotations

import streamlit as st


def render_clarification_panel(questions: list[str]) -> str:
    st.warning("Some critical details are missing. Please answer these follow-up questions.")
    answer_blocks = []
    for idx, item in enumerate(questions, start=1):
        answer = st.text_input(f"Q{idx}: {item}")
        if answer:
            answer_blocks.append(f"{item} {answer}")
    return " ".join(answer_blocks)
