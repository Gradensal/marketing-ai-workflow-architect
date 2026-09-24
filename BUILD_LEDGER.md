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
- Pydantic: pending environment verification

---

# Build Progress

## Milestone 0 — Environment Audit

Status: Complete

Verified the development environment and compared it with the previous
Gradensal Signature Build.

## Milestone 1 — Project Foundation

Status: In Progress

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