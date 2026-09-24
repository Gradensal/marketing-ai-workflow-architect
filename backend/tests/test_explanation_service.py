from types import SimpleNamespace

import pytest

from backend.app.models import (
    ArchitectureRecommendation,
    RiskLevel,
    WorkflowExplanation,
    WorkflowInput,
)
from backend.app.services import assess_workflow
from backend.app.services.explanation_service import (
    build_explanation_input,
    generate_workflow_explanation,
)


class FakeResponses:
    def __init__(
        self,
        parsed: WorkflowExplanation | None,
    ):
        self.parsed = parsed
        self.last_request = None

    def parse(self, **kwargs):
        self.last_request = kwargs

        return SimpleNamespace(
            output_parsed=self.parsed
        )


class FakeOpenAIClient:
    def __init__(
        self,
        parsed: WorkflowExplanation | None,
    ):
        self.responses = FakeResponses(parsed)


def make_workflow() -> WorkflowInput:
    return WorkflowInput(
        name="Weekly Campaign Reporting",
        team="Marketing Operations",
        description=(
            "Collect the same campaign metrics every Monday, "
            "calculate standardized KPIs, and generate the same "
            "reporting package."
        ),
        repeatability=5,
        ambiguity=1,
        tool_use=3,
        external_actions=1,
        business_risk=2,
        data_sensitivity=2,
        mandatory_human_approval=False,
    )


def make_explanation() -> WorkflowExplanation:
    return WorkflowExplanation(
        why_this_approach=(
            "The workflow is highly predictable, so explicit "
            "automation provides a simpler and more reliable solution."
        ),
        why_not_more_autonomy=(
            "Agentic autonomy would add complexity without meaningful "
            "benefit for a workflow governed by stable rules."
        ),
        proposed_architecture=(
            "Use a scheduled deterministic workflow that collects "
            "campaign data, calculates KPIs, and produces the report."
        ),
        human_checkpoint=(
            "A marketer reviews exceptions rather than every routine run."
        ),
        first_experiment=(
            "Automate one reporting cycle and compare the output against "
            "the existing manually prepared report."
        ),
        success_metric=(
            "Reduce preparation time without reducing reporting accuracy."
        ),
    )


def test_prompt_contains_authoritative_assessment():
    workflow = make_workflow()
    assessment = assess_workflow(workflow)

    prompt = build_explanation_input(
        workflow,
        assessment,
    )

    assert (
        ArchitectureRecommendation.DETERMINISTIC_AUTOMATION.value
        in prompt
    )

    assert RiskLevel.LOW.value in prompt


def test_generate_explanation_returns_structured_model():
    workflow = make_workflow()
    assessment = assess_workflow(workflow)

    fake_client = FakeOpenAIClient(
        make_explanation()
    )

    result = generate_workflow_explanation(
        workflow,
        assessment,
        client=fake_client,
        model="test-model",
    )

    assert isinstance(
        result,
        WorkflowExplanation,
    )

    assert (
        "predictable"
        in result.why_this_approach.lower()
    )


def test_service_passes_structured_output_model():
    workflow = make_workflow()
    assessment = assess_workflow(workflow)

    fake_client = FakeOpenAIClient(
        make_explanation()
    )

    generate_workflow_explanation(
        workflow,
        assessment,
        client=fake_client,
        model="test-model",
    )

    request = fake_client.responses.last_request

    assert request["model"] == "test-model"

    assert (
        request["text_format"]
        is WorkflowExplanation
    )


def test_service_raises_when_no_parsed_result_is_returned():
    workflow = make_workflow()
    assessment = assess_workflow(workflow)

    fake_client = FakeOpenAIClient(None)

    with pytest.raises(
        RuntimeError,
        match="no parsed workflow explanation",
    ):
        generate_workflow_explanation(
            workflow,
            assessment,
            client=fake_client,
            model="test-model",
        )