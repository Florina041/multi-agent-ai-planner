class ToolService:
    def estimate_study_hours(self, hours_per_day: int, weeks: int) -> str:
        total = hours_per_day * 7 * weeks
        return f"Estimated total effort: {total} hours over {weeks} weeks"