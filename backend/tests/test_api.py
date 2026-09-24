from fastapi.testclient import TestClient

from backend.app.main import app


client = TestClient(app)


def make_payload(**overrides) -> dict:
    payload = {
        "name": "Weekly Campaign Reporting",
        "team": "Marketing Operations",
        "description": (
            "Collect the same campaign metrics every Monday, "
            "calculate standardized KPIs, and generate the same "
            "reporting package."
        ),
        "repeatability": 5,
        "ambiguity": 1,
        "tool_use": 3,
        "external_actions": 1,
        "business_risk": 2,
        "data_sensitivity": 2,
        "mandatory_human_approval": False,
    }

    payload.update(overrides)

    return payload


def test_health_endpoint():
    response = client.get("/health")

    assert response.status_code == 200

    assert response.json() == {
        "status": "ok",
        "service": "marketing-ai-workflow-architect",
        "version": "0.1.0",
    }


def test_assess_endpoint_returns_deterministic_recommendation():
    response = client.post(
        "/api/v1/assess",
        json=make_payload(),
    )

    assert response.status_code == 200

    data = response.json()

    assert (
        data["recommendation"]
        == "deterministic_automation"
    )
    assert data["risk_level"] == "low"
    assert data["decision_strength"] == 5
    assert data["human_approval_required"] is False


def test_assess_endpoint_returns_human_first_for_high_risk_workflow():
    response = client.post(
        "/api/v1/assess",
        json=make_payload(
            name="Autonomous Customer Pricing",
            description=(
                "Analyze customer information and independently "
                "change customer-facing prices without approval."
            ),
            repeatability=3,
            ambiguity=5,
            tool_use=4,
            external_actions=5,
            business_risk=5,
            data_sensitivity=3,
        ),
    )

    assert response.status_code == 200

    data = response.json()

    assert (
        data["recommendation"]
        == "keep_human_redesign_first"
    )
    assert data["risk_level"] == "high"
    assert data["human_approval_required"] is True
    assert data["human_approval_reason"] is not None


def test_assess_endpoint_rejects_invalid_scale_value():
    response = client.post(
        "/api/v1/assess",
        json=make_payload(
            repeatability=6,
        ),
    )

    assert response.status_code == 422


def test_assess_endpoint_rejects_unexpected_fields():
    payload = make_payload()

    payload["magic_ai_score"] = 999

    response = client.post(
        "/api/v1/assess",
        json=payload,
    )

    assert response.status_code == 422