from fastapi.testclient import TestClient

from backend.app.api.analysis import (
    get_explanation_generator,
)
from backend.app.main import app
from backend.app.models import (
    ArchitectureAssessment,
    WorkflowExplanation,
    WorkflowInput,
)


client = TestClient(app)


def fake_explanation_generator(
    workflow: WorkflowInput,
    assessment: ArchitectureAssessment,
) -> WorkflowExplanation:
    return WorkflowExplanation(
        why_this_approach=(
            "The workflow benefits from language-model assistance "
            "while retaining a bounded process."
        ),
        why_not_more_autonomy=(
            "The workflow does not require autonomous tool selection "
            "or independent consequential actions."
        ),
        proposed_architecture=(
            "Use an LLM-assisted drafting workflow with structured "
            "inputs and explicit human review."
        ),
        human_checkpoint=(
            "A marketer reviews the resulting draft before publication."
        ),
        first_experiment=(
            "Run the workflow against a small sample of campaign briefs "
            "and compare results with the existing process."
        ),
        success_metric=(
            "Measure usable-draft rate and editing effort."
        ),
    )


def make_payload(**overrides) -> dict:
    payload = {
        "name": "Campaign Message Drafting",
        "team": "Product Marketing",
        "description": (
            "Use campaign context and audience information to create "
            "first-draft marketing message variations for human review."
        ),
        "repeatability": 3,
        "ambiguity": 4,
        "tool_use": 2,
        "external_actions": 2,
        "business_risk": 2,
        "data_sensitivity": 2,
        "mandatory_human_approval": False,
    }

    payload.update(overrides)

    return payload


def setup_function():
    app.dependency_overrides[
        get_explanation_generator
    ] = lambda: fake_explanation_generator


def teardown_function():
    app.dependency_overrides.clear()


def test_analyze_returns_assessment_and_explanation():
    response = client.post(
        "/api/v1/analyze",
        json=make_payload(),
    )

    assert response.status_code == 200

    data = response.json()

    assert (
        data["assessment"]["recommendation"]
        == "llm_assisted_workflow"
    )

    assert data["assessment"]["risk_level"] == "low"

    assert (
        "why_this_approach"
        in data["explanation"]
    )

    assert (
        "human_checkpoint"
        in data["explanation"]
    )


def test_analyze_preserves_deterministic_decision():
    response = client.post(
        "/api/v1/analyze",
        json=make_payload(
            name="Weekly Campaign Reporting",
            description=(
                "Collect the same campaign metrics every Monday, "
                "calculate standardized KPIs, and create the same report."
            ),
            repeatability=5,
            ambiguity=1,
            tool_use=5,
            external_actions=1,
            business_risk=1,
        ),
    )

    assert response.status_code == 200

    data = response.json()

    assert (
        data["assessment"]["recommendation"]
        == "deterministic_automation"
    )


def test_analyze_rejects_invalid_workflow_before_ai_call():
    response = client.post(
        "/api/v1/analyze",
        json=make_payload(
            ambiguity=99,
        ),
    )

    assert response.status_code == 422