import pytest
from pydantic import ValidationError

from backend.app.models import WorkflowInput


def make_valid_workflow(**overrides):
    data = {
        "name": "Weekly Campaign Performance Review",
        "team": "Marketing Operations",
        "description": (
            "Collect campaign performance metrics, compare them with the "
            "previous reporting period, and prepare a weekly summary."
        ),
        "repeatability": 5,
        "ambiguity": 2,
        "tool_use": 3,
        "external_actions": 1,
        "business_risk": 2,
        "data_sensitivity": 2,
        "mandatory_human_approval": False,
    }

    data.update(overrides)

    return WorkflowInput(**data)


def test_valid_workflow_is_accepted():
    workflow = make_valid_workflow()

    assert workflow.name == "Weekly Campaign Performance Review"
    assert workflow.team == "Marketing Operations"
    assert workflow.repeatability == 5
    assert workflow.mandatory_human_approval is False


def test_scale_values_must_be_between_one_and_five():
    with pytest.raises(ValidationError):
        make_valid_workflow(repeatability=6)


def test_short_description_is_rejected():
    with pytest.raises(ValidationError):
        make_valid_workflow(description="Too short")


def test_unexpected_fields_are_rejected():
    with pytest.raises(ValidationError):
        make_valid_workflow(magic_ai_score=9000)


def test_string_whitespace_is_removed():
    workflow = make_valid_workflow(
        name="   Weekly Campaign Performance Review   ",
        team="   Marketing Operations   ",
    )

    assert workflow.name == "Weekly Campaign Performance Review"
    assert workflow.team == "Marketing Operations"