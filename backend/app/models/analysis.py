from typing import Literal

from pydantic import (
    BaseModel,
    ConfigDict,
    model_validator,
)

from backend.app.models.assessment import (
    ArchitectureAssessment,
)
from backend.app.models.explanation import (
    WorkflowExplanation,
)


ExplanationStatus = Literal[
    "available",
    "unavailable",
]


class WorkflowAnalysis(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )

    assessment: ArchitectureAssessment

    explanation: WorkflowExplanation | None = None

    explanation_status: ExplanationStatus = "available"

    explanation_message: str | None = None


    @model_validator(mode="after")
    def validate_explanation_state(
        self,
    ) -> "WorkflowAnalysis":
        if self.explanation_status == "available":
            if self.explanation is None:
                raise ValueError(
                    "An available explanation must include "
                    "WorkflowExplanation content."
                )

            if self.explanation_message is not None:
                raise ValueError(
                    "An available explanation must not "
                    "include an unavailable message."
                )

        if self.explanation_status == "unavailable":
            if self.explanation is not None:
                raise ValueError(
                    "An unavailable explanation must not "
                    "include WorkflowExplanation content."
                )

            if not self.explanation_message:
                raise ValueError(
                    "An unavailable explanation must include "
                    "a user-facing explanation message."
                )

        return self