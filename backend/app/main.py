from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.app.api import (
    analysis_router,
    assessment_router,
    health_router,
)


app = FastAPI(
    title="Marketing AI Workflow Architect",
    summary=(
        "Decision support for selecting the appropriate "
        "level of AI automation for a business workflow."
    ),
    description=(
        "GSB-002 is a Gradensal Signature Build that evaluates "
        "workflow characteristics and recommends deterministic "
        "automation, LLM assistance, agentic AI, or human-first "
        "redesign."
    ),
    version="0.1.0",
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=False,
    allow_methods=[
        "GET",
        "POST",
    ],
    allow_headers=[
        "Content-Type",
    ],
)


app.include_router(health_router)
app.include_router(assessment_router)
app.include_router(analysis_router)