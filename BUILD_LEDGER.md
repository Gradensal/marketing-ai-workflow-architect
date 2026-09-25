# GSB-002 — BUILD LEDGER

## Marketing AI Workflow Architect

**Organization:** Gradensal  
**Series:** Gradensal Signature Builds  
**Build ID:** GSB-002  
**Author:** Lissette Gorrin Rodriguez  
**Started:** September 24, 2026  
**Current phase:** Documentation and release preparation  

---

# 1. Build Purpose

GSB-002 — Marketing AI Workflow Architect is a decision-support prototype for determining the appropriate level of automation or AI autonomy for a business workflow.

The system can recommend:

1. deterministic automation;
2. LLM-assisted workflow;
3. agentic workflow;
4. keep human / redesign first.

The central engineering principle is:

> **The deterministic engine owns the architecture decision. The LLM explains the decision.**

The project was intentionally designed to demonstrate controlled AI integration rather than simply placing an LLM behind a user interface.

---

# 2. Original Problem

Organizations frequently begin AI initiatives with the question:

> Where can we add AI?

GSB-002 reframes the problem:

> **What level of automation or AI autonomy does this workflow actually require?**

The prototype evaluates workflow characteristics before recommending an architecture.

This allows the system to distinguish between:

```text
ordinary software
LLM assistance
bounded agentic behavior
human-first redesign
```

instead of assuming that more autonomy is always better.

---

# 3. Target Portfolio Context

GSB-002 was created as a Gradensal Signature Build demonstrating skills relevant to AI-enabled marketing technology, workflow architecture, AI governance, software engineering, and technical storytelling.

The build is an independent portfolio prototype.

It is not a reproduction of any employer's internal system, and it does not claim to demonstrate complete qualification for any specific role.

---

# 4. Core Build Method

The project followed the Gradensal Lab / Signature Build workflow:

```text
BUILD
  ↓
LEARN
  ↓
SHOW
```

Each milestone was developed through:

1. concept explanation;
2. implementation;
3. automated or manual verification;
4. documentation;
5. visual evidence;
6. Git checkpoint.

The project was not advanced to the next major stage until the current stage had been verified.

---

# 5. Development Environment

## Machine

```text
Platform      macOS
Primary host  Mac Studio
```

---

## Python

```text
Python        3.12.6
Virtual env   .venv
```

Verified interpreter:

```text
/Users/lissettegorrin/Desktop/_Gradensal/Signature_Builds/
marketing-ai-workflow-architect/.venv/bin/python3
```

---

## Backend Tooling

```text
FastAPI             0.141.1
Uvicorn             0.53.0
python-dotenv        1.2.3
OpenAI Python SDK   3.19.2
pytest              9.1.1
httpx2              2.13.1
Pydantic            2.13.5
```

---

## Frontend Tooling

```text
Node.js             23.1.0
npm                 10.9.0
React               19.3.0
React DOM           19.3.0
Vite                8.3.1
@vitejs/plugin-react 6.1.1
TypeScript
```

---

# 6. Environment Notes

## Conda interference

During backend testing, the shell temporarily contained both:

```text
(.venv)
(base)
```

This caused an earlier pytest command to execute through the wrong Python environment.

The correct project configuration is:

```text
(.venv)
```

without Conda base active.

Verified environment:

```text
Python 3.12.6
pytest 9.1.1
```

Conda automatic base activation was disabled with:

```bash
conda config --set auto_activate_base false
```

---

## Recommended terminal separation

The project uses two named terminal contexts.

### Backend Terminal

Working directory:

```text
marketing-ai-workflow-architect/
```

Typical commands:

```bash
python3 -m pytest backend/tests -q
python3 -m scripts.run_decision_demo
python3 -m uvicorn backend.app.main:app --reload
```

Python virtual environment:

```text
.venv
```

---

### Frontend Terminal

Working directory:

```text
marketing-ai-workflow-architect/frontend/
```

Typical commands:

```bash
npm run dev
npm run build
```

The Python virtual environment is not required for frontend work.

---

# 7. Node 23 npm Experimental Warning

The frontend currently uses:

