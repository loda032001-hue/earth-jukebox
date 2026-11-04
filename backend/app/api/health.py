"""Ruta de salud del servicio."""

from fastapi import APIRouter

from app.core.config import settings
from app.schemas.health import HealthResponse

router = APIRouter(tags=["health"])


@router.get("/health", response_model=HealthResponse)
async def health() -> HealthResponse:
    return HealthResponse(
        status="ok",
        service="earth-jukebox",
        version="0.1.0",
        environment=settings.app_env,
    )
