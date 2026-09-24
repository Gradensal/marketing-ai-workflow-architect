import pytest
from pydantic import ValidationError

from backend.app.models import (
    ArchitectureAssessment,
    ArchitectureRecommendation,
    RiskLevel,
)


def make_valid_assessment(**overrides):
    data = {
        "recommendation": (
            ArchitectureRecommendation.DETERMINISTIC_AUTOMATION
        ),
        "risk_level": RiskLevel.LOW,
        "decision_strength": 5,
        "human_approval_required": False,
        "human_approval_reason": None,
        "rationale": [
            "The workflow is highly repeatable.",
            "The workflow requires little interpretation.",
        ],
        "warnings": [],
    }

    data.update(overrides)

    return ArchitectureAssessment(**data)


def test_valid_assessment_is_accepted():
    assessment = make_valid_assessment()

    assert (
        assessment.recommendation
        == ArchitectureRecommendation.DETERMINISTIC_AUTOMATION
    )
    assert assessment.risk_level == RiskLevel.LOW
    assert assessment.decision_strength == 5


def test_decision_strength_must_be_between_one_and_five():
    with pytest.raises(ValidationError):
        make_valid_assessment(decision_strength=6)


def test_invalid_recommendation_is_rejected():
    with pytest.raises(ValidationError):
        make_valid_assessment(
            recommendation="magic_super_agent"
        )


def test_human_approval_requires_a_reason():
    with pytest.raises(ValidationError):
        make_valid_assessment(
            human_approval_required=True,
            human_approval_reason=None,
        )


def test_human_approval_with_reason_is_accepted():
    assessment = make_valid_assessment(
        human_approval_required=True,
        human_approval_reason=(
            "The workflow performs consequential external actions."
        ),
    )

    assert assessment.human_approval_required is True
    assert assessment.human_approval_reason is not None


def test_unexpected_fields_are_rejected():
    with pytest.raises(ValidationError):
        make_valid_assessment(
            secret_agent_score=999
        )