from pydantic import BaseModel, ConfigDict, Field


class WorkflowInput(BaseModel):
    """
    Structured description of a business workflow submitted
    to the architecture decision engine.
    """

    model_config = ConfigDict(
        str_strip_whitespace=True,
        extra="forbid",
    )

    name: str = Field(
        min_length=3,
        max_length=120,
        description="Short, human-readable name for the workflow.",
    )

    team: str = Field(
        min_length=2,
        max_length=80,
        description="Business team responsible for the workflow.",
    )

    description: str = Field(
        min_length=20,
        max_length=1500,
        description="Plain-language description of how the workflow operates.",
    )

    repeatability: int = Field(
        ge=1,
        le=5,
        description=(
            "How predictable and repeatable the workflow is. "
            "1 means highly variable; 5 means highly repeatable."
        ),
    )

    ambiguity: int = Field(
        ge=1,
        le=5,
        description=(
            "How much interpretation or judgment the workflow requires. "
            "1 means rules are clear; 5 means substantial judgment is needed."
        ),
    )

    tool_use: int = Field(
        ge=1,
        le=5,
        description=(
            "How much the workflow depends on other tools, systems, "
            "or information sources."
        ),
    )

    external_actions: int = Field(
        ge=1,
        le=5,
        description=(
            "How consequentially the workflow acts on external systems. "
            "1 means mostly read-only; 5 means significant external actions."
        ),
    )

    business_risk: int = Field(
        ge=1,
        le=5,
        description=(
            "Potential business impact of an incorrect result or action. "
            "1 means minor impact; 5 means severe impact."
        ),
    )

    data_sensitivity: int = Field(
        ge=1,
        le=5,
        description=(
            "Sensitivity of the information handled by the workflow. "
            "1 means public/non-sensitive; 5 means highly sensitive."
        ),
    )

    mandatory_human_approval: bool = Field(
        default=False,
        description=(
            "Whether organizational policy already requires a human "
            "to approve consequential workflow actions."
        ),
    )
