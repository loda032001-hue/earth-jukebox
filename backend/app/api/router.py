"""Enrutador principal de la API."""

from fastapi import APIRouter

from app.api.health import router as health_router
from app.api.sounds import router as sounds_router
from app.api.geography import router as geo_router
from app.api.scientific import router as scientific_router
from app.api.auth import router as auth_router
from app.api.favorites import router as favorites_router
from app.api.compositions import router as compositions_router
from app.api.compare import router as compare_router

api_router = APIRouter(prefix="/api")
api_router.include_router(health_router)
api_router.include_router(sounds_router)
api_router.include_router(geo_router)
api_router.include_router(scientific_router)
api_router.include_router(compare_router)
api_router.include_router(auth_router)
api_router.include_router(favorites_router)
api_router.include_router(compositions_router)
