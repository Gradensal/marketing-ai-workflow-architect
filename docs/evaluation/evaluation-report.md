# GSB-002 - Marketing AI Workflow Architect

## Engineering Evaluation Report

**Project:** Gradensal Signature Build GSB-002  
**Product:** Marketing AI Workflow Architect  
**Author:** Lissette Gorrin Rodriguez  
**Organization:** Gradensal  

---

# 1. Evaluation Purpose

The purpose of this evaluation is to determine whether GSB-002 behaves consistently with its intended architecture.

The system is designed around a core authority boundary:

> **The deterministic rules engine chooses the architecture recommendation. The generative AI layer explains that recommendation.**

The evaluation therefore does not focus only on whether the application can call an LLM.

It evaluates whether:

1. workflow inputs are validated;
2. the deterministic decision engine returns the intended architecture families;
3. high-risk conditions can override otherwise agentic characteristics;
4. human-approval rules remain independent from architecture selection;
5. the LLM explanation layer cannot replace the authoritative assessment;
6. AI-provider failure does not destroy the deterministic result;
7. the combined API returns structured output;
8. the React frontend correctly handles success and failure states;
9. the interface remains usable across common viewport sizes;
10. the complete application can run end-to-end.

---

# 2. Evaluation Scope

The evaluation covers:

- Pydantic domain models;
- deterministic decision rules;
- architecture authority boundaries;
- FastAPI endpoints;
- structured AI explanation models;
- dependency-injected AI explanation behavior;
- graceful degradation;
- React production compilation;
- browser-based workflow analysis;
- responsive behavior;
- keyboard interaction;
- frontend validation;
- request-state handling.

The evaluation does not attempt to prove that the current prototype is ready for unrestricted production use.

Production deployment would require additional organization-specific work related to:

- authentication;
- authorization;
- telemetry;
- rate limiting;
- secrets management;
- privacy review;
- security review;
- legal review;
- compliance review;
- production monitoring;
- model-cost controls;
- application hosting;
- operational support.

---

# 3. Test Strategy

GSB-002 uses multiple forms of evaluation.

```text
Domain validation
        ↓
Unit tests
        ↓
Decision-engine tests
        ↓
Authority-boundary tests
        ↓
API tests
        ↓
AI resilience tests
        ↓
Deterministic scenario demo
        ↓
Live end-to-end browser test
        ↓
Manual responsive + accessibility QA
```

This layered strategy is intentional.

A browser demo alone would not prove the policy layer is correct.

Unit tests alone would not prove the product works end-to-end.

The project therefore combines deterministic automated evaluation with controlled manual integration testing.

---

# 4. Automated Test Baseline

At the completion of the product-hardening phase, the backend automated test suite contains:

```text
41 passing tests
```

The verified command is:

```bash
python3 -m pytest backend/tests -q
```

Verified result:

```text
......................................... [100%]
41 passed
```

The automated suite completes without requiring live OpenAI API calls.

AI-dependent tests use controlled test doubles or injected explanation generators where appropriate.

This allows the deterministic behavior and resilience logic to be tested repeatedly without unnecessary API cost or external-provider dependency.

---

# 5. Domain Model Evaluation

## 5.1 Workflow Input Validation

`WorkflowInput` validates the business workflow submitted to the architecture engine.

The model includes:

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

Architecture signals are constrained to:

```text
1 through 5
```

The model also applies minimum and maximum lengths to descriptive fields and rejects unexpected fields.

This prevents malformed workflow data from silently reaching the decision engine.

---

## 5.2 Architecture Assessment Validation

The deterministic result is represented by `ArchitectureAssessment`.

It validates:

- architecture recommendation;
- risk level;
- decision strength;
- human-approval requirement;
- human-approval reason;
- rationale;
- warnings.

If human approval is required, a reason must also be present.

This prevents the system from returning an approval requirement without an explanation.

---

## 5.3 Structured AI Explanation Validation

The LLM explanation is validated against `WorkflowExplanation`.

The response requires six structured fields:

1. `why_this_approach`
2. `why_not_more_autonomy`
3. `proposed_architecture`
4. `human_checkpoint`
5. `first_experiment`
6. `success_metric`

The frontend therefore does not depend on arbitrary prose formatting.