```text
Node.js             23.1.0
React               19.3.0
React DOM           19.3.0
Vite                8.3.1
@vitejs/plugin-react 6.1.1
```

Running npm commands may emit an experimental CommonJS / ES-module warning from npm's internal dependencies under Node 23.

The warning has not affected:

- Vite startup;
- React execution;
- TypeScript compilation;
- production builds.

The runtime was therefore left unchanged during the build.

A future deployment environment may use a current Node LTS release if needed.

---

# 8. Initial Project Structure

The project was created at:

```text
/Users/lissettegorrin/Desktop/_Gradensal/Signature_Builds/
marketing-ai-workflow-architect
```

Initial structure:

```text
marketing-ai-workflow-architect/
├── backend/
│   ├── __init__.py
│   ├── app/
│   │   ├── __init__.py
│   │   ├── api/
│   │   ├── core/
│   │   ├── models/
│   │   ├── services/
│   │   └── main.py
│   └── tests/
│
├── frontend/
│
├── docs/
│   ├── architecture/
│   └── decisions/
│
├── research/
│
├── assets/
│   ├── screenshots/
│   ├── diagrams/
│   └── demo/
│
├── case-study/
│
├── .env.example
├── .gitignore
├── README.md
├── PROJECT.md
├── BUILD_LEDGER.md
├── requirements.txt
└── requirements-dev.txt
```

---

# 9. Milestone 1 — Project Foundation

## Status

```text
COMPLETE
```

Created:

- professional repository structure;
- Python virtual environment;
- dependency files;
- environment template;
- `.gitignore`;
- project metadata;
- initial README;
- build ledger;
- Git repository on branch `main`.

Git identity:

```text
Name   Lissette Gorrin Rodriguez
Email  gradensal@gmail.com
```

---

# 10. Milestone 2 — Workflow Domain Model

## Status

```text
COMPLETE
```

Created:

```text
backend/app/models/workflow.py
```

The `WorkflowInput` model captures:

- name;
- team;
- description;
- repeatability;
- ambiguity;
- tool use;
- external actions;
- business risk;
- data sensitivity;
- mandatory human approval.

Architecture scores are constrained to:

```text
1 through 5
```

Unexpected fields are rejected.

Whitespace is normalized.

---

# 11. Milestone 3 — Architecture Assessment Model

## Status

```text
COMPLETE
```

Created:

```text
backend/app/models/assessment.py
```

Architecture recommendation enum:

```text
deterministic_automation
llm_assisted_workflow
agentic_workflow
keep_human_redesign_first
```

Risk enum:

```text
low
medium
high
```

`ArchitectureAssessment` includes:

- recommendation;
- risk level;
- decision strength;
- human approval required;
- human approval reason;
- rationale;
- warnings.

Important design decision:

```text
decision_strength
```

represents strength of explicit rule match.

It is not:

- a probability;
- model confidence;
- statistical certainty.

---

# 12. Milestone 4 — Deterministic Decision Engine

## Status

```text
COMPLETE
```

Created:

```text
backend/app/services/decision_engine.py
```

The engine evaluates workflow characteristics using explicit rules.

---

## Risk determination

Risk is based on the strongest of:

```text
business risk
data sensitivity
```

Representative mapping:

```text
4–5   high
3     medium
1–2   low
```

---

## Human approval

Approval can be required when:

- the workflow already mandates approval;
- business risk is meaningful;
- external actions are highly consequential;
- data sensitivity is high.

---

## Human-first override

Human-first redesign has precedence when risk exceeds the autonomy boundary.

Representative cases include:

```text
business risk >= 4
AND
external actions >= 4
```

or:

```text
data sensitivity >= 5
AND
external actions >= 3
```

---

## Deterministic automation

Representative criteria:

```text
repeatability >= 4
ambiguity <= 2
external actions <= 2
business risk <= 2
data sensitivity <= 3
```

---

## Agentic workflow

Representative criteria:

```text
ambiguity >= 4
tool use >= 4
external actions >= 3
business risk <= 3
data sensitivity <= 3
```

---

## Default middle architecture

Workflows requiring interpretation or generation but not strongly justifying agentic behavior are classified as:

