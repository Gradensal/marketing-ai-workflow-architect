from fastapi import FastAPI

from backend.app.api import (
    analysis_router,
    assessment_router,
    health_router,
)


app = FastAPI(
    title="Marketing AI Workflow Architect",
    summary=(
        "Decision support for selecting appropriate levels "
        "of AI automation."
    ),
    description=(
        "GSB-002 is a Gradensal Signature Build that evaluates "
        "business workflow characteristics and recommends "
        "deterministic automation, LLM assistance, agentic AI, "
        "or human-first redesign."
    ),
    version="0.1.0",
)


app.include_router(health_router)
app.include_router(assessment_router)
app.include_router(analysis_router)