It receives a predictable structured response.

---

# 6. Canonical Architecture Scenarios

The deterministic demo exercises one representative workflow for each architecture family.

Run with:

```bash
python3 -m scripts.run_decision_demo
```

The demo does not require a live LLM call.

---

## Scenario 1 — Weekly Campaign Reporting

### Characteristics

Representative profile:

- highly repeatable;
- low ambiguity;
- limited external action;
- low business risk.

### Expected Recommendation

```text
DETERMINISTIC AUTOMATION
```

### Verified Result

```text
Recommendation      DETERMINISTIC AUTOMATION
Risk                LOW
Decision strength   5/5
Human approval      NO
```

### Interpretation

The workflow does not require AI simply because AI is available.

Explicit deterministic software rules provide the more appropriate architecture.

---

## Scenario 2 — Campaign Message Drafting

### Characteristics

Representative profile:

- moderate repeatability;
- meaningful interpretation or generation;
- limited external action;
- low business risk.

### Expected Recommendation

```text
LLM ASSISTED WORKFLOW
```

### Verified Result

```text
Recommendation      LLM ASSISTED WORKFLOW
Risk                LOW
Decision strength   4/5
Human approval      NO
```

### Interpretation

Generative assistance is useful, but autonomous execution is not justified.

The LLM supports the marketer while the workflow structure and final authority remain explicit.

---

## Scenario 3 — Campaign Anomaly Investigation

### Characteristics

Representative profile:

- substantial ambiguity;
- multiple tools or information sources;
- meaningful adaptive investigation;
- bounded business risk.

### Expected Recommendation

```text
AGENTIC WORKFLOW
```

### Verified Result

```text
Recommendation      AGENTIC WORKFLOW
Risk                MEDIUM
Decision strength   4/5
Human approval      YES
```

### Interpretation

The workflow requires more than simple generation.

It benefits from tool use, interpretation, and adaptive intermediate behavior.

However, the agentic recommendation does not remove the human-governance requirement.

---

## Scenario 4 — Autonomous Customer Pricing

### Characteristics

Representative profile:

- consequential external action;
- elevated business risk;
- high autonomy would affect external outcomes.

### Expected Recommendation

```text
KEEP HUMAN / REDESIGN FIRST
```

### Verified Result

```text
Recommendation      KEEP HUMAN REDESIGN FIRST
Risk                HIGH
Decision strength   5/5
Human approval      YES
```

### Interpretation

The system does not interpret high automation potential as a reason to maximize autonomy.

Risk overrides the autonomy opportunity.

The workflow should first be redesigned around explicit human control.

---

# 7. Canonical Scenario Matrix

| Workflow | Recommendation | Risk | Strength | Human Approval |
|---|---|---|---:|---|
| Weekly campaign reporting | Deterministic automation | Low | 5/5 | No |
| Campaign message drafting | LLM-assisted workflow | Low | 4/5 | No |
| Campaign anomaly investigation | Agentic workflow | Medium | 4/5 | Yes |
| Autonomous customer pricing | Keep human / redesign first | High | 5/5 | Yes |

The four scenarios exercise all four architecture families.

---

# 8. Authority-Boundary Evaluation

A core design requirement is that agent-like characteristics must not automatically produce an agentic recommendation.

Dedicated authority-boundary tests were created to evaluate this behavior.

The test file verifies four important conditions.

---

## 8.1 High Risk Overrides Agentic Characteristics

A workflow can have:

```text
ambiguity           5
tool use            5
external actions    5
business risk       5
```

This resembles a strong candidate for an autonomous agent if only capability requirements are considered.

However, the expected recommendation is:

```text
KEEP HUMAN / REDESIGN FIRST
```

The test verifies that elevated business risk and consequential external action override otherwise agentic characteristics.

---

## 8.2 Extreme Data Sensitivity Can Block Autonomy

A workflow with:

- high ambiguity;
- high tool use;
- meaningful external action;
- extremely sensitive data

is expected to return:

```text
KEEP HUMAN / REDESIGN FIRST
```

The evaluation verifies that data sensitivity acts as an architecture constraint rather than merely an informational label.

---

## 8.3 Tool Count Alone Does Not Create an Agent