```text
LLM-ASSISTED WORKFLOW
```

---

# 13. Milestone 5 — Deterministic Demo

## Status

```text
COMPLETE
```

Created:

```text
scripts/run_decision_demo.py
```

Canonical command:

```bash
python3 -m scripts.run_decision_demo
```

The demo exercises all four architecture families.

---

## Scenario A

```text
Weekly campaign reporting
→ DETERMINISTIC AUTOMATION
→ LOW risk
→ 5/5 decision strength
→ no human approval
```

---

## Scenario B

```text
Campaign message drafting
→ LLM ASSISTED WORKFLOW
→ LOW risk
→ 4/5 decision strength
→ no human approval
```

---

## Scenario C

```text
Campaign anomaly investigation
→ AGENTIC WORKFLOW
→ MEDIUM risk
→ 4/5 decision strength
→ human approval required
```

---

## Scenario D

```text
Autonomous customer pricing
→ KEEP HUMAN REDESIGN FIRST
→ HIGH risk
→ 5/5 decision strength
→ human approval required
```

---

# 14. Python Script Import Issue

Initial command:

```bash
python3 scripts/run_decision_demo.py
```

failed with:

```text
ModuleNotFoundError: No module named 'backend'
```

Cause:

Python used the `scripts/` directory as the script import location, so the sibling `backend/` package was not automatically visible.

Temporary working command:

```bash
PYTHONPATH=. python3 scripts/run_decision_demo.py
```

Permanent project convention:

```bash
python3 -m scripts.run_decision_demo
```

Added:

```text
scripts/__init__.py
```

This provides a cleaner module-based execution pattern.

---

# 15. Milestone 6 — AI Explanation Layer

## Status

```text
COMPLETE
```

Created:

```text
backend/app/models/explanation.py
backend/app/services/explanation_service.py
backend/app/core/config.py
scripts/run_ai_explanation_demo.py
```

---

## AI responsibility

The LLM receives:

- original workflow characteristics;
- deterministic recommendation;
- risk level;
- decision strength;
- approval requirement;
- rationale;
- warnings.

It produces six structured fields:

```text
why_this_approach
why_not_more_autonomy
proposed_architecture
human_checkpoint
first_experiment
success_metric
```

---

## Authority rule

The model is explicitly instructed not to change:

- recommendation;
- risk;
- human approval;
- deterministic policy.

The model explains the decision rather than making the decision.

---

## OpenAI configuration

Backend `.env.example`:

```text
APP_ENV=development
OPENAI_API_KEY=your_api_key_here
OPENAI_MODEL=gpt-6-luna
```

The real API key exists only in the local project-root `.env`.

It is not committed.

---

# 16. OpenAI Integration Issues

## Invalid API key

The first live request returned:

```text
401
```

A new API key was created.

---

## No API credits

The next live request returned:

```text
429
```

API billing was separate from the ChatGPT subscription.

A small API balance was purchased.

---

## Successful live explanation

After API billing was configured, the live explanation demo completed successfully.

The Campaign Message Drafting scenario returned:

```text
Recommendation
LLM ASSISTED WORKFLOW

Risk
LOW
```

plus structured explanation content covering:

- why the approach fits;
- why more autonomy is unnecessary;
- proposed architecture;
- human checkpoint;
- first experiment;
- success metric.

---

# 17. Milestone 7 — Combined Analysis API

## Status

```text
COMPLETE
```

Created:

```text
backend/app/models/analysis.py
backend/app/api/analysis.py
```

Endpoint:

```text
POST /api/v1/analyze
```

The endpoint performs:

```text
WorkflowInput validation
        ↓
Deterministic assessment
        ↓
AI explanation
        ↓
WorkflowAnalysis
```

---

## Public API paths

Verified through OpenAPI:

```text
/api/v1/analyze
/api/v1/assess
/health
```

---

# 18. FastAPI Route Inspection Issue

Initial diagnostic command attempted:

```python
[route.path for route in app.routes]
```

and failed because the current FastAPI version included an internal:

```text
_IncludedRouter
```

object without a `path` attribute.

The application itself was not broken.

