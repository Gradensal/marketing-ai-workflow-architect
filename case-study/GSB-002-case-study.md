# GSB-002 - Marketing AI Workflow Architect

## Choosing the right level of AI before building the system

**Gradensal Signature Build**  
**Author:** Lissette Gorrin Rodriguez  
**Focus:** AI Architecture × Marketing Operations × Governance × Product Engineering

---

# Executive Summary

Organizations are under pressure to add AI to business workflows.

But the first architecture question should not be:

> **Where can we add an AI agent?**

It should be:

> **What level of automation or autonomy does this workflow actually need?**

I built **Marketing AI Workflow Architect** to explore that question.

The product evaluates a business workflow across six operational signals and recommends one of four architectures:

```text
Deterministic automation

LLM-assisted workflow

Agentic workflow

Keep human / redesign first
```

The most important design decision was not the user interface or even the LLM integration.

It was the system's **authority boundary**.

The recommendation is produced by explicit deterministic rules.

Only after that decision exists is a generative model allowed to explain it.

In other words:

> **The rule engine decides. The LLM explains.**

This created a prototype where AI adds interpretation and communication without becoming the uncontrolled source of architecture policy.

The finished system includes:

- a deterministic architecture decision engine;
- typed workflow and assessment models;
- risk-based autonomy boundaries;
- explicit human-approval logic;
- structured generative explanations;
- graceful degradation when the AI provider is unavailable;
- FastAPI endpoints;
- a React + TypeScript frontend;
- responsive and keyboard-accessible interaction;
- 41 passing backend tests;
- four canonical architecture scenarios;
- architecture and engineering evaluation documentation.

---

# 1. The Problem I Wanted to Explore

AI conversations inside organizations increasingly move quickly from:

```text
We have this workflow
```

to:

```text
Let's put an agent on it.
```

That jump skips an important architecture decision.

A workflow may involve repetitive work, many tools, judgment, sensitive data, or consequential actions.

Those characteristics do not all imply the same solution.

For example:

### A highly repeatable reporting workflow

may need:

```text
ordinary deterministic automation
```

rather than an LLM.

### A marketing drafting workflow

may benefit from:

```text
LLM assistance
```

without autonomous execution.

### An investigation workflow

may justify:

```text
bounded agentic behavior
```

because the sequence of actions cannot be completely predetermined.

### A high-risk pricing workflow

may technically be automatable while still requiring:

```text
human control and workflow redesign
```

The architecture problem is therefore not:

> How much AI can we add?

It is:

> **What is the least autonomous architecture that can responsibly accomplish the work?**

That became the core thesis of GSB-002.

---

# 2. Why I Chose a Marketing Workflow Context

I wanted the project to sit at the intersection of:

```text
AI systems

software engineering

business workflows

marketing operations

risk and governance

technical communication
```

Marketing is particularly useful for this exploration because the domain contains workflows with very different characteristics.

Some are highly structured:

```text
report generation
data transformation
scheduled exports
campaign tagging
```

Some involve generation:

```text
message drafting
content variation
summarization
research synthesis
```

Some require adaptive investigation:

```text
campaign anomaly analysis
performance diagnostics
cross-system investigation
```

And some can carry significant business consequences:

```text
pricing changes
customer-facing actions
budget reallocations
sensitive-data decisions
```

That variation made marketing workflows a useful domain for testing architecture boundaries.

---

# 3. My Initial Architecture Question

Before writing the AI integration, I defined four possible outcomes:

```text
1. Deterministic automation

2. LLM-assisted workflow

3. Agentic workflow

4. Keep human / redesign first
```

I did not want the application to treat these as maturity levels.

They are not:

```text
basic
better
advanced
best
```

Instead, they are different architecture families appropriate for different operating conditions.

That distinction shaped the entire system.

---

# 4. The Six Architecture Signals

The prototype evaluates six workflow characteristics.

## Repeatability

How consistently does the workflow follow the same sequence?

```text
1 = changes often

5 = highly repeatable
```

High repeatability can be evidence that deterministic automation is sufficient.

---

## Ambiguity

How much interpretation or judgment is required?

```text
1 = clear rules

5 = substantial judgment
```

Higher ambiguity increases the potential value of language-model reasoning or adaptive behavior.

---

## Tool Use

How much does the workflow depend on other systems or information sources?

```text
1 = few tools

5 = many systems
```

One of the important lessons in the project was:

> **Tool count alone does not make a workflow agentic.**

