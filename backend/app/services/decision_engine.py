from backend.app.models import (
    ArchitectureAssessment,
    ArchitectureRecommendation,
    RiskLevel,
    WorkflowInput,
)


def assess_workflow(workflow: WorkflowInput) -> ArchitectureAssessment:
    """
    Evaluate a workflow using explicit architecture rules.

    The function deliberately separates deterministic architecture
    selection from any future LLM explanation layer.
    """

    risk_level = _determine_risk_level(workflow)

    human_approval_required = _requires_human_approval(workflow)

    human_approval_reason = (
        _build_human_approval_reason(workflow)
        if human_approval_required
        else None
    )

    if _requires_human_first_design(workflow):
        return ArchitectureAssessment(
            recommendation=(
                ArchitectureRecommendation.KEEP_HUMAN_REDESIGN_FIRST
            ),
            risk_level=risk_level,
            decision_strength=_human_first_strength(workflow),
            human_approval_required=True,
            human_approval_reason=(
                human_approval_reason
                or "The workflow has consequential risk characteristics."
            ),
            rationale=[
                "The workflow combines elevated risk with consequential actions.",
                (
                    "Autonomous execution would create more risk than this "
                    "prototype considers acceptable."
                ),
                (
                    "The workflow should be redesigned around explicit human "
                    "control before additional autonomy is considered."
                ),
            ],
            warnings=[
                (
                    "This prototype does not replace security, privacy, legal, "
                    "compliance, or organization-specific risk review."
                ),
            ],
        )

    if _fits_deterministic_automation(workflow):
        return ArchitectureAssessment(
            recommendation=(
                ArchitectureRecommendation.DETERMINISTIC_AUTOMATION
            ),
            risk_level=risk_level,
            decision_strength=_deterministic_strength(workflow),
            human_approval_required=human_approval_required,
            human_approval_reason=human_approval_reason,
            rationale=[
                "The workflow is highly repeatable.",
                "The workflow requires relatively little interpretation.",
                (
                    "Its external actions and business risk are limited enough "
                    "that explicit software rules are preferable to unnecessary "
                    "AI autonomy."
                ),
            ],
            warnings=[],
        )

    if _fits_agentic_workflow(workflow):
        warnings = [
            (
                "Agentic execution should include observability, bounded tool "
                "permissions, failure handling, and evaluation before "
                "production use."
            )
        ]

        if human_approval_required:
            warnings.append(
                (
                    "Consequential actions should remain behind an explicit "
                    "human approval checkpoint."
                )
            )

        return ArchitectureAssessment(
            recommendation=(
                ArchitectureRecommendation.AGENTIC_WORKFLOW
            ),
            risk_level=risk_level,
            decision_strength=_agentic_strength(workflow),
            human_approval_required=human_approval_required,
            human_approval_reason=human_approval_reason,
            rationale=[
                (
                    "The workflow requires substantial interpretation "
                    "rather than only fixed rules."
                ),
                (
                    "It depends on several tools or information sources."
                ),
                (
                    "It performs meaningful actions that may require the "
                    "system to adapt based on intermediate results."
                ),
            ],
            warnings=warnings,
        )

    return ArchitectureAssessment(
        recommendation=(
            ArchitectureRecommendation.LLM_ASSISTED_WORKFLOW
        ),
        risk_level=risk_level,
        decision_strength=_llm_assisted_strength(workflow),
        human_approval_required=human_approval_required,
        human_approval_reason=human_approval_reason,
        rationale=[
            (
                "The workflow benefits from interpretation or generation, "
                "but does not strongly justify autonomous agent behaviour."
            ),
            (
                "An LLM can assist a human while keeping the workflow "
                "structure and final authority explicit."
            ),
        ],
        warnings=[
            (
                "LLM-generated content should be reviewed when accuracy, "
                "brand impact, customer communication, or business decisions "
                "are involved."
            )
        ],
    )


def _determine_risk_level(workflow: WorkflowInput) -> RiskLevel:
    highest_risk_signal = max(
        workflow.business_risk,
        workflow.data_sensitivity,
    )

    if highest_risk_signal >= 4:
        return RiskLevel.HIGH

    if highest_risk_signal == 3:
        return RiskLevel.MEDIUM

    return RiskLevel.LOW


def _requires_human_approval(workflow: WorkflowInput) -> bool:
    return any(
        [
            workflow.mandatory_human_approval,
            workflow.business_risk >= 3,
            workflow.external_actions >= 4,
            workflow.data_sensitivity >= 4,
        ]
    )


def _build_human_approval_reason(
    workflow: WorkflowInput,
) -> str:
    reasons: list[str] = []

    if workflow.mandatory_human_approval:
        reasons.append(
            "Organizational policy already requires human approval."
        )

    if workflow.business_risk >= 3:
        reasons.append(
            "The workflow has meaningful business risk."
        )

    if workflow.external_actions >= 4:
        reasons.append(
            "The workflow performs consequential external actions."
        )

    if workflow.data_sensitivity >= 4:
        reasons.append(
            "The workflow handles sensitive information."
        )

    return " ".join(reasons)


def _requires_human_first_design(
    workflow: WorkflowInput,
) -> bool:
    high_risk_external_action = (
        workflow.business_risk >= 4
        and workflow.external_actions >= 4
    )

    highly_sensitive_active_workflow = (
        workflow.data_sensitivity >= 5
        and workflow.external_actions >= 3
    )

    return (
        high_risk_external_action
        or highly_sensitive_active_workflow
    )


def _fits_deterministic_automation(
    workflow: WorkflowInput,
) -> bool:
    return (
        workflow.repeatability >= 4
        and workflow.ambiguity <= 2
        and workflow.external_actions <= 2
        and workflow.business_risk <= 2
        and workflow.data_sensitivity <= 3
    )


def _fits_agentic_workflow(
    workflow: WorkflowInput,
) -> bool:
    return (
        workflow.ambiguity >= 4
        and workflow.tool_use >= 4
        and workflow.external_actions >= 3
        and workflow.business_risk <= 3
        and workflow.data_sensitivity <= 3
    )


def _human_first_strength(
    workflow: WorkflowInput,
) -> int:
    if (
        workflow.business_risk == 5
        or workflow.data_sensitivity == 5
    ):
        return 5

    return 4


def _deterministic_strength(
    workflow: WorkflowInput,
) -> int:
    if (
        workflow.repeatability == 5
        and workflow.ambiguity == 1
        and workflow.external_actions == 1
    ):
        return 5

    return 4


def _agentic_strength(
    workflow: WorkflowInput,
) -> int:
    if (
        workflow.ambiguity >= 4
        and workflow.tool_use >= 4
        and workflow.external_actions >= 4
        and workflow.business_risk <= 2
    ):
        return 5

    return 4


def _llm_assisted_strength(
    workflow: WorkflowInput,
) -> int:
    if workflow.ambiguity >= 3:
        return 4

    return 3