A better diagnostic was used:

```bash
python3 -c "from backend.app.main import app; print(sorted(app.openapi()['paths'].keys()))"
```

Verified:

```text
['/api/v1/analyze', '/api/v1/assess', '/health']
```

Lesson:

Use the generated OpenAPI schema when verifying the application's public endpoint contract rather than depending on internal router object implementation details.

---

# 19. Milestone 8 — React Product Interface

## Status

```text
COMPLETE
```

Frontend scaffold:

```text
React 19.3.0
React DOM 19.3.0
Vite 8.3.1
@vitejs/plugin-react 6.1.1
TypeScript
```

---

# 20. Gradensal Product Identity

The frontend established the initial Gradensal application design language.

Palette:

```text
Gradensal Ink          #020611
Deep Navy              #001556
Deep Cobalt            #023496
Cobalt Blue            #0450D1
Electric Blue          #0E83E9
Gradensal Cyan         #17BDF7
Ice Blue               #53CFFB
Frost                  #E7FAFD
```

Visual direction:

```text
technical
premium
restrained
dark
precise
luminous blue
glass-like
```

Avoided:

```text
generic purple SaaS
gaming-neon aesthetic
overly decorative interface
```

---

# 21. Frontend Architecture

Current frontend structure includes:

```text
frontend/src/
├── assets/
│   └── gradensal-logo.png
│
├── components/
│   ├── ScoreField.tsx
│   └── WorkflowForm.tsx
│
├── services/
│   └── analysisApi.ts
│
├── styles/
│   ├── tokens.css
│   ├── global.css
│   ├── app.css
│   ├── analysis.css
│   └── polish.css
│
├── types/
│   ├── workflow.ts
│   └── analysis.ts
│
├── App.tsx
└── main.tsx
```

---

# 22. Workflow Intake UX

The React form mirrors the backend `WorkflowInput` contract.

It captures:

- workflow name;
- team;
- description;
- repeatability;
- ambiguity;
- tool use;
- external actions;
- business risk;
- data sensitivity;
- mandatory human approval.

Reusable component:

```text
ScoreField.tsx
```

is used for all six architecture signals.

---

# 23. Frontend API Contract

TypeScript mirrors the backend's Pydantic structures.

Conceptually:

```text
Python WorkflowInput
        ↕
JSON
        ↕
TypeScript WorkflowInput
```

and:

```text
Python WorkflowAnalysis
        ↕
JSON
        ↕
TypeScript WorkflowAnalysis
```

This reduces ambiguity across the network boundary.

---

# 24. CORS

Development frontend:

```text
http://localhost:5173
```

Development backend:

```text
http://127.0.0.1:8000
```

FastAPI CORS explicitly allows:

```text
http://localhost:5173
http://127.0.0.1:5173
```

Wildcard origins were intentionally avoided.

---

# 25. Frontend Environment Configuration

Frontend `.env.example`:

```text
VITE_API_BASE_URL=http://127.0.0.1:8000
```

Frontend `.env` is ignored by Git.

Verified:

```text
.env          ignored
.env.example  trackable
```

Important rule:

> Never put the OpenAI API key in a `VITE_*` variable.

`VITE_*` values are browser-accessible.

The OpenAI key remains exclusively in the backend environment.

---

# 26. End-to-End Integration

## Status

```text
COMPLETE
```

Verified browser path:

```text
React form
        ↓
POST /api/v1/analyze
        ↓
FastAPI
        ↓
Pydantic
        ↓
Deterministic engine
        ↓
AI explanation
        ↓
WorkflowAnalysis
        ↓
React results UI
```

Backend observed:

```text
OPTIONS /api/v1/analyze 200 OK
POST /api/v1/analyze    200 OK
```

---

# 27. First Complete Product Result

A high-risk workflow produced:

```text
KEEP HUMAN / REDESIGN FIRST

Risk
HIGH

Decision strength
5/5

Human approval
Required
```

The browser simultaneously displayed:

- deterministic assessment;
- source label `RULE ENGINE`;
- approval reasoning;
- deterministic rationale;
- guardrails;
- AI explanation;
- source label for generative explanation.

