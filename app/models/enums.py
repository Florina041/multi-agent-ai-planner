from enum import Enum


class DomainType(str, Enum):
    CAREER = "career"
    STUDY = "study"
    SKILL = "skill"


class WorkflowStatus(str, Enum):
    NEED_CLARIFICATION = "need_clarification"
    COMPLETE = "complete"