A workflow can integrate many systems while still being completely deterministic.

---

## External Actions

How consequentially does the workflow act on systems outside itself?

```text
1 = mostly read-only

5 = consequential external action
```

This signal becomes especially important when combined with risk.

---

## Business Risk

What could happen if the system makes a bad decision?

```text
1 = minor impact

5 = severe impact
```

Risk is not merely presented to the user.

It participates directly in architecture selection.

---

## Data Sensitivity

How sensitive is the information handled by the workflow?

```text
1 = public or low sensitivity

5 = highly sensitive
```

High data sensitivity can constrain autonomy even when the workflow otherwise looks technically suitable for an agent.

---

# 5. The Architecture Decision Engine

I intentionally implemented architecture selection as deterministic software.

The system does not send the workflow to an LLM and ask:

> What architecture would you recommend?

Instead, explicit rules determine the recommendation.

This gives the decision layer properties that are valuable for governance:

```text
repeatability

testability

inspectability

predictability

clear failure boundaries
```

---

# 6. Why Deterministic First Matters

Generative models are useful when interpretation is required.

But I did not want a probabilistic model to become the source of truth for a policy decision that I could express explicitly.

The architecture therefore follows:

```text
Workflow characteristics
        ↓
Deterministic rules
        ↓
Architecture assessment
        ↓
Assessment becomes authoritative
        ↓
Generative explanation
```

The model receives the decision after it has already been made.

That means the LLM is useful without owning the decision.

---

# 7. The Authority Boundary

This became the most important concept in the project.

The generative layer is not permitted to modify:

```text
architecture recommendation

risk level

decision strength

human-approval requirement

deterministic rationale

deterministic warnings
```

Conceptually:

```text
RULE ENGINE
    ↓
DECIDES

LLM
    ↓
EXPLAINS
```

This prevents the system from quietly shifting policy authority to the model.

---

# 8. Recommendation 1 - Deterministic Automation

The system selects deterministic automation when the workflow is strongly characterized by:

```text
high repeatability

low ambiguity

limited consequential external action

low business risk

bounded data sensitivity
```

Representative scenario:

## Weekly Campaign Reporting

Verified result:

```text
DETERMINISTIC AUTOMATION

Risk
LOW

Decision strength
5/5

Human approval
Not required
```

The design principle here is important:

> **Do not introduce AI when ordinary software is sufficient.**

A scheduled reporting pipeline can often be cheaper, faster, easier to test, and more reliable than an AI-driven process.

---

# 9. Recommendation 2 - LLM-Assisted Workflow

The LLM-assisted category covers workflows where language interpretation or generation adds value but autonomous tool execution is unnecessary.

Representative scenario:

## Campaign Message Drafting

Verified result:

```text
LLM-ASSISTED WORKFLOW

Risk
LOW

Decision strength
4/5

Human approval
Not required
```

In this type of architecture:

```text
software controls the workflow

LLM produces or interprets content

human or deterministic logic retains final authority
```

This is intentionally different from an agent.

---

# 10. Recommendation 3 - Agentic Workflow

Agentic architecture becomes appropriate when the workflow requires a combination of:

```text
high ambiguity

substantial tool use

adaptive intermediate decisions

meaningful external actions

bounded risk
```

Representative scenario:

## Campaign Anomaly Investigation

Verified result:

```text
AGENTIC WORKFLOW

Risk
MEDIUM

Decision strength
4/5

Human approval
Required
```

The significant part of this result is:

```text
Agentic
+
Human approval required
```

Those ideas are not contradictory.

An agent may be allowed to:

- gather evidence;
- select tools;
- investigate;
- compare results;
- prepare a proposed action.

That does not mean it should have unrestricted authority to perform every consequential final action.

---

# 11. Recommendation 4 - Keep Human / Redesign First

The fourth category exists because some workflows should not become more autonomous simply because automation is technically possible.

Representative scenario:

## Autonomous Customer Pricing

Verified result:

```text
KEEP HUMAN / REDESIGN FIRST

Risk
HIGH

Decision strength
5/5

Human approval
Required
```

This recommendation can override otherwise agentic characteristics.

That was a deliberate policy decision.

The system treats:

```text
capability
```

and:

```text
permission
```

as different questions.

---

# 12. The Risk Override

One of the most important automated tests creates a workflow that strongly resembles an agentic candidate:

```text
high ambiguity

high tool use

high external action
```

But it also has:

```text
high business risk
```

The engine returns:

