import pytest
from pydantic import ValidationError

from backend.app.models import (
    ArchitectureAssessment,
    ArchitectureRecommendation,
    RiskLevel,
    WorkflowAnalysis,
    WorkflowExplanation,
)


def make_assessment() -> ArchitectureAssessment:
    return ArchitectureAssessment(
        recommendation=(
            ArchitectureRecommendation.LLM_ASSISTED_WORKFLOW
        ),
        risk_level=RiskLevel.LOW,
        decision_strength=4,
        human_approval_required=False,
        human_approval_reason=None,
        rationale=[
            "The workflow benefits from interpretation and generation."
        ],
        warnings=[
            "Generated marketing content should be reviewed."
        ],
    )


def make_explanation() -> WorkflowExplanation:
    return WorkflowExplanation(
        why_this_approach=(
            "An LLM can help generate useful first drafts while "
            "keeping the workflow bounded and understandable."
        ),
        why_not_more_autonomy=(
            "The workflow does not require autonomous actions or "
            "dynamic tool selection."
        ),
        proposed_architecture=(
            "Use a structured LLM-assisted drafting workflow with "
            "campaign context supplied as controlled input."
        ),
        human_checkpoint=(
            "A marketer reviews generated drafts before publication."
        ),
        first_experiment=(
            "Test the workflow on a small set of campaign briefs and "
            "compare generated drafts with the existing process."
        ),
        success_metric=(
            "Measure usable-draft rate and average editing effort."
        ),
    )


def test_valid_workflow_analysis_is_accepted():
    result = WorkflowAnalysis(
        assessment=make_assessment(),
        explanation=make_explanation(),
    )

    assert (
        result.assessment.recommendation
        == ArchitectureRecommendation.LLM_ASSISTED_WORKFLOW
    )

    assert (
        "marketer"
        in result.explanation.human_checkpoint.lower()
    )


def test_unexpected_fields_are_rejected():
    with pytest.raises(ValidationError):
        WorkflowAnalysis(
            assessment=make_assessment(),
            explanation=make_explanation(),
            hidden_agent_decision=True,
        )