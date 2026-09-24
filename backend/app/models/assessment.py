from enum import StrEnum

from pydantic import BaseModel, ConfigDict, Field, model_validator


class ArchitectureRecommendation(StrEnum):
    """
    Supported architecture recommendations produced by
    the deterministic decision engine.
    """

    DETERMINISTIC_AUTOMATION = "deterministic_automation"
    LLM_ASSISTED_WORKFLOW = "llm_assisted_workflow"
    AGENTIC_WORKFLOW = "agentic_workflow"
    KEEP_HUMAN_REDESIGN_FIRST = "keep_human_redesign_first"


class RiskLevel(StrEnum):
    """
    High-level risk classification for the workflow.
    """

    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class ArchitectureAssessment(BaseModel):
    """
    Structured result produced by the architecture
    decision engine.
    """

    model_config = ConfigDict(
        extra="forbid",
    )

    recommendation: ArchitectureRecommendation

    risk_level: RiskLevel

    decision_strength: int = Field(
        ge=1,
        le=5,
        description=(
            "Strength of the explicit rule match supporting the "
            "recommendation. This is not a statistical confidence score."
        ),
    )

    human_approval_required: bool

    human_approval_reason: str | None = Field(
        default=None,
        max_length=500,
    )

    rationale: list[str] = Field(
        min_length=1,
        description="Human-readable reasons supporting the recommendation.",
    )

    warnings: list[str] = Field(
        default_factory=list,
        description="Important limitations, risks, or cautionary notes.",
    )

    @model_validator(mode="after")
    def validate_human_approval_reason(self):
        if (
            self.human_approval_required
            and not self.human_approval_reason
        ):
            raise ValueError(
                "human_approval_reason is required when "
                "human_approval_required is True"
            )

        return self