```text
KEEP HUMAN / REDESIGN FIRST
```

rather than:

```text
AGENTIC WORKFLOW
```

This test demonstrates the principle:

> **Governance can override capability.**

---

# 13. Sensitive Data as an Architecture Constraint

I also created an authority-boundary test for a workflow with:

```text
extremely sensitive data
+
meaningful external action
```

The result is human-first redesign.

This matters because sensitivity should not exist only as a warning shown after architecture selection.

In GSB-002, it can change the architecture itself.

---

# 14. Tool Use Does Not Equal Agency

This became another explicit test.

A workflow may connect to:

```text
CRM

analytics

advertising platform

content repository

data warehouse
```

and still follow a completely known sequence.

Multiple integrations create orchestration complexity.

They do not automatically create autonomous decision-making.

The test suite therefore verifies:

> **High tool use by itself must not return an agentic recommendation.**

---

# 15. Human Approval Is Its Own Decision

I separated:

```text
What architecture should execute this workflow?
```

from:

```text
Where does a human need to approve consequential behavior?
```

This allows outcomes such as:

```text
AGENTIC WORKFLOW
+
HUMAN APPROVAL REQUIRED
```

This is a more useful model of enterprise agents than treating autonomy as binary.

---

# 16. The Generative Explanation Layer

Once the deterministic assessment exists, the backend calls the generative layer.

The model receives:

- original workflow characteristics;
- recommendation;
- risk;
- decision strength;
- approval requirement;
- rationale;
- warnings.

It returns six structured fields:

```text
why_this_approach

why_not_more_autonomy

proposed_architecture

human_checkpoint

first_experiment

success_metric
```

The response is validated through a Pydantic model.

The frontend therefore receives a defined application contract rather than arbitrary model prose.

---

# 17. Why Structured Output Matters

If the application depended on unrestricted text such as:

```text
"Tell us what you think about this architecture..."
```

the UI would have to guess how to present the answer.

Instead, structured output allows the product to consistently render:

```text
WHY THIS APPROACH

WHY NOT MORE AUTONOMY

PROPOSED ARCHITECTURE

HUMAN CHECKPOINT

FIRST EXPERIMENT

SUCCESS METRIC
```

That improves:

- UI reliability;
- testing;
- downstream integration;
- stakeholder readability.

---

# 18. Graceful Degradation

Another key design decision came from asking:

> What happens if the AI provider is unavailable?

The first version of a combined system could easily behave like:

```text
assessment succeeds
+
LLM request fails
=
entire request fails
```

But that would contradict the architecture.

If the deterministic result is authoritative, then the model going offline should not destroy it.

I changed the response model so that:

```text
assessment
```

is mandatory while:

```text
explanation
```

can independently become unavailable.

---

# 19. The Final Failure Boundary

The backend now behaves conceptually like this:

```python
assessment = assess_workflow(workflow)

try:
    explanation = generate_explanation(
        workflow,
        assessment,
    )
except:
    preserve_the_assessment()
```

The assessment is computed **outside** the AI failure boundary.

If generation fails, the API still returns:

```text
HTTP 200

architecture assessment present

explanation = null

explanation_status = unavailable
```

The frontend then tells the user that the architecture decision remains valid.

---

# 20. Why This Failure Mode Matters

External AI services introduce dependencies that ordinary deterministic application code does not control.

Possible failures include:

- provider outage;
- authentication problems;
- quota exhaustion;
- model availability;
- request timeout;
- SDK failure.

A system should identify which parts of its functionality truly depend on that service.

In GSB-002:

```text
Explanation depends on the model.

Architecture policy does not.
```

The implementation now reflects that boundary.

---

# 21. Backend Architecture

The backend uses:

```text
FastAPI

Pydantic

Python

OpenAI Python SDK

pytest
```

Responsibilities are separated across:

```text
API routes

domain models

decision service

explanation service

configuration

tests
```

The request path is:

```text
HTTP request
    ↓
WorkflowInput validation
    ↓
Deterministic decision engine
    ↓
ArchitectureAssessment
    ↓
AI explanation attempt
    ↓
WorkflowAnalysis
```

---

# 22. API Design

The application exposes three primary endpoints:

```text
GET /health

POST /api/v1/assess

POST /api/v1/analyze
```

## `/api/v1/assess`

Runs only the deterministic architecture engine.

This makes the decision layer usable without depending on generative AI.

## `/api/v1/analyze`

Combines:

```text
deterministic assessment
+
optional generative explanation
```

