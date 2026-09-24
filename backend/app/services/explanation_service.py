from openai import OpenAI

from backend.app.core.config import get_openai_model
from backend.app.models import (
    ArchitectureAssessment,
    WorkflowExplanation,
    WorkflowInput,
)


SYSTEM_INSTRUCTIONS = """
You are a business-facing AI systems architect.

Your job is to explain an architecture decision that has already been
made by a deterministic rules engine.

The deterministic ArchitectureAssessment is authoritative.

You MUST NOT:
- change the recommendation;
- contradict the risk level;
- remove a required human approval checkpoint;
- claim the prototype is production-ready;
- invent organization-specific policies;
- claim certainty that the rules engine does not provide.

Your job is to translate the existing decision into clear, useful
language for a marketing or business leader.

Prefer the least complex architecture that safely satisfies the
workflow requirements.

Be concrete, practical, concise, and technically accurate.
"""


def build_explanation_input(
    workflow: WorkflowInput,
    assessment: ArchitectureAssessment,
) -> str:
    """
    Build the business context supplied to the explanation model.
    """

    rationale = "\n".join(
        f"- {reason}"
        for reason in assessment.rationale
    )

    warnings = (
        "\n".join(
            f"- {warning}"
            for warning in assessment.warnings
        )
        if assessment.warnings
        else "- None"
    )

    return f"""
WORKFLOW

Name: {workflow.name}
Team: {workflow.team}

Description:
{workflow.description}

Workflow characteristics:
- Repeatability: {workflow.repeatability}/5
- Ambiguity: {workflow.ambiguity}/5
- Tool use: {workflow.tool_use}/5
- External actions: {workflow.external_actions}/5
- Business risk: {workflow.business_risk}/5
- Data sensitivity: {workflow.data_sensitivity}/5
- Mandatory human approval: {workflow.mandatory_human_approval}


AUTHORITATIVE ARCHITECTURE ASSESSMENT

Recommendation:
{assessment.recommendation.value}

Risk:
{assessment.risk_level.value}

Decision strength:
{assessment.decision_strength}/5

Human approval required:
{assessment.human_approval_required}

Human approval reason:
{assessment.human_approval_reason or "None"}

Rationale:
{rationale}

Warnings:
{warnings}


TASK

Explain this existing architecture assessment for a marketing leader.

Do not alter the recommendation.

The proposed architecture must remain consistent with the
authoritative assessment above.
""".strip()


def generate_workflow_explanation(
    workflow: WorkflowInput,
    assessment: ArchitectureAssessment,
    *,
    client: OpenAI | None = None,
    model: str | None = None,
) -> WorkflowExplanation:
    """
    Generate a structured stakeholder explanation for an existing
    deterministic architecture assessment.
    """

    api_client = client or OpenAI()

    selected_model = model or get_openai_model()

    response = api_client.responses.parse(
        model=selected_model,
        reasoning={
            "effort": "low",
        },
        instructions=SYSTEM_INSTRUCTIONS,
        input=build_explanation_input(
            workflow,
            assessment,
        ),
        text_format=WorkflowExplanation,
    )

    if response.output_parsed is None:
        raise RuntimeError(
            "OpenAI returned no parsed workflow explanation."
        )

    return response.output_parsed