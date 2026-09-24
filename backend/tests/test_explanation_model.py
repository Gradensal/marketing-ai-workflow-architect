import pytest
from pydantic import ValidationError

from backend.app.models import WorkflowExplanation


def make_explanation(**overrides):
    data = {
        "why_this_approach": (
            "The workflow is predictable enough that explicit "
            "automation provides a simpler and more reliable design."
        ),
        "why_not_more_autonomy": (
            "Greater autonomy would add complexity without providing "
            "meaningful value for this highly repeatable workflow."
        ),
        "proposed_architecture": (
            "Use a scheduled workflow that retrieves the required data, "
            "applies explicit transformation rules, and produces the report."
        ),
        "human_checkpoint": (
            "A marketer should review exceptions rather than every run."
        ),
        "first_experiment": (
            "Automate one weekly reporting workflow and compare the result "
            "with the current manual process for four reporting cycles."
        ),
        "success_metric": (
            "Reduce manual preparation time while preserving reporting accuracy."
        ),
    }

    data.update(overrides)

    return WorkflowExplanation(**data)


def test_valid_explanation_is_accepted():
    explanation = make_explanation()

    assert "predictable" in explanation.why_this_approach


def test_short_explanation_is_rejected():
    with pytest.raises(ValidationError):
        make_explanation(
            why_this_approach="Too short"
        )


def test_unexpected_fields_are_rejected():
    with pytest.raises(ValidationError):
        make_explanation(
            model_changed_the_decision=True
        )