A workflow can depend on many systems without requiring agentic behavior.

A dedicated test verifies that:

```text
high tool use
```

by itself does not imply:

```text
AGENTIC WORKFLOW
```

This protects the engine from a common architectural mistake:

> confusing integration complexity with autonomous decision-making.

---

## 8.4 Agentic Architecture Requires Bounded Risk

The evaluation also verifies a workflow where:

- ambiguity is high;
- tool use is high;
- external action is meaningful;
- business risk remains bounded;
- data sensitivity remains bounded.

Expected:

```text
AGENTIC WORKFLOW
```

This confirms that the governance boundary does not simply block agentic systems.

It permits agentic architecture when the workflow characteristics justify it and the risk profile remains within the defined prototype boundary.

---

# 9. Human Approval Evaluation

Architecture selection and human approval are intentionally separate.

For example:

```text
AGENTIC WORKFLOW
```

can coexist with:

```text
Human approval required
```

This distinction is important.

Agentic architecture describes the system's ability to:

- interpret;
- select tools;
- adapt;
- perform intermediate actions.

It does not imply permission to perform every consequential final action without human review.

The evaluation confirms that meaningful risk can trigger a human checkpoint even when agentic architecture is selected.

---

# 10. AI Authority Evaluation

The AI explanation layer receives the deterministic assessment after the decision has already been made.

The explanation service is instructed not to change:

- recommendation;
- risk;
- approval requirement;
- deterministic rationale.

The generative layer provides interpretation and communication rather than policy authority.

Conceptually:

```text
RULE ENGINE
    ↓
DECIDES

LLM
    ↓
EXPLAINS
```

This is a central evaluation target because the product is intended to demonstrate controlled AI integration rather than delegated policy.

---

# 11. AI Failure Resilience

Dedicated resilience tests simulate AI explanation failure.

The important expected behavior is:

```text
Deterministic decision succeeds
        ↓
AI explanation fails
        ↓
HTTP response remains valid
        ↓
Deterministic assessment is preserved
```

The response reports:

```text
explanation_status = unavailable
```

and:

```text
explanation = null
```

while preserving:

- recommendation;
- risk;
- decision strength;
- approval requirement;
- rationale;
- warnings.

---

# 12. AI Failure Test Result

A simulated explanation-provider failure verifies that:

```text
HTTP status             200
Architecture assessment preserved
AI explanation          unavailable
User-facing message     present
```

The response explains that:

- the architecture assessment completed successfully;
- the AI explanation is temporarily unavailable;
- the deterministic recommendation remains valid.

This is graceful degradation rather than total application failure.

---

# 13. API Evaluation

The FastAPI application exposes:

```text
/health
/api/v1/assess
/api/v1/analyze
```

The public path set was verified through the application's generated OpenAPI schema.

---

## 13.1 Health Endpoint

Purpose:

- confirm API availability;
- expose basic service/version information.

---

## 13.2 Deterministic Assessment Endpoint

```text
POST /api/v1/assess
```

Purpose:

- validate workflow input;
- execute the deterministic architecture engine;
- return `ArchitectureAssessment`.

This endpoint does not require the LLM explanation layer.

---

## 13.3 Combined Analysis Endpoint

```text
POST /api/v1/analyze
```

Purpose:

1. validate workflow input;
2. perform deterministic assessment;
3. attempt AI explanation;
4. return structured `WorkflowAnalysis`.

The endpoint preserves the deterministic result if the explanation service fails.

---

# 14. Live End-to-End Integration Test

A complete browser-based workflow was successfully executed through:

```text
React
  ↓
FastAPI
  ↓
Pydantic
  ↓
Deterministic Decision Engine
  ↓
Structured AI Explanation
  ↓
FastAPI Response
  ↓
React Results UI
```

The backend recorded:

```text
OPTIONS /api/v1/analyze 200 OK
POST /api/v1/analyze    200 OK
```

This confirms successful cross-origin frontend/backend communication during development.

---

# 15. Live High-Risk Result

A live workflow with approximately:

```text
Repeatability       4/5
Ambiguity           2/5
Tool use            4/5
External actions    4/5
Business risk       5/5
Data sensitivity    5/5
```

returned:

