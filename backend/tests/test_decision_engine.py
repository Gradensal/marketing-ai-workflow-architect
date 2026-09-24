from backend.app.models import (
    ArchitectureRecommendation,
    RiskLevel,
    WorkflowInput,
)
from backend.app.services import assess_workflow


def make_workflow(**overrides) -> WorkflowInput:
    data = {
        "name": "Example Marketing Workflow",
        "team": "Marketing Operations",
        "description": (
            "A representative marketing workflow used to test "
            "architecture recommendations in the decision engine."
        ),
        "repeatability": 3,
        "ambiguity": 3,
        "tool_use": 2,
        "external_actions": 2,
        "business_risk": 2,
        "data_sensitivity": 2,
        "mandatory_human_approval": False,
    }

    data.update(overrides)

    return WorkflowInput(**data)


def test_predictable_reporting_uses_deterministic_automation():
    workflow = make_workflow(
        name="Weekly Campaign Reporting",
        description=(
            "Collect the same campaign metrics every Monday, calculate "
            "standardized KPIs, and generate the same reporting package."
        ),
        repeatability=5,
        ambiguity=1,
        tool_use=3,
        external_actions=1,
        business_risk=2,
        data_sensitivity=2,
    )

    assessment = assess_workflow(workflow)

    assert (
        assessment.recommendation
        == ArchitectureRecommendation.DETERMINISTIC_AUTOMATION
    )
    assert assessment.risk_level == RiskLevel.LOW
    assert assessment.decision_strength == 5
    assert assessment.human_approval_required is False


def test_message_drafting_uses_llm_assistance():
    workflow = make_workflow(
        name="Campaign Message Drafting",
        description=(
            "Use campaign context and audience information to create "
            "first-draft marketing message variations for human review."
        ),
        repeatability=3,
        ambiguity=4,
        tool_use=2,
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
    assert assessment.human_approval_required is False


def test_anomaly_investigation_can_use_agentic_workflow():
    workflow = make_workflow(
        name="Campaign Anomaly Investigation",
        description=(
            "Investigate unexpected campaign performance by collecting "
            "context from several systems, comparing evidence, and "
            "preparing recommended actions for review."
        ),
        repeatability=2,
        ambiguity=5,
        tool_use=5,
        external_actions=3,
        business_risk=3,
        data_sensitivity=2,
    )

    assessment = assess_workflow(workflow)

    assert (
        assessment.recommendation
        == ArchitectureRecommendation.AGENTIC_WORKFLOW
    )
    assert assessment.risk_level == RiskLevel.MEDIUM
    assert assessment.human_approval_required is True
    assert assessment.human_approval_reason is not None


def test_autonomous_high_risk_pricing_stays_human_first():
    workflow = make_workflow(
        name="Autonomous Customer Pricing",
        description=(
            "Analyze customer information and independently change "
            "customer-facing prices without requiring approval."
        ),
        repeatability=3,
        ambiguity=5,
        tool_use=4,
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
    assert assessment.decision_strength == 5


def test_many_tools_do_not_automatically_require_an_agent():
    workflow = make_workflow(
        name="Multi-Platform Reporting",
        description=(
            "Retrieve standardized metrics from five reporting systems "
            "and combine them using the same rules every week."
        ),
        repeatability=5,
        ambiguity=1,
        tool_use=5,
        external_actions=1,
        business_risk=1,
        data_sensitivity=2,
    )

    assessment = assess_workflow(workflow)

    assert (
        assessment.recommendation
        == ArchitectureRecommendation.DETERMINISTIC_AUTOMATION
    )


def test_mandatory_human_approval_is_preserved():
    workflow = make_workflow(
        name="Executive Campaign Brief",
        description=(
            "Create a campaign recommendation that company policy "
            "requires a marketing leader to approve before use."
        ),
        repeatability=3,
        ambiguity=3,
        tool_use=2,
        external_actions=2,
        business_risk=2,
        data_sensitivity=2,
        mandatory_human_approval=True,
    )

    assessment = assess_workflow(workflow)

    assert assessment.human_approval_required is True
    assert "policy" in assessment.human_approval_reason.lower()


def test_highly_sensitive_active_workflow_stays_human_first():
    workflow = make_workflow(
        name="Sensitive Customer Outreach",
        description=(
            "Use highly sensitive customer data to determine and execute "
            "individualized outbound actions across customer systems."
        ),
        repeatability=2,
        ambiguity=4,
        tool_use=4,
        external_actions=3,
        business_risk=3,
        data_sensitivity=5,
    )

    assessment = assess_workflow(workflow)

    assert (
        assessment.recommendation
        == ArchitectureRecommendation.KEEP_HUMAN_REDESIGN_FIRST
    )
    assert assessment.risk_level == RiskLevel.HIGH