# GSB-002 Build Ledger

## Project

Marketing AI Workflow Architect

## Started

2026-09-24

---

## Environment Baseline

### Machine

Mac Studio

### Local Project Root

`/Users/lissettegorrin/Desktop/_Gradensal/Signature_Builds/marketing-ai-workflow-architect`

### Runtime Versions

- Python: 3.12.6
- Git: 2.50.1 (Apple Git-155)
- Node.js: 23.1.0
- npm: 10.9.0
- Java: 22.0.1

### Git

- Author: Lissette Gorrin Rodriguez
- Default project branch: `main`
- Repository owner planned: Gradensal
- Remote: not created yet

### Baseline Python Dependencies

- FastAPI: 0.141.1
- Uvicorn: 0.53.0
- HTTPX: 0.28.1
- python-dotenv: 1.2.3
- pytest: 9.1.1
- Pydantic: 2.13.5

---

# Build Progress

## Milestone 0 - Environment Audit

Status: Complete

Verified the development environment and compared it with the previous
Gradensal Signature Build.

## Milestone 1 - Project Foundation

Status: Complete

### Decisions

- Keep Python 3.12.6 for consistency with GSB-001.
- Use a project-local `.venv`.
- Use `main` explicitly because no global Git default branch is configured.
- Keep backend and frontend separated.
- Delay OpenAI integration until deterministic logic is implemented and tested.
- Do not create the GitHub remote until the local foundation has passed its
  first checkpoint.

---

# Bugs & Lessons

None yet.

## Milestone 2 - Workflow Domain Model

Status: Complete

### Domain Decision

A workflow will initially be represented using seven architecture-relevant
signals:

- repeatability;
- ambiguity;
- tool use;
- external actions;
- business risk;
- data sensitivity;
- mandatory human approval.

Each scored signal uses a 1–5 scale.

### Engineering Decision

Pydantic validates the workflow before it reaches the architecture engine.

Unexpected fields are rejected rather than silently ignored.

### Key Insight

Before deciding whether a workflow needs AI, the business process must first be
translated into explicit, inspectable characteristics.

### Architecture Assessment Output Model

The decision engine will return a typed `ArchitectureAssessment`
rather than an unstructured dictionary.

The assessment contains:

- architecture recommendation;
- risk level;
- decision strength;
- human approval requirement;
- human approval reason;
- rationale;
- warnings.

### Vocabulary Decision

Architecture recommendations use an explicit enum:

- deterministic automation;
- LLM-assisted workflow;
- agentic workflow;
- keep human / redesign first.

Risk levels use:

- low;
- medium;
- high.

### Important Semantic Decision

`decision_strength` describes how strongly the deterministic rule
conditions support a recommendation.

It is deliberately not described as statistical or AI confidence.

### Validation Rule

When human approval is required, an explicit approval reason must
also be present.

## Milestone 3 - Deterministic Architecture Decision Engine

Status: Complete

### Core Design

Architecture selection occurs before the LLM explanation layer.

The initial recommendation is produced by explicit software rules rather
than by asking a language model to choose an architecture.

### Decision Priority

The first version evaluates architecture in this order:

1. high-risk workflows requiring human-first design;
2. highly predictable workflows suited to deterministic automation;
3. ambiguous, multi-tool workflows suited to agentic execution;
4. remaining interpretive workflows suited to LLM assistance.

### Important Insight

Tool count alone does not justify an agent.

A workflow can interact with many systems while remaining deterministic
if its sequence and decision rules are predictable.

Agentic architecture becomes more appropriate when ambiguity, dynamic
tool use, and meaningful actions occur together.

### Safety Principle

A workflow may technically satisfy characteristics associated with an
agent while still being inappropriate for autonomous execution because
business risk or data sensitivity takes priority.

## Milestone 4 - Decision Engine Demonstration

Status: Complete

### Demonstration

Created a developer-facing demonstration that runs four representative
marketing workflows through the deterministic architecture engine.

### Demonstrated Outcomes

1. Weekly Campaign Reporting
   → Deterministic Automation

2. Campaign Message Drafting
   → LLM-Assisted Workflow

3. Campaign Anomaly Investigation
   → Agentic Workflow

4. Autonomous Customer Pricing
   → Keep Human / Redesign First

### Evidence

`assets/screenshots/02-four-architecture-decisions.png`

### Key Insight

The same software system can recommend different levels of automation
because architecture selection is based on workflow characteristics rather
than an assumption that every workflow benefits from greater AI autonomy.