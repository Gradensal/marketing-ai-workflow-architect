from pydantic import BaseModel, ConfigDict

from backend.app.models.assessment import ArchitectureAssessment
from backend.app.models.explanation import WorkflowExplanation


class WorkflowAnalysis(BaseModel):
    """
    Combined result containing the authoritative deterministic
    assessment and the generative stakeholder explanation.
    """

    model_config = ConfigDict(
        extra="forbid",
    )

    assessment: ArchitectureAssessment
    explanation: WorkflowExplanation