# Marketing AI Workflow Architect

**GSB-002 - Gradensal Signature Build**

A decision-support prototype for reasoning about whether a business workflow
should use deterministic automation, LLM assistance, agentic AI, or remain
human-controlled.

> The important AI architecture question is not always “Which agent should we
> build?” Sometimes it is “Should this workflow use an agent at all?”

## Status

In active development.

## Problem

Teams adopting AI can introduce unnecessary complexity when they treat every
workflow as an agent problem.

This project explores a more deliberate approach by evaluating characteristics
such as:

- repeatability;
- ambiguity and judgment;
- tool requirements;
- external actions;
- business risk;
- data sensitivity;
- human approval requirements.

## Planned Recommendations

The prototype will classify workflows into one of four categories:

1. **Deterministic Automation**
2. **LLM-Assisted Workflow**
3. **Agentic Workflow**
4. **Keep Human / Redesign First**

## Architectural Principle

The initial architecture recommendation is produced by explicit,
testable software logic.

An LLM may later help explain the result in clear stakeholder language, but it
does not have sole authority over the architecture decision.

## Technology

Planned stack:

- Python
- FastAPI
- Pydantic
- OpenAI Responses API
- React
- Vite
- pytest

## Repository Structure

```text
backend/       API, domain logic, services and tests
frontend/      React application
docs/          Architecture and decision records
research/      Supporting source material
assets/        Screenshots, diagrams and demos
case-study/    Gradensal Signature Build case study
```

## Disclaimer

This is a portfolio and research prototype.

It is not a validated enterprise AI-governance framework and should not be used
as the sole basis for production architecture, security, privacy, financial,
legal, or operational decisions.