into the complete product response.

---

# 23. Frontend Architecture

The frontend uses:

```text
React

TypeScript

Vite
```

It contains separate layers for:

```text
components

domain types

API service

product styles

analysis presentation

brand tokens
```

The TypeScript models mirror the backend's important Pydantic contracts.

Conceptually:

```text
Python domain model
        ↓
       JSON
        ↓
TypeScript domain model
```

This makes the network boundary explicit.

---

# 24. The Product Experience

I wanted the interface to expose the architecture rather than hide it.

The output is visibly separated into:

```text
DETERMINISTIC ASSESSMENT
```

and:

```text
AI EXPLANATION
```

The result source is also labeled.

That means the interface itself communicates:

> Which part came from explicit software policy, and which part came from the generative model?

This is part of the product design, not only backend architecture.

---

# 25. Gradensal Product Identity

The application also became an opportunity to establish a reusable Gradensal product language.

The interface uses:

```text
near-black surfaces

deep navy panels

cobalt blue

electric blue

cyan status accents

frost typography

restrained glass effects

chrome-blue Gradensal sculpture
```

The desired impression was:

```text
technical

premium

precise

calm

intentional
```

rather than a generic AI interface.

---

# 26. Interaction Design

The workflow form includes:

- workflow name;
- team;
- workflow description;
- six architecture sliders;
- mandatory approval control;
- sample workflow loader;
- reset action;
- analysis action.

Slider tracks visually represent their selected score.

For example:

```text
1/5    0% illuminated

3/5   50% illuminated

5/5  100% illuminated
```

This makes the architecture profile easier to scan.

---

# 27. Preventing Duplicate Requests

During analysis, all workflow controls become temporarily locked.

This includes:

```text
text fields

description

six sliders

approval checkbox

Load example

Reset

Analyze workflow
```

This prevents accidental duplicate API calls while the current request is running.

---

# 28. Browser Failure Experience

I deliberately tested the product with FastAPI stopped.

Instead of the interface disappearing or silently failing:

- the React application remains available;
- the workflow stays in the browser;
- a controlled error state appears;
- the user is told to verify the API and try again.

This is separate from an AI-provider failure.

The application therefore distinguishes:

```text
application API unavailable
```

from:

```text
AI explanation unavailable
```

---

# 29. Accessibility Testing

The interface was manually tested using keyboard navigation.

Keyboard focus reaches:

```text
Load example

Reset

Workflow name

Team

Description

Repeatability

Ambiguity

Tool use

External actions

Business risk

Data sensitivity

Human approval

Analyze workflow
```

The sliders support arrow-key adjustment.

The checkbox supports keyboard operation.

Interactive controls have visible focus treatment.

---

# 30. Responsive Testing

I tested representative layouts at approximately:

```text
Desktop
1440px+

Laptop
1100px

Tablet
768 × 1024

Mobile
390 × 844
```

The final product supports:

- desktop two-column workflow and analysis;
- tablet panel stacking;
- mobile form layout;
- responsive hero composition;
- touch-friendly controls;
- responsive footer behavior;
- no unexpected horizontal scrolling in the tested layouts.

---

# 31. Evaluation Strategy

I did not want to rely on a successful browser screenshot as proof that the architecture worked.

The project uses several layers of evidence:

```text
domain validation
        ↓
unit tests
        ↓
decision-engine tests
        ↓
authority-boundary tests
        ↓
API tests
        ↓
resilience tests
        ↓
deterministic scenario demo
        ↓
live model integration
        ↓
browser end-to-end testing
        ↓
responsive/accessibility QA
```

---

# 32. Automated Test Baseline

The final backend baseline currently contains:

```text
41 passing tests
```

Verified using:

```bash
python3 -m pytest backend/tests -q
```

Result:

```text
......................................... [100%]

41 passed
```

The automated suite does not require repeated live OpenAI calls.

---

# 33. Canonical Evaluation Scenarios

The deterministic evaluation demo covers all four architecture families.

| Workflow | Architecture | Risk | Strength | Human Approval |
|---|---|---|---:|---|
| Weekly campaign reporting | Deterministic automation | Low | 5/5 | No |
| Campaign message drafting | LLM-assisted workflow | Low | 4/5 | No |
| Campaign anomaly investigation | Agentic workflow | Medium | 4/5 | Yes |
| Autonomous customer pricing | Keep human / redesign first | High | 5/5 | Yes |

These scenarios provide a compact demonstration of the engine's intended behavior.