This validated the complete product loop.

---

# 28. Milestone 9 — Evaluation & Hardening

## Status

```text
COMPLETE
```

The hardening phase focused on proving that the product behaves according to its architectural claims.

---

# 29. Authority-Boundary Tests

Created:

```text
backend/tests/test_authority_boundaries.py
```

Added four tests.

They prove:

1. high business risk overrides otherwise agentic characteristics;
2. extreme data sensitivity plus external action can require redesign;
3. tool count alone does not make a workflow agentic;
4. agentic architecture is available when adaptive behavior is justified and risk remains bounded.

Result:

```text
4 passed
```

Backend total after this checkpoint:

```text
39 passed
```

---

# 30. Graceful AI Failure

The combined response model was hardened so that:

```text
assessment
```

is authoritative and required, while:

```text
explanation
```

may become unavailable independently.

Current analysis response supports:

```text
assessment
explanation
explanation_status
explanation_message
```

Possible explanation statuses:

```text
available
unavailable
```

---

# 31. AI Failure Boundary

Important implementation decision:

The deterministic assessment executes outside the AI `try/except` boundary.

Conceptually:

```text
assessment = assess_workflow(...)

try:
    explanation = generate(...)
except:
    preserve assessment
```

Not:

```text
try:
    assessment = ...
    explanation = ...
except:
    fail everything
```

This directly encodes the project's authority hierarchy.

---

# 32. Resilience Tests

Created:

```text
backend/tests/test_analysis_resilience.py
```

Tests verify:

### Successful explanation

```text
HTTP 200
assessment present
explanation present
explanation_status = available
```

### Failed explanation

```text
HTTP 200
assessment preserved
explanation = null
explanation_status = unavailable
user-facing explanation message present
```

Result:

```text
2 passed
```

Full backend suite:

```text
41 passed
```

---

# 33. Current Automated Test Baseline

Verified command:

```bash
python3 -m pytest backend/tests -q
```

Verified result:

```text
......................................... [100%]
41 passed
```

This is the current baseline for release.

---

# 34. Frontend Failure States

The frontend now distinguishes:

## Initial

```text
Awaiting workflow
```

## Loading

```text
ANALYZING WORKFLOW
```

## Complete

Displays:

```text
deterministic assessment
+
AI explanation
```

## FastAPI unavailable

Displays controlled request failure messaging.

## AI explanation unavailable

Displays:

```text
deterministic assessment
+
AI EXPLANATION UNAVAILABLE
```

and explicitly communicates that the rule-engine recommendation remains valid.

---

# 35. Double-Submission Protection

While an analysis request is active, the application disables:

- workflow name;
- team;
- description;
- all six sliders;
- approval checkbox;
- Load example;
- Reset;
- Analyze workflow.

This prevents accidental repeated API requests.

---

# 36. Slider UX Improvement

The final `ScoreField` exposes:

```text
--score-progress
```

to CSS.

Slider illumination now visually represents:

```text
1/5    0%
2/5   25%
3/5   50%
4/5   75%
5/5  100%
```

This improves immediate interpretation of architecture scores.

---

# 37. Accessibility QA

Manual keyboard testing verified navigation through:

- Load example;
- Reset;
- workflow name;
- team;
- description;
- repeatability slider;
- ambiguity slider;
- tool-use slider;
- external-action slider;
- business-risk slider;
- data-sensitivity slider;
- approval checkbox;
- Analyze workflow.

Verified:

- keyboard focus;
- visible focus treatment;
- slider arrow controls;
- checkbox keyboard toggling.

---

# 38. Responsive QA

Manual QA completed at representative viewport sizes.

## Desktop

```text
1440px+
```

Result:

```text
PASS
```

---

## Laptop

```text
~1100px
```

Result:

```text
PASS
```

---

## Tablet

```text
768 × 1024
```

Result:

```text
PASS
```

---

## Mobile

```text
390 × 844
```

Result:

```text
PASS
```

Verified:

- responsive hero;
- panel stacking;
- mobile sliders;
- touch targets;
- footer stacking;
- no unexpected horizontal scrolling.

---

