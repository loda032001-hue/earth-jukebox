"""Rutas científicas y de sonificación."""

from fastapi import APIRouter, HTTPException, Query

from app.schemas.scientific import (
    NasaPowerRequest,
    NasaPowerResponse,
    SonificationResponse,
)
from app.scientific.nasa_power import fetch_daily
from app.sonification.engine import sonify

router = APIRouter(prefix="/scientific", tags=["scientific"])


@router.get("/nasa-power", response_model=NasaPowerResponse)
async def nasa_power(
    latitude: float = Query(...),
    longitude: float = Query(...),
    parameters: str = Query(default="T2M,PRECTOTCORR,WS10M"),
    start: str = Query(...),
    end: str = Query(...),
    community: str = Query(default="SB"),
) -> NasaPowerResponse:
    params = [p.strip() for p in parameters.split(",") if p.strip()]
    req = NasaPowerRequest(
        latitude=latitude,
        longitude=longitude,
        parameters=params,
        start=start,
        end=end,
        community=community,
    )
    try:
        return await fetch_daily(req)
    except Exception as exc:
        raise HTTPException(status_code=502, detail=f"Error al consultar NASA POWER: {exc}") from exc


@router.get("/sonify", response_model=SonificationResponse)
async def sonify_endpoint(
    latitude: float = Query(...),
    longitude: float = Query(...),
    parameters: str = Query(default="T2M,PRECTOTCORR,WS10M"),
    start: str = Query(...),
    end: str = Query(...),
) -> SonificationResponse:
    params = [p.strip() for p in parameters.split(",") if p.strip()]
    req = NasaPowerRequest(
        latitude=latitude,
        longitude=longitude,
        parameters=params,
        start=start,
        end=end,
    )
    try:
        data = await fetch_daily(req)
    except Exception as exc:
        raise HTTPException(status_code=502, detail=f"Error al consultar NASA POWER: {exc}") from exc
    series, normalized, rules = sonify(data.parameters)
    return SonificationResponse(
        latitude=latitude,
        longitude=longitude,
        start=data.start,
        end=data.end,
        rules=rules,
        series=series,
        normalized=normalized,
        note="Transformación de datos científicos en parámetros musicales. Correspondencias artísticas, no científicas universales.",
    )
