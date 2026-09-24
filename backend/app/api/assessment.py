from fastapi import APIRouter

from backend.app.models import (
    ArchitectureAssessment,
    WorkflowInput,
)
from backend.app.services import assess_workflow


router = APIRouter(
    prefix="/api/v1",
    tags=["Assessment"],
)


@router.post(
    "/assess",
    response_model=ArchitectureAssessment,
    summary="Assess workflow architecture",
)
def assess_workflow_endpoint(
    workflow: WorkflowInput,
) -> ArchitectureAssessment:
    """
    Evaluate a business workflow and return a structured
    architecture recommendation.
    """

    return assess_workflow(workflow)