# 39. API-Down QA

FastAPI was intentionally stopped while the React application remained active.

Result:

```text
PASS
```

The application:

- remained rendered;
- preserved workflow data;
- displayed a controlled connectivity error.

---

# 40. Logo Optimization

Original frontend logo:

```text
1254 × 1254
approximately 1.3 MB
```

Preserved master:

```text
assets/brand/gradensal-logo-master.png
```

Optimized frontend copy:

```text
900 × 900
approximately 843 KB
```

Final Vite bundle reported:

```text
gradensal-logo
862.80 kB
```

The approved master asset remains unchanged.

---

# 41. Product Metadata

The frontend now includes:

- Gradensal favicon;
- descriptive application title;
- theme-color metadata;
- page description;
- author metadata;
- application name;
- Open Graph title;
- Open Graph description;
- Open Graph site name.

Browser title:

```text
Marketing AI Workflow Architect | Gradensal
```

---

# 42. Product Header

Final header contains:

```text
GRADENSAL
SIGNATURE BUILDS

ARCHITECTURE DECISION SYSTEM

GSB-002
```

The system-status treatment is intentionally subtle.

---

# 43. Product Footer

Final footer includes:

```text
Gradensal
Signature Build GSB-002

Marketing AI Workflow Architect
Prototype v0.1.0
Lissette Gorrin Rodriguez
```

The product remains labeled:

```text
Prototype v0.1.0
```

until repository documentation, case study, GitHub release, and final release verification are complete.

---

# 44. Final Frontend Build Baseline

Verified production build:

```text
Vite 8.3.1

25 modules transformed
```

Representative final bundle:

```text
dist/index.html
1.45 kB

Gradensal logo
862.80 kB

CSS
24.50 kB

JavaScript
235.47 kB
```

The build completed without TypeScript errors.

---

# 45. Milestone 10 — Product Polish

## Status

```text
COMPLETE
```

Completed:

- logo optimization;
- slider visual progress;
- disabled-state consistency;
- product metadata;
- favicon;
- header refinement;
- footer;
- responsive QA;
- accessibility QA;
- API-down QA;
- browser presentation.

The frontend is considered feature-frozen unless an actual defect is discovered.

---

# 46. Milestone 11A — Architecture Documentation

## Status

```text
COMPLETE
```

Created:

```text
docs/architecture/system-architecture.md
```

Current length:

```text
610 lines
```

Contains four Mermaid diagrams covering:

1. end-to-end architecture;
2. authority boundary;
3. architecture recommendation flow;
4. graceful degradation.

---

# 47. Milestone 11B — Engineering Evaluation

## Status

```text
COMPLETE
```

Created:

```text
docs/evaluation/evaluation-report.md
```

Current length:

```text
1177 lines
```

Contains 30 primary sections covering:

- evaluation strategy;
- domain validation;
- canonical scenarios;
- authority boundaries;
- human approval;
- AI authority;
- graceful degradation;
- API behavior;
- live integration evidence;
- frontend QA;
- responsive behavior;
- accessibility;
- limitations;
- evidence boundaries.

Current test baseline documented:

```text
41 passing backend tests
```

---

# 48. Milestone 11C — README

## Status

```text
FINAL README PREPARED
```

The final README is designed as the repository landing page.

It covers:

- problem;
- architecture outcomes;
- system architecture;
- authority boundaries;
- graceful degradation;
- evaluation evidence;
- API;
- frontend;
- technology stack;
- repository structure;
- local setup;
- engineering decisions;
- limitations;
- Gradensal;
- author.

Canonical future repository URL:

```text
https://github.com/Gradensal/marketing-ai-workflow-architect
```

---

# 49. Important Engineering Principles Learned

## 49.1 AI does not automatically mean agent

Tool count, complexity, or model availability are insufficient reasons to build an autonomous agent.

---

## 49.2 Risk must participate in architecture selection

A technically capable agent may still be the wrong architecture when:

- risk is high;
- actions are consequential;
- information is extremely sensitive.

---

## 49.3 Architecture and approval are different questions

A workflow can be:

```text
AGENTIC
```

while still requiring:

