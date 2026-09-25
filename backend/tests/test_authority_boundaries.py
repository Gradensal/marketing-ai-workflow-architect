from backend.app.models import (
    ArchitectureRecommendation,
    RiskLevel,
    WorkflowInput,
)
from backend.app.services import assess_workflow


def make_workflow(
    *,
    repeatability: int = 3,
    ambiguity: int = 3,
    tool_use: int = 3,
    external_actions: int = 2,
    business_risk: int = 2,
    data_sensitivity: int = 2,
) -> WorkflowInput:
    return WorkflowInput(
        name="Authority Boundary Test",
        team="Marketing Operations",
        description=(
            "Evaluate a representative marketing workflow "
            "for architecture and governance boundaries."
        ),
        repeatability=repeatability,
        ambiguity=ambiguity,
        tool_use=tool_use,
        external_actions=external_actions,
        business_risk=business_risk,
        data_sensitivity=data_sensitivity,
        mandatory_human_approval=False,
    )


def test_high_risk_overrides_agentic_characteristics() -> None:
    workflow = make_workflow(
        ambiguity=5,
        tool_use=5,
        external_actions=5,
        business_risk=5,
        data_sensitivity=3,
    )

    assessment = assess_workflow(workflow)

    assert (
        assessment.recommendation
        == ArchitectureRecommendation.KEEP_HUMAN_REDESIGN_FIRST
    )
    assert assessment.risk_level == RiskLevel.HIGH
    assert assessment.human_approval_required is True


def test_extreme_data_sensitivity_with_external_actions_requires_redesign() -> None:
    workflow = make_workflow(
        ambiguity=5,
        tool_use=5,
        external_actions=3,
        business_risk=2,
        data_sensitivity=5,
    )

    assessment = assess_workflow(workflow)

    assert (
        assessment.recommendation
        == ArchitectureRecommendation.KEEP_HUMAN_REDESIGN_FIRST
    )
    assert assessment.risk_level == RiskLevel.HIGH
    assert assessment.human_approval_required is True


def test_tool_use_alone_does_not_make_a_workflow_agentic() -> None:
    workflow = make_workflow(
        repeatability=3,
        ambiguity=2,
        tool_use=5,
        external_actions=2,
        business_risk=2,
        data_sensitivity=2,
    )

    assessment = assess_workflow(workflow)

    assert (
        assessment.recommendation
        == ArchitectureRecommendation.LLM_ASSISTED_WORKFLOW
    )
    assert assessment.risk_level == RiskLevel.LOW


def test_agentic_recommendation_requires_bounded_risk() -> None:
    workflow = make_workflow(
        repeatability=3,
        ambiguity=5,
        tool_use=5,
        external_actions=3,
        business_risk=3,
        data_sensitivity=3,
    )

    assessment = assess_workflow(workflow)

    assert (
        assessment.recommendation
        == ArchitectureRecommendation.AGENTIC_WORKFLOW
    )
    assert assessment.risk_level == RiskLevel.MEDIUM
    assert assessment.human_approval_required is True