```text
KEEP HUMAN / REDESIGN FIRST

Risk
HIGH

Decision strength
5/5

Human approval
Required
```

The browser displayed:

- deterministic recommendation;
- risk;
- decision strength;
- approval requirement;
- approval reason;
- deterministic rationale;
- guardrails;
- AI explanation.

This demonstrated the complete product loop.

---

# 16. Frontend Build Evaluation

The frontend was repeatedly compiled during development using:

```bash
npm run build
```

The final Milestone 10 build completed successfully using:

```text
React             19.3.0
React DOM         19.3.0
Vite              8.3.1
@vitejs/plugin-react 6.1.1
```

The production build completed without TypeScript errors.

The final tested build transformed:

```text
25 modules
```

and successfully generated production assets.

---

# 17. Frontend Failure-State Evaluation

The React frontend distinguishes multiple runtime states.

---

## 17.1 Initial State

The interface displays:

```text
Awaiting workflow
```

before analysis begins.

---

## 17.2 Loading State

During analysis:

- form controls are disabled;
- sliders are disabled;
- the submit button changes state;
- duplicate submission is prevented;
- the results panel displays analysis progress.

This reduces accidental repeated API calls.

---

## 17.3 API Connectivity Failure

With FastAPI intentionally stopped, the frontend was manually tested.

Expected behavior:

- application remains rendered;
- workflow data remains in the browser;
- user receives a controlled error;
- the application does not silently fail.

Manual QA confirmed this behavior.

---

## 17.4 AI Explanation Failure

Automated backend evaluation verifies the graceful-degradation contract.

The frontend contains a dedicated presentation state for:

```text
AI EXPLANATION
UNAVAILABLE
```

while continuing to display the deterministic assessment.

---

# 18. Responsive Evaluation

Manual responsive QA was completed at representative viewport sizes.

---

## Desktop

Approximate target:

```text
1440px+
```

Verified:

- two-column workflow/analysis layout;
- complete Gradensal hero treatment;
- desktop navigation metadata;
- sticky analysis behavior;
- footer layout;
- no unexpected horizontal scrolling.

---

## Laptop

Approximate target:

```text
1100px
```

Verified:

- two-column layout remains usable;
- inputs remain readable;
- sliders remain usable;
- result cards do not overflow.

---

## Tablet

Approximate target:

```text
768 × 1024
```

Verified:

- workflow and analysis panels stack;
- hero switches to single-column composition;
- inputs expand to available width;
- footer adapts correctly;
- no horizontal scrolling.

---

## Mobile

Approximate target:

```text
390 × 844
```

Verified:

- system-status text is reduced appropriately;
- hero composition remains readable;
- workflow panel uses full width;
- touch targets remain usable;
- intermediate score markers are removed where space is constrained;
- analysis content stacks correctly;
- footer becomes vertical;
- no unexpected horizontal scrolling.

---

# 19. Keyboard Accessibility Evaluation

Manual keyboard navigation was completed.

The application allows keyboard focus through:

- Load example;
- Reset;
- workflow name;
- team;
- description;
- all architecture sliders;
- human approval checkbox;
- Analyze workflow.

Sliders support keyboard adjustment.

The checkbox supports keyboard toggling.

Visible focus treatment is provided for interactive elements.

---

# 20. Frontend Validation Evaluation

The frontend prevents submission until minimum descriptive requirements are met.

Representative minimum constraints include:

```text
Workflow name       at least 3 characters
Team                at least 2 characters
Description         at least 20 characters
```

This provides immediate user feedback before backend validation.

Backend validation remains authoritative.

---

# 21. Double-Submission Evaluation

During an active analysis request:

- text fields are disabled;
- textarea is disabled;
- score sliders are disabled;
- approval checkbox is disabled;
- Load example is disabled;
- Reset is disabled;
- Analyze workflow is disabled.

This prevents accidental duplicate analysis requests while a request is in progress.

---

# 22. Brand and Product QA

The frontend establishes the initial Gradensal product design system.

Key characteristics include:

- near-black page surface;
- deep navy application panels;
- cobalt and electric-blue accents;
- cyan system indicators;
- frost-white primary typography;
- restrained glass-like surfaces;
- Gradensal chrome-blue sculptural mark.