```text
HUMAN APPROVAL
```

---

## 49.4 Generative AI should have explicit authority boundaries

The LLM in GSB-002 is intentionally constrained to explanation.

The deterministic layer owns policy.

---

## 49.5 Graceful degradation matters

An external AI outage should not eliminate a valid deterministic result.

---

## 49.6 Tests should avoid unnecessary live model calls

Deterministic policy and integration contracts can be tested using:

- fake clients;
- injected dependencies;
- controlled explanation generators.

Live model requests are reserved for deliberate integration checks.

---

## 49.7 UI should expose system boundaries

The frontend deliberately labels:

```text
RULE ENGINE
```

separately from:

```text
GPT-6 LUNA
```

so the user can see which layer produced which information.

---

# 50. Bugs and Lessons

## Bug — wrong pytest environment

### Symptom

The shell showed:

```text
(.venv) (base)
```

and pytest used the wrong environment.

### Fix

- fully deactivate Conda;
- disable automatic base activation;
- activate project `.venv` once;
- prefer:

```bash
python3 -m pytest
```

over:

```bash
pytest
```

### Lesson

Do not assume the shell prompt alone proves which interpreter is executing.

Verify:

```bash
which python3
python3 --version
python3 -m pytest --version
```

---

## Bug — Python demo could not import backend

### Symptom

```text
ModuleNotFoundError: No module named 'backend'
```

### Cause

Direct script execution changed Python's import search path.

### Fix

Use:

```bash
python3 -m scripts.run_decision_demo
```

### Lesson

Prefer package/module execution for repository scripts with project-level imports.

---

## Bug — FastAPI route inspection

### Symptom

```text
AttributeError: '_IncludedRouter' object has no attribute 'path'
```

### Cause

Diagnostic code relied on an internal routing implementation detail.

### Fix

Inspect:

```python
app.openapi()["paths"]
```

### Lesson

Prefer stable public contracts over framework internals when verifying behavior.

---

## Bug — npm run build from project root

### Symptom

```text
ENOENT
Could not read package.json
```

### Cause

`npm run build` was executed from:

```text
marketing-ai-workflow-architect/
```

instead of:

```text
marketing-ai-workflow-architect/frontend/
```

### Fix

Run frontend commands from:

```text
frontend/
```

### Lesson

Maintain clear Backend Terminal and Frontend Terminal responsibilities.

---

## Bug — frontend form initially unstyled

### Symptom

React form rendered with browser-default controls.

### Cause

Workflow form CSS had not been added to the active application stylesheet.

### Fix

Add the form styling layer.

### Lesson

When:

```text
component renders
data renders
interaction works
visual style missing
```

debug the presentation layer rather than rewriting working React logic.

---

# 51. Security Decisions

The project intentionally:

- keeps the OpenAI API key only on the backend;
- ignores real `.env` files;
- tracks `.env.example`;
- avoids OpenAI secrets in `VITE_*`;
- restricts development CORS origins;
- validates API input;
- validates AI output;
- separates deterministic authority from generative explanation;
- does not execute consequential external business actions.

---

# 52. Current Repository Test Commands

## Backend

```bash
python3 -m pytest backend/tests -q
```

Expected:

```text
41 passed
```

---

## Deterministic architecture demo

```bash
python3 -m scripts.run_decision_demo
```

Expected architecture families:

```text
DETERMINISTIC AUTOMATION
LLM ASSISTED WORKFLOW
AGENTIC WORKFLOW
KEEP HUMAN REDESIGN FIRST
```

---

## Frontend

From:

```text
frontend/
```

run:

```bash
npm run build
```

Expected:

```text
successful TypeScript + Vite production build
```

---

# 53. Development Servers

## Backend Terminal

```bash
python3 -m uvicorn backend.app.main:app --reload
```

Backend:

```text
http://127.0.0.1:8000
```

Swagger:

```text
http://127.0.0.1:8000/docs
```

---

## Frontend Terminal

```bash
npm run dev
```

Frontend:

```text
http://localhost:5173
```

---

# 54. Visual Documentation

Existing or planned screenshot sequence:

