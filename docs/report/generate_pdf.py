"""
Generate Capstone Report PDF with proper formatting per guidelines:
- A4, Justified, Page numbers (bottom-right)
- Arial: 15px Heading, 14px Subheading, 12px Body
"""
import os
from fpdf import FPDF

# Find Arial TTF on Windows
ARIAL_DIR = r"C:\Windows\Fonts"

class ReportPDF(FPDF):
    def __init__(self):
        super().__init__("P", "mm", "A4")
        # Register real Arial TTF for Unicode support
        self.add_font("ArialUni", "", os.path.join(ARIAL_DIR, "arial.ttf"), uni=True)
        self.add_font("ArialUni", "B", os.path.join(ARIAL_DIR, "arialbd.ttf"), uni=True)
        self.add_font("ArialUni", "I", os.path.join(ARIAL_DIR, "ariali.ttf"), uni=True)
        self.add_font("ArialUni", "BI", os.path.join(ARIAL_DIR, "arialbi.ttf"), uni=True)

    def header(self):
        pass

    def footer(self):
        self.set_y(-15)
        self.set_font("ArialUni", "I", 9)
        self.cell(0, 10, f"Page {self.page_no()}", new_x="RIGHT", new_y="TOP", align="R")

    def add_heading(self, text):
        self.set_font("ArialUni", "B", 15)
        self.set_text_color(20, 60, 120)
        self.cell(0, 10, text, new_x="LMARGIN", new_y="NEXT")
        self.set_draw_color(20, 60, 120)
        self.set_line_width(0.5)
        self.line(self.l_margin, self.get_y(), self.w - self.r_margin, self.get_y())
        self.ln(4)
        self.set_text_color(0, 0, 0)

    def add_subheading(self, text):
        self.set_font("ArialUni", "B", 14)
        self.set_text_color(40, 80, 140)
        self.cell(0, 9, text, new_x="LMARGIN", new_y="NEXT")
        self.ln(2)
        self.set_text_color(0, 0, 0)

    def add_body(self, text):
        self.set_font("ArialUni", "", 12)
        self.multi_cell(0, 6.5, text, align="J")
        self.ln(2)

    def add_bullet(self, text):
        self.set_font("ArialUni", "", 12)
        x_start = self.get_x()
        self.cell(8, 6.5, "\u2022  ", new_x="RIGHT", new_y="TOP")
        self.multi_cell(0, 6.5, text, align="J")
        self.ln(1)

    def add_bold_bullet(self, bold_part, normal_part):
        self.set_font("ArialUni", "", 12)
        self.cell(8, 6.5, "\u2022  ", new_x="RIGHT", new_y="TOP")
        x_after_bullet = self.get_x()
        y_start = self.get_y()
        self.set_font("ArialUni", "B", 12)
        w_bold = self.get_string_width(bold_part + " ")
        self.cell(w_bold, 6.5, bold_part + " ", new_x="RIGHT", new_y="TOP")
        self.set_font("ArialUni", "", 12)
        # Calculate remaining width
        remaining = self.w - self.r_margin - self.get_x()
        if self.get_string_width(normal_part) <= remaining:
            self.cell(0, 6.5, normal_part, new_x="LMARGIN", new_y="NEXT")
        else:
            self.multi_cell(0, 6.5, normal_part, align="J")
        self.ln(1)

    def add_table_row(self, col1, col2, is_header=False):
        if is_header:
            self.set_font("ArialUni", "B", 12)
            self.set_fill_color(20, 60, 120)
            self.set_text_color(255, 255, 255)
        else:
            self.set_font("ArialUni", "", 12)
            row_idx = getattr(self, '_row_idx', 0)
            if row_idx % 2 == 0:
                self.set_fill_color(240, 242, 248)
            else:
                self.set_fill_color(250, 250, 255)
            self.set_text_color(0, 0, 0)
            self._row_idx = row_idx + 1

        self.cell(55, 8, " " + col1, 1, 0, "L", True)
        self.cell(0, 8, " " + col2, 1, 1, "L", True)
        self.set_text_color(0, 0, 0)