---

# 34. What I Tested Beyond the Happy Path

The project specifically includes tests for architectural boundary conditions.

These include:

```text
high-risk override

extreme-data-sensitivity override

tool-count-is-not-agency

bounded-risk agentic workflow

AI explanation failure
```

Those tests were more important to me than simply proving the normal API call worked.

They test the assumptions that define the product.

---

# 35. A Real Integration Failure I Encountered

The project was not built without problems.

One early deterministic demo failed with:

```text
ModuleNotFoundError:
No module named 'backend'
```

The issue was caused by running the script directly:

```bash
python3 scripts/run_decision_demo.py
```

which changed Python's effective import path.

I initially verified the diagnosis using:

```bash
PYTHONPATH=. python3 scripts/run_decision_demo.py
```

Then changed the project convention to:

```bash
python3 -m scripts.run_decision_demo
```

and added:

```text
scripts/__init__.py
```

The lesson was not only how to solve the import.

It reinforced the value of treating repository scripts as modules when they depend on project-level packages.

---

# 36. Another Debugging Lesson - Environment Ambiguity

At one stage my shell showed both:

```text
(.venv)
(base)
```

The Conda environment interfered with which Python environment was being used.

Rather than continuing to patch dependency symptoms, I verified:

```text
which python3

python3 --version

which pytest

python3 -m pytest --version
```

and disabled automatic Conda base activation.

The project now uses the dedicated `.venv` cleanly.

This reinforced a debugging principle:

> **Verify the runtime before debugging the application.**

---

# 37. Another Debugging Lesson — Public Contracts vs Internals

While inspecting FastAPI routes, an initial diagnostic assumed every internal route object exposed:

```text
route.path
```

That failed because one internal router object did not.

Rather than changing the application, I verified the actual public contract through:

```python
app.openapi()["paths"]
```

which returned:

```text
/api/v1/analyze

/api/v1/assess

/health
```

The lesson:

> Prefer a framework's stable public contract over undocumented internal implementation details.

---

# 38. API and ChatGPT Billing Are Different Systems

The first live model integration also exposed an operational lesson.

A working ChatGPT subscription did not provide API credits.

I encountered:

```text
401
```

while resolving credentials, followed by:

```text
429
```

when the API account had no available billing balance.

After configuring the API account correctly, the live structured explanation succeeded.

This was useful practical experience with the difference between:

```text
ChatGPT product access
```

and:

```text
OpenAI API access
```

---

# 39. Secrets Boundary

The project keeps:

```text
OPENAI_API_KEY
```

only on the backend.

The frontend environment contains only:

```text
VITE_API_BASE_URL
```

This matters because:

```text
VITE_*
```

values are delivered to the browser and are therefore not secret.

The actual `.env` is ignored by Git.

The repository tracks `.env.example` instead.

---

# 40. CORS Boundary

During local development:

```text
React
http://localhost:5173
```

communicates with:

```text
FastAPI
http://127.0.0.1:8000
```

The backend allows only the required local frontend origins rather than using an unrestricted wildcard.

Production deployment would replace those with the final deployment origins.

---

# 41. Asset Optimization

The approved Gradensal source image originally measured:

```text
1254 × 1254

approximately 1.3 MB
```

Before optimization, I preserved the master at:

```text
assets/brand/gradensal-logo-master.png
```

Then resized only the frontend working copy to:

```text
900 × 900

approximately 843 KB
```

The production bundle reports the image at approximately:

```text
862.80 kB
```

This reduced application delivery weight without sacrificing the preserved original asset.

---

# 42. Production Frontend Build

The final tested production build uses:

```text
React 19.3.0

React DOM 19.3.0

Vite 8.3.1
```

The verified build completed with:

```text
25 modules transformed
```

and no TypeScript build errors.

---

# 43. Product Metadata

The final browser presentation includes:

- Gradensal favicon;
- application title;
- description metadata;
- author metadata;
- theme color;
- Open Graph title;
- Open Graph description;
- product identifier;
- Gradensal footer.

Browser title:

```text
Marketing AI Workflow Architect | Gradensal
```

---

# 44. What I Would Add for Production

GSB-002 is intentionally a focused Signature Build.

A production system would require additional work.

Examples include:

```text
authentication

authorization

persistent storage

organization-specific policy configuration

audit history

workflow versioning

telemetry

rate limiting

model-cost controls

production secrets management

administrative controls

security review

privacy review

legal review

compliance review

deployment infrastructure

operational monitoring
```

