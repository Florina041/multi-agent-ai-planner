from app.models.schemas import UserProfile


REQUIRED_FIELDS = ["goal", "timeline_months", "daily_time_hours"]


def detect_missing_fields(profile: UserProfile) -> list[str]:
    missing = []
    for field_name in REQUIRED_FIELDS:
        value = getattr(profile, field_name)
        if value in (None, "", []):
            missing.append(field_name)
    return missing
