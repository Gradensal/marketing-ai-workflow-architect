from pydantic import BaseModel, ConfigDict, Field


class WorkflowExplanation(BaseModel):
    """
    Stakeholder-friendly explanation of an architecture assessment.

    This model communicates an existing deterministic decision.
    It does not replace or modify the ArchitectureAssessment.
    """

    model_config = ConfigDict(
        extra="forbid",
    )

    why_this_approach: str = Field(
        min_length=20,
        max_length=1200,
    )

    why_not_more_autonomy: str = Field(
        min_length=20,
        max_length=1200,
    )

    proposed_architecture: str = Field(
        min_length=20,
        max_length=1500,
    )

    human_checkpoint: str = Field(
        min_length=10,
        max_length=1000,
    )

    first_experiment: str = Field(
        min_length=20,
        max_length=1200,
    )

    success_metric: str = Field(
        min_length=10,
        max_length=800,
    )
    