The current decision policy would also need to be calibrated to the organization's real governance standards.

---

# 45. What the Current Evidence Does Not Prove

The current evaluation demonstrates that the prototype behaves as designed under the tested conditions.

It does not prove:

```text
universal correctness of the architecture policy

production security readiness

regulatory compliance

enterprise-scale performance

perfect model behavior

suitability for unrestricted high-impact autonomy
```

I consider that limitation important.

A credible AI system should distinguish:

```text
what has been demonstrated
```

from:

```text
what has merely been assumed
```

---

# 46. The Most Important Technical Lesson

The strongest lesson from this build is not:

> How to call an LLM from FastAPI.

It is:

> **Where should an LLM have authority?**

There are parts of a system where probabilistic interpretation creates enormous value.

There are other parts where explicit, deterministic policy is more appropriate.

The engineering task is to know the difference.

---

# 47. The Most Important Product Lesson

System boundaries should not only exist in source code.

Users should be able to understand them.

That is why the interface explicitly distinguishes:

```text
RULE ENGINE
```

from:

```text
AI EXPLANATION
```

A technically sound boundary becomes more useful when the product experience communicates it.

---

# 48. The Most Important AI Architecture Lesson

More autonomy is not necessarily more sophisticated architecture.

Sometimes sophisticated architecture means recognizing that:

```text
a rules engine is enough
```

or that:

```text
an LLM should assist rather than act
```

or that:

```text
an agent should investigate but not authorize
```

or that:

```text
the workflow should remain human-controlled
```

Choosing the correct boundary is part of building AI well.

---

# 49. What This Build Demonstrates About My Work

GSB-002 brings together several parts of how I want to work with AI.

## I can think beyond the model

The project treats the LLM as one component inside a larger system rather than as the entire application.

---

## I can translate business workflows into architecture

The workflow characteristics connect operational reality to technical decisions.

---

## I can implement the architecture

The project includes:

```text
Python

FastAPI

Pydantic

React

TypeScript

REST APIs

OpenAI structured output

testing
```

---

## I can reason about AI governance

The system explicitly models:

```text
risk

data sensitivity

human approval

authority boundaries

graceful degradation
```

---

## I can design the product around the architecture

The interface does not hide where the recommendation comes from.

The UX reinforces the system model.

---

## I can explain the system

The repository includes:

```text
architecture documentation

engineering evaluation

build ledger

README

case study
```

The goal is not only to make the software work.

It is to make the reasoning understandable.

---

# 50. Why I Built This as a Gradensal Signature Build

Gradensal is my environment for exploring practical AI systems, intelligent automation, and software around real business operations.

The Signature Build format lets me take one architecture problem and carry it through:

```text
problem framing

technical architecture

implementation

testing

product design

documentation

public explanation
```

GSB-002 is therefore both:

```text
a working prototype
```

and:

```text
a documented architecture investigation
```

---

# 51. Final Architecture Principle

The project ultimately reduced to one principle:

> **Use the least autonomous architecture that can responsibly accomplish the work.**

That may mean:

```text
DETERMINISTIC SOFTWARE
```

when the rules are known.

It may mean:

```text
LLM ASSISTANCE
```

when interpretation adds value.

It may mean:

```text
A BOUNDED AGENT
```

when adaptive tool use is genuinely necessary.

And sometimes it means:

```text
KEEP THE HUMAN
```

when the consequences demand explicit human authority.

---

# 52. Result

GSB-002 became a complete working prototype that:

```text
evaluates workflow characteristics
        ↓
selects an architecture deterministically
        ↓
applies risk and governance boundaries
        ↓
identifies human approval requirements
        ↓
uses AI to explain the decision
        ↓
survives AI-provider failure
        ↓
presents the boundaries clearly in the UI
```

The final automated backend baseline is:

```text
41 passing tests
```

The production frontend builds successfully.

Responsive and keyboard QA passed.

The complete React → FastAPI → deterministic engine → AI explanation → React workflow has been exercised successfully.

---

# 53. Closing Thought

The question that started this project was:

> Where should AI go in this workflow?

The better question turned out to be:

> **Where should AI be allowed to decide?**

That is the question GSB-002 is designed to make visible.

---

## Project

**Marketing AI Workflow Architect**

Gradensal Signature Build **GSB-002**

---

## Built by

**Lissette Gorrin Rodriguez**

**AI Builder × Storyteller**

Gradensal  
Toronto, Canada