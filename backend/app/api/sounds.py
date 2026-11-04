"""Rutas del catálogo de sonidos."""

from fastapi import APIRouter, HTTPException, Query

from app.schemas.sound import NaturalSound, SoundCategory, SoundListResponse
from app.services.sound_catalog import (
    get_sound,
    list_categories,
    list_sounds,
)

router = APIRouter(prefix="/sounds", tags=["sounds"])


@router.get("/categories", response_model=list[SoundCategory])
async def categories() -> list[SoundCategory]:
    return list_categories()


@router.get("", response_model=SoundListResponse)
async def sounds(
    category: str | None = Query(default=None),
    q: str | None = Query(default=None),
) -> SoundListResponse:
    items = list_sounds(category=category, query=q)
    return SoundListResponse(items=items, total=len(items))


@router.get("/{sound_id}", response_model=NaturalSound)
async def sound_detail(sound_id: str) -> NaturalSound:
    sound = get_sound(sound_id)
    if sound is None:
        raise HTTPException(status_code=404, detail="Sonido no encontrado")
    return sound
