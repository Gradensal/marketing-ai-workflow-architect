from backend.app.models import WorkflowInput
from backend.app.services import (
    assess_workflow,
    generate_workflow_explanation,
)


def main() -> None:
    workflow = WorkflowInput(
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
    )

    assessment = assess_workflow(workflow)

    explanation = generate_workflow_explanation(
        workflow,
        assessment,
    )

    print()
    print("GSB-002 — AI EXPLANATION DEMO")
    print("=" * 72)

    print(
        f"Authoritative recommendation: "
        f"{assessment.recommendation.value}"
    )

    print(
        f"Risk level: "
        f"{assessment.risk_level.value}"
    )

    print()
    print("WHY THIS APPROACH")
    print(explanation.why_this_approach)

    print()
    print("WHY NOT MORE AUTONOMY")
    print(explanation.why_not_more_autonomy)

    print()
    print("PROPOSED ARCHITECTURE")
    print(explanation.proposed_architecture)

    print()
    print("HUMAN CHECKPOINT")
    print(explanation.human_checkpoint)

    print()
    print("FIRST EXPERIMENT")
    print(explanation.first_experiment)

    print()
    print("SUCCESS METRIC")
    print(explanation.success_metric)

    print()


if __name__ == "__main__":
    main()