```text
01-workflow-model-tests-passing.png

02-four-architecture-decisions.png

03-fastapi-assessment-endpoint.png

04-combined-analysis-api.png

05-gradensal-frontend-foundation.png

06-human-first-analysis.png

07-llm-assisted-analysis.png
```

Final public documentation should use only the cleanest screenshots.

---

# 55. Preserved Brand Asset

Master Gradensal logo:

```text
assets/brand/gradensal-logo-master.png
```

This file should remain unchanged.

Frontend optimized copy:

```text
frontend/src/assets/gradensal-logo.png
```

Favicon:

```text
frontend/public/favicon.png
```

---

# 56. Documentation Set

Current documentation includes:

```text
PROJECT.md

BUILD_LEDGER.md

README.md

docs/architecture/
└── system-architecture.md

docs/evaluation/
└── evaluation-report.md
```

Remaining major written deliverable:

```text
case-study/
```

---

# 57. Current Product State

```text
Project foundation                  COMPLETE
Workflow domain model               COMPLETE
Architecture assessment model       COMPLETE
Deterministic decision engine       COMPLETE
Deterministic demo                  COMPLETE
AI explanation layer                COMPLETE
Combined analysis API               COMPLETE
React frontend                      COMPLETE
Gradensal design system             COMPLETE
End-to-end browser workflow         COMPLETE
Authority-boundary evaluation       COMPLETE
AI failure resilience               COMPLETE
Responsive QA                       COMPLETE
Accessibility QA                    COMPLETE
Product polish                      COMPLETE
Architecture documentation          COMPLETE
Engineering evaluation              COMPLETE
README                              PREPARED
Case study                          NEXT
GitHub finalization                 PENDING
Release                            PENDING
Public showcase                    PENDING
```

---

# 58. Release Requirements

Before declaring `v1.0.0`, complete:

1. final case study;
2. repository status review;
3. secret scan / `.gitignore` review;
4. backend final test;
5. frontend final build;
6. clean Git history;
7. GitHub repository verification;
8. screenshots;
9. release tag;
10. release notes.

---

# 59. Current Quality Baseline

```text
Backend tests                   41 passing
Decision families               4/4 verified
Authority-boundary tests        passing
AI resilience tests             passing
FastAPI end-to-end              passing
React ↔ FastAPI                 passing
Live OpenAI explanation         verified
Desktop QA                      passing
Laptop QA                       passing
Tablet QA                       passing
Mobile QA                       passing
Keyboard QA                     passing
Frontend validation             passing
Double-submit protection        passing
API-down handling               passing
Production frontend build       passing
```

---

# 60. Core Architectural Thesis

The project demonstrates:

```text
Deterministic software
for explicit policy

LLMs
for interpretation and communication

Agents
for bounded adaptive execution

Humans
for consequential authority
```

The system therefore does not ask:

> How can we make this workflow more autonomous?

It asks:

> **What is the least autonomous architecture that can responsibly accomplish the work?**

---

# 61. Portfolio Positioning

GSB-002 demonstrates the intersection of:

```text
AI architecture
+
software engineering
+
governance
+
marketing workflows
+
product design
+
technical storytelling
```

The portfolio story is not:

> I called an LLM from React.

The stronger story is:

> **I designed a hybrid decision-support system that separates deterministic policy authority from generative explanation, evaluates the appropriate level of autonomy, enforces governance boundaries, degrades gracefully when AI is unavailable, and exposes those system boundaries clearly in the product UX.**

---

# 62. Next Milestone

## Milestone 11E — Case Study

Create a portfolio-quality case study explaining:

- the business problem;
- architecture question;
- solution;
- decision framework;
- implementation;
- authority boundaries;
- evaluation;
- failures and lessons;
- final product;
- what the build demonstrates professionally.

After the case study:

```text
Milestone 12
Git + GitHub + release

Milestone 13
Public showcase package
```

---

# 63. Current Build Status

**GSB-002 application development is complete.**

Remaining work is primarily:

```text
DOCUMENT
        ↓
PACKAGE
        ↓
RELEASE
        ↓
SHOW
```

The product should not receive new features unless a defect is discovered during final release verification.