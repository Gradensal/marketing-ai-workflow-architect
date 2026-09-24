from backend.app.api.assessment import router as assessment_router
from backend.app.api.health import router as health_router


__all__ = [
    "assessment_router",
    "health_router",
]