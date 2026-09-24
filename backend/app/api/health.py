from fastapi import APIRouter


router = APIRouter(
    tags=["System"],
)


@router.get(
    "/health",
    summary="Check API health",
)
def health_check() -> dict[str, str]:
    """
    Return a lightweight service health response.
    """

    return {
        "status": "ok",
        "service": "marketing-ai-workflow-architect",
        "version": "0.1.0",
    }