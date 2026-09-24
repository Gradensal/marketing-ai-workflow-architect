from backend.app.models import WorkflowInput
from backend.app.services import assess_workflow


def build_demo_workflows() -> list[WorkflowInput]:
    return [
        WorkflowInput(
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
        ),
        WorkflowInput(
            name="Campaign Message Drafting",
            team="Product Marketing",
            description=(
                "Use campaign context and audience information to create "
                "first-draft marketing message variations that a marketer "
                "reviews before publication."
            ),
            repeatability=3,
            ambiguity=4,
            tool_use=2,
            external_actions=2,
            business_risk=2,
            data_sensitivity=2,
            mandatory_human_approval=False,
        ),
        WorkflowInput(
            name="Campaign Anomaly Investigation",
            team="Digital Acquisition",
            description=(
                "Investigate unexpected campaign performance by collecting "
                "context from several systems, comparing evidence, and "
                "preparing recommended actions."
            ),
            repeatability=2,
            ambiguity=5,
            tool_use=5,
            external_actions=3,
            business_risk=3,
            data_sensitivity=2,
            mandatory_human_approval=False,
        ),
        WorkflowInput(
            name="Autonomous Customer Pricing",
            team="Growth",
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
            mandatory_human_approval=False,
        ),
    ]


def format_label(value: str) -> str:
    return value.replace("_", " ").upper()


def print_assessment(workflow: WorkflowInput) -> None:
    assessment = assess_workflow(workflow)

    print("=" * 72)
    print(workflow.name.upper())
    print("=" * 72)

    print(
        f"Recommendation : "
        f"{format_label(assessment.recommendation.value)}"
    )

    print(
        f"Risk level     : "
        f"{assessment.risk_level.value.upper()}"
    )

    print(
        f"Decision strength: "
        f"{assessment.decision_strength}/5"
    )

    print(
        "Human approval : "
        f"{'YES' if assessment.human_approval_required else 'NO'}"
    )

    if assessment.human_approval_reason:
        print(
            f"Approval reason: "
            f"{assessment.human_approval_reason}"
        )

    print("\nWhy:")

    for reason in assessment.rationale:
        print(f"  - {reason}")

    if assessment.warnings:
        print("\nWarnings:")

        for warning in assessment.warnings:
            print(f"  - {warning}")

    print()


def main() -> None:
    print()
    print("GSB-002 — MARKETING AI WORKFLOW ARCHITECT")
    print("Deterministic Architecture Decision Demo")
    print()

    for workflow in build_demo_workflows():
        print_assessment(workflow)


if __name__ == "__main__":
    main()