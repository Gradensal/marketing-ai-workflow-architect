from collections.abc import Callable

from fastapi import APIRouter, Depends

from backend.app.models import (
    ArchitectureAssessment,
    WorkflowAnalysis,
    WorkflowExplanation,
    WorkflowInput,
)
from backend.app.services import (
    assess_workflow,
    generate_workflow_explanation,
)


ExplanationGenerator = Callable[
    [WorkflowInput, ArchitectureAssessment],
    WorkflowExplanation,
]


router = APIRouter(
    prefix="/api/v1",
    tags=["Analysis"],
)


def get_explanation_generator() -> ExplanationGenerator:
    """
    Provide the explanation generator.

    FastAPI dependency injection allows tests to replace this
    external AI dependency without making live API calls.
    """

    return generate_workflow_explanation


@router.post(
    "/analyze",
    response_model=WorkflowAnalysis,
    summary="Assess and explain workflow architecture",
)
def analyze_workflow_endpoint(
    workflow: WorkflowInput,
    explanation_generator: ExplanationGenerator = Depends(
        get_explanation_generator
    ),
) -> WorkflowAnalysis:
    """
    Run deterministic architecture assessment first, then generate
    a stakeholder-friendly explanation of that existing decision.
    """

    assessment = assess_workflow(workflow)

    explanation = explanation_generator(
        workflow,
        assessment,
    )

    return WorkflowAnalysis(
        assessment=assessment,
        explanation=explanation,
    )