The approved logo master is preserved separately from the optimized frontend asset.

---

# 23. Asset Optimization

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
approximately 843 KB source file
```

The production bundle reported the optimized logo asset at approximately:

```text
862.80 kB
```

The optimization reduced delivery size while preserving the approved master asset.

---

# 24. Browser-Level Product QA

The frontend includes:

- Gradensal favicon;
- descriptive page title;
- theme metadata;
- application description metadata;
- Open Graph title and description;
- product/build identification;
- Gradensal footer;
- prototype version information.

The browser title is:

```text
Marketing AI Workflow Architect | Gradensal
```

---

# 25. Current Evidence Summary

| Evaluation Area | Status |
|---|---|
| Domain validation | Pass |
| Four architecture families | Pass |
| Risk override | Pass |
| Data-sensitivity override | Pass |
| Tool-count boundary | Pass |
| Agentic bounded-risk case | Pass |
| Human approval logic | Pass |
| AI structured output | Pass |
| AI failure resilience | Pass |
| API endpoints | Pass |
| Combined browser workflow | Pass |
| FastAPI CORS integration | Pass |
| Frontend production compilation | Pass |
| Desktop responsive QA | Pass |
| Laptop responsive QA | Pass |
| Tablet responsive QA | Pass |
| Mobile responsive QA | Pass |
| Keyboard navigation | Pass |
| Slider keyboard control | Pass |
| Frontend validation | Pass |
| Double-submit prevention | Pass |
| API-down UX | Pass |
| Logo optimization | Pass |

---

# 26. What the Evaluation Supports

The current evidence supports the following statements about the prototype:

### The architecture engine is deterministic

The same workflow characteristics produce the same architecture decision.

---

### The system does not automatically maximize AI autonomy

The engine can select:

- deterministic automation;
- LLM assistance;
- agentic execution;
- human-first redesign.

---

### Governance can override capability

A workflow that looks technically suitable for an agent can still be rejected for autonomous execution when risk exceeds the prototype's defined boundary.

---

### Human approval and architecture type are separate

An agentic workflow can still require explicit human approval.

---

### The LLM is not the architecture authority

The recommendation is produced before the generative explanation begins.

---

### AI-provider failure does not invalidate the deterministic result

The application can return a valid architecture assessment even when the explanation service is unavailable.

---

### The prototype operates end-to-end

The complete browser-to-backend-to-AI-to-browser loop has been manually executed successfully.

---

# 27. What the Evaluation Does Not Support

The current evaluation does not prove:

- production security readiness;
- regulatory compliance;
- enterprise-scale performance;
- model behavior across every possible workflow;
- suitability for fully autonomous high-impact decisions;
- universal correctness of the scoring policy;
- production reliability of the external AI provider;
- suitability as a replacement for human risk, privacy, legal, security, or compliance review.

The decision rules are prototype policy logic intended to demonstrate architecture selection and governance design.

They should be reviewed and adapted before organization-specific production use.

---

# 28. Known Prototype Limitations

The current prototype does not yet include:

- persistent workflow storage;
- user accounts;
- authentication;
- authorization;
- organization-specific policy configuration;
- production telemetry;
- production deployment infrastructure;
- cost dashboards;
- usage quotas;
- audit-history persistence;
- workflow version history;
- administrative policy management.

These omissions are deliberate for the current Signature Build scope.

---

# 29. Evaluation Conclusion

GSB-002 demonstrates that an AI-enabled product can separate:

```text
policy
from
generation
```

and:

```text
decision authority
from
natural-language explanation.
```

The evaluation confirms that the prototype:

- exercises four architecture families;
- enforces risk-based authority boundaries;
- preserves explicit human governance;
- validates structured inputs and outputs;
- handles AI-provider failure gracefully;
- operates through a complete browser-based application;
- remains usable across desktop, tablet, and mobile layouts;
- passes 41 automated backend tests.

The central engineering result is not that the project uses an LLM.

It is that the project defines **where the LLM is allowed to matter and where it is not**.

---

# 30. Final Evaluation Principle

> **Use AI where interpretation creates value. Use deterministic software where rules are sufficient. Use bounded agents where adaptive tool use is justified. Keep humans in control when the consequences demand it.**