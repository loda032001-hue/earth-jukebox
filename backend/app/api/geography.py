"""Rutas geográficas del explorador sonoro."""

import math

from fastapi import APIRouter, Query

from app.schemas.sound import GeoSearchResponse, NaturalSound
from app.services.sound_catalog import geolocated_sounds, list_sounds
from app.geographic.service import haversine_km

router = APIRouter(prefix="/geo", tags=["geography"])


@router.get("/sounds", response_model=list[NaturalSound])
async def geo_sounds() -> list[NaturalSound]:
    """Sonidos con coordenadas verificables (para el mapa)."""
    return geolocated_sounds()


@router.get("/search", response_model=GeoSearchResponse)
async def geo_search(
    lat: float = Query(...),
    lon: float = Query(...),
    radius_km: float = Query(default=100.0, gt=0),
) -> GeoSearchResponse:
    """Búsqueda por radio alrededor de una coordenada."""
    items = []
    for s in geolocated_sounds():
        if s.latitude is None or s.longitude is None:
            continue
        d = haversine_km(lat, lon, s.latitude, s.longitude)
        if d <= radius_km:
            items.append(s)
    return GeoSearchResponse(
        center={"latitude": lat, "longitude": lon},
        radius_km=radius_km,
        items=items,
        total=len(items),
    )


@router.get("/regions/{region_name}", response_model=dict)
async def region_info(region_name: str) -> dict:
    """Información básica de una región y sus grabaciones."""
    items = [s for s in list_sounds() if (s.region or "").lower() == region_name.lower()]
    return {
        "region": region_name,
        "count": len(items),
        "sounds": [s.id for s in items],
    }
