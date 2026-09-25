import logging

from collections.abc import Callable

from fastapi import (
    APIRouter,
    Depends,
)

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


logger = logging.getLogger(__name__)


router = APIRouter(
    prefix="/api/v1",
    tags=["analysis"],
)


ExplanationGenerator = Callable[
    [
        WorkflowInput,
        ArchitectureAssessment,
    ],
    WorkflowExplanation,
]


def get_explanation_generator(
) -> ExplanationGenerator:
    return generate_workflow_explanation


@router.post(
    "/analyze",
    response_model=WorkflowAnalysis,
)
def analyze_workflow(
    workflow: WorkflowInput,
    explanation_generator: ExplanationGenerator = Depends(
        get_explanation_generator,
    ),
) -> WorkflowAnalysis:
    """
    Analyze a workflow in two deliberately separated stages.

    Stage 1:
    The deterministic decision engine produces the
    authoritative architecture assessment.

    Stage 2:
    The AI explanation service translates that assessment
    into stakeholder-friendly guidance.

    If Stage 2 fails, Stage 1 remains valid and is still
    returned to the caller.
    """

    assessment = assess_workflow(
        workflow,
    )


    try:
        explanation = explanation_generator(
            workflow,
            assessment,
        )

    except Exception:
        logger.exception(
            "AI explanation generation failed after "
            "the deterministic assessment completed."
        )

        return WorkflowAnalysis(
            assessment=assessment,
            explanation=None,
            explanation_status="unavailable",
            explanation_message=(
                "The architecture assessment completed "
                "successfully, but the AI explanation is "
                "temporarily unavailable. The deterministic "
                "recommendation remains valid."
            ),
        )


    return WorkflowAnalysis(
        assessment=assessment,
        explanation=explanation,
        explanation_status="available",
        explanation_message=None,
    )