def generate_report():
    pdf = ReportPDF()
    pdf.set_auto_page_break(auto=True, margin=20)
    pdf.add_page()

    # ===== TITLE PAGE =====
    pdf.ln(30)
    pdf.set_font("ArialUni", "B", 24)
    pdf.set_text_color(20, 60, 120)
    pdf.multi_cell(0, 13, "Multi-Agent AI Decision\nand Planning System", align="C")
    pdf.ln(4)
    pdf.set_font("ArialUni", "I", 14)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(0, 10, "Personal Planning and Decision Making", new_x="LMARGIN", new_y="NEXT", align="C")
    pdf.ln(10)

    # Divider line
    pdf.set_draw_color(20, 60, 120)
    pdf.set_line_width(0.8)
    pdf.line(60, pdf.get_y(), 150, pdf.get_y())
    pdf.ln(10)

    # Student details
    details = [
        ("Student Name", "Florina Sahu"),
        ("Roll Number", "2329030"),
        ("Batch / Program", "B.Tech CSE, 2023\u20132027"),
        ("Department", "Computer Science"),
        ("Institution", "Kalinga Institute of Industrial Technology (KIIT)"),
        ("Academic Year", "2025\u201326"),
    ]
    for label, value in details:
        pdf.set_font("ArialUni", "B", 13)
        pdf.set_text_color(40, 40, 40)
        pdf.cell(55, 9, label + ":", new_x="RIGHT", new_y="TOP", align="R")
        pdf.set_font("ArialUni", "", 13)
        pdf.set_text_color(0, 0, 0)
        pdf.cell(0, 9, "  " + value, new_x="LMARGIN", new_y="NEXT")

    pdf.ln(20)
    pdf.set_font("ArialUni", "I", 10)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(0, 10, "Capstone Project  |  April 2026", new_x="LMARGIN", new_y="NEXT", align="C")

    # ===== PAGE 2: Problem Statement =====
    pdf.add_page()

    pdf.add_heading("1. Problem Statement")
    pdf.add_body(
        "Students and early-career professionals frequently struggle to convert broad, ambiguous goals "
        "such as \"I want to become a data scientist\" or \"I need to prepare for placements\" into "
        "realistic, actionable plans. The challenges are compounded by real-world constraints: limited "
        "daily study hours, weak prerequisite skills, tight budgets, and looming deadlines."
    )
    pdf.add_body(
        "Existing tools and chatbot-style assistants typically return generic, one-size-fits-all advice "
        "without separating distinct reasoning stages or explaining why a particular recommendation was "
        "made. There is no transparency in how options were compared or which trade-offs were considered."
    )
    pdf.add_body(
        "This project addresses that gap by building a true multi-agent AI pipeline where each stage has "
        "a clearly defined role, and the final recommendation is fully explainable and auditable."
    )

    # ===== Solution and Features =====
    pdf.add_heading("2. Solution and Features")
    pdf.add_body(
        "The system is a modular multi-agent AI application that accepts natural language user goals and "
        "produces personalized, explainable planning recommendations through a structured pipeline of "
        "six specialized agents."
    )

    pdf.add_subheading("Core Features")
    features = [
        ("Natural Language Input:", "Users describe goals in plain English (e.g., \"I want a backend developer role in 10 months, I know Python basics\")."),
        ("Structured Profile Extraction:", "The Collector Agent parses input to extract goal, timeline, daily hours, current skills, constraints, and preferences."),
        ("Smart Clarification Loop:", "If critical fields are missing, the system generates follow-up questions before proceeding."),
        ("Context-Aware Analysis:", "The Analyzer Agent evaluates readiness, identifies priorities, detects risks, and flags assumptions."),
        ("Multi-Option Plan Generation:", "The Planner Agent creates three distinct roadmap options with milestones and weekly blocks."),
        ("Weighted Decision Scoring:", "The Decision Agent ranks all options using a transparent scoring formula."),
        ("Explainable Recommendations:", "The Response Agent produces human-readable output with the recommended plan, action steps, and risk warnings."),
        ("Session Memory & Export:", "The Memory Agent stores interactions in SQLite; results can be exported in JSON and text formats."),
    ]
    for bold, normal in features:
        pdf.add_bold_bullet(bold, normal)

    pdf.ln(2)
    pdf.add_subheading("Decision Scoring Formula")
    pdf.set_font("ArialUni", "B", 11)
    pdf.set_fill_color(240, 242, 248)
    pdf.set_draw_color(20, 60, 120)
    pdf.multi_cell(0, 7,
        "  Score(plan) = 0.35 x GoalAlignment + 0.25 x TimeFeasibility\n"
        "                       + 0.20 x SkillGapFit + 0.20 x Sustainability - RiskPenalty",
        border=1, align="L", fill=True)
    pdf.ln(3)
    pdf.set_font("ArialUni", "", 12)
    pdf.add_body("This formula balances desirability, feasibility, and risk awareness to select the optimal plan.")

    pdf.add_subheading("Agent Pipeline Workflow")
    steps = [
        "User submits a natural language prompt via the Streamlit dashboard.",
        "Collector Agent extracts structured profile fields from the input.",
        "If required fields are missing, clarification questions are generated.",
        "Analyzer Agent interprets needs, risks, and priorities.",
        "Planner Agent produces three roadmap alternatives.",
        "Decision Agent scores, ranks, and selects the best option.",
        "Response Agent creates the final user-facing recommendation.",
        "Memory Agent stores interaction payloads for retrieval and review.",
    ]
    for i, step in enumerate(steps, 1):
        pdf.set_font("ArialUni", "B", 12)
        pdf.cell(8, 6.5, f"{i}.", new_x="RIGHT", new_y="TOP")
        pdf.set_font("ArialUni", "", 12)
        pdf.multi_cell(0, 6.5, step, align="J")
        pdf.ln(1)

    # ===== Screenshots =====
    pdf.add_page()
    pdf.add_heading("3. Screenshots")
    pdf.add_body(
        "The following screenshots are captured from the running Streamlit application and are "
        "available in the docs/screenshots/ directory of the project repository:"
    )
    screenshots = [
        ("Home Screen (ui_home.png):", "Main input panel with domain selector, goal text area, and quick-start tips."),
        ("Clarification View (ui_clarification.png):", "Follow-up questions generated when the user provides incomplete input."),
        ("Plan Comparison (ui_plan_comparison.png):", "Side-by-side comparison of three roadmap options with weighted scores."),
        ("Final Recommendation (ui_final_recommendation.png):", "Selected plan with action steps, weekly schedule, and risk warnings."),
        ("History View (ui_history.png):", "Table of recent interactions retrieved from the SQLite database."),
    ]
    for bold, normal in screenshots:
        pdf.add_bold_bullet(bold, normal)

    # ===== Tech Stack =====
    pdf.ln(3)
    pdf.add_heading("4. Tech Stack")
    pdf._row_idx = 0
    tech_data = [
        ("Layer", "Technology"),
        ("Language", "Python 3.10+"),
        ("UI Framework", "Streamlit"),
        ("Data Modeling", "Python Dataclasses / Pydantic-style"),
        ("Persistence", "SQLite"),
        ("Testing", "Pytest"),
        ("LLM Integration", "OpenAI API / Gemini (optional)"),
        ("Environment", "python-dotenv"),
        ("Deployment", "Render, Streamlit Cloud, Docker"),
    ]
    for i, (col1, col2) in enumerate(tech_data):
        pdf.add_table_row(col1, col2, is_header=(i == 0))

    # ===== Unique Points =====
    pdf.ln(5)
    pdf.add_heading("5. Unique Points")
    unique = [
        ("True Multi-Agent Architecture:", "Unlike single-chatbot projects, this system decomposes planning into six distinct agents with clear role separation and structured data contracts."),
        ("Explainable Decision Logic:", "Every recommendation includes a transparent weighted score breakdown showing why a plan was chosen."),
        ("Clarification Loop:", "The system proactively detects missing information and asks targeted follow-up questions, mimicking a human advisor."),
        ("Deterministic & Auditable:", "The scoring formula and agent logs ensure repeatable outputs reviewable stage-by-stage."),
        ("Typed Inter-Agent Contracts:", "Dataclass schemas (UserProfile, AnalysisReport, PlanOption, DecisionReport, FinalResponse) enforce predictable data handoff."),
        ("Session Persistence:", "SQLite-backed memory allows users to revisit past sessions and track goal evolution."),
    ]
    for bold, normal in unique:
        pdf.add_bold_bullet(bold, normal)

    # ===== Future Improvements =====
    pdf.add_heading("6. Future Improvements")
    improvements = [
        "Add a FastAPI service layer for API-first integration and third-party access.",
        "Implement user authentication and role-based multi-user support.",
        "Improve semantic extraction using advanced language models for nuanced understanding.",
        "Integrate with Google Calendar for milestone reminders and deadline tracking.",
        "Introduce adaptive feedback loops where past outcomes improve future recommendations.",
        "Migrate from SQLite to PostgreSQL for concurrent multi-user production scaling.",
    ]
    for imp in improvements:
        pdf.add_bullet(imp)

    # ===== References =====
    pdf.ln(2)
    pdf.add_heading("7. References")
    refs = [
        "Streamlit Documentation - https://docs.streamlit.io",
        "Python Documentation - https://docs.python.org/3/",
        "Pytest Documentation - https://docs.pytest.org",
        "SQLite Documentation - https://www.sqlite.org/docs.html",
        "OpenAI API Reference - https://platform.openai.com/docs",
    ]
    for i, ref in enumerate(refs, 1):
        pdf.set_font("ArialUni", "", 12)
        pdf.cell(0, 7, f"{i}. {ref}", new_x="LMARGIN", new_y="NEXT")

    # Save
    output_path = r"x:\git_demo\AgenticAI_kiit\2329030\Capstone\docs\report\Capstone_Report_Florina_Sahu.pdf"
    pdf.output(output_path)
    print(f"PDF generated successfully: {output_path}")
    print(f"Total pages: {pdf.page_no()}")


if __name__ == "__main__":
    generate_report()
