from fastapi.testclient import TestClient

from backend.app.api.analysis import (
    get_explanation_generator,
)

from backend.app.main import app

from backend.app.models import (
    WorkflowExplanation,
)


client = TestClient(app)


WORKFLOW_PAYLOAD = {
    "name": "Campaign Message Drafting",
    "team": "Product Marketing",
    "description": (
        "Use campaign context and audience information "
        "to create first-draft marketing message "
        "variations that a marketer reviews before "
        "publication."
    ),
    "repeatability": 3,
    "ambiguity": 4,
    "tool_use": 2,
    "external_actions": 2,
    "business_risk": 2,
    "data_sensitivity": 2,
    "mandatory_human_approval": False,
}


def successful_explanation_generator(
    workflow,
    assessment,
):
    return WorkflowExplanation(
        why_this_approach=(
            "The workflow benefits from generative assistance "
            "while keeping final authority with the marketer."
        ),
        why_not_more_autonomy=(
            "The workflow does not require autonomous actions "
            "or independent control of external systems."
        ),
        proposed_architecture=(
            "Use an LLM-assisted drafting step inside an "
            "explicit marketer-controlled workflow."
        ),
        human_checkpoint=(
            "A marketer reviews the generated campaign "
            "content before publication."
        ),
        first_experiment=(
            "Test the workflow with a small collection of "
            "campaign briefs and compare draft quality."
        ),
        success_metric=(
            "Measure how many drafts are usable with only "
            "light human editing."
        ),
    )


def failing_explanation_generator(
    workflow,
    assessment,
):
    raise RuntimeError(
        "Simulated AI provider outage."
    )


def test_analysis_reports_available_explanation() -> None:
    app.dependency_overrides[
        get_explanation_generator
    ] = lambda: successful_explanation_generator

    try:
        response = client.post(
            "/api/v1/analyze",
            json=WORKFLOW_PAYLOAD,
        )
    finally:
        app.dependency_overrides.clear()


    assert response.status_code == 200

    body = response.json()

    assert (
        body["assessment"]["recommendation"]
        == "llm_assisted_workflow"
    )

    assert (
        body["explanation_status"]
        == "available"
    )

    assert body["explanation"] is not None

    assert (
        body["explanation_message"]
        is None
    )


def test_ai_failure_preserves_deterministic_assessment() -> None:
    app.dependency_overrides[
        get_explanation_generator
    ] = lambda: failing_explanation_generator

    try:
        response = client.post(
            "/api/v1/analyze",
            json=WORKFLOW_PAYLOAD,
        )
    finally:
        app.dependency_overrides.clear()


    assert response.status_code == 200

    body = response.json()


    assert (
        body["assessment"]["recommendation"]
        == "llm_assisted_workflow"
    )

    assert (
        body["assessment"]["risk_level"]
        == "low"
    )

    assert (
        body["assessment"]["decision_strength"]
        == 4
    )


    assert body["explanation"] is None

    assert (
        body["explanation_status"]
        == "unavailable"
    )

    assert (
        "assessment completed successfully"
        in body["explanation_message"].lower()
    )

    assert (
        "recommendation remains valid"
        in body["explanation_message"].lower()
    )