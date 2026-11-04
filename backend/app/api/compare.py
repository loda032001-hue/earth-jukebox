"""Comparación científica entre dos periodos/ubicaciones."""

from fastapi import APIRouter, HTTPException, Query

from app.scientific.nasa_power import fetch_daily
from app.schemas.scientific import NasaPowerRequest

router = APIRouter(prefix="/compare", tags=["compare"])


def stats(values: list[float]) -> dict:
    if not values:
        return {"count": 0, "mean": None, "min": None, "max": None}
    return {
        "count": len(values),
        "mean": sum(values) / len(values),
        "min": min(values),
        "max": max(values),
    }


@router.get("")
async def compare(
    lat1: float = Query(...),
    lon1: float = Query(...),
    start1: str = Query(...),
    end1: str = Query(...),
    lat2: float = Query(...),
    lon2: float = Query(...),
    start2: str = Query(...),
    end2: str = Query(...),
    parameter: str = Query(default="T2M"),
) -> dict:
    try:
        d1 = await fetch_daily(NasaPowerRequest(latitude=lat1, longitude=lon1, parameters=[parameter], start=start1, end=end1))
        d2 = await fetch_daily(NasaPowerRequest(latitude=lat2, longitude=lon2, parameters=[parameter], start=start2, end=end2))
    except Exception as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc

    vals1 = [v for v in d1.parameters.get(parameter, {}).values() if v is not None]
    vals2 = [v for v in d2.parameters.get(parameter, {}).values() if v is not None]

    s1 = stats(vals1)
    s2 = stats(vals2)
    diff_mean = None
    if s1["mean"] is not None and s2["mean"] is not None:
        diff_mean = s2["mean"] - s1["mean"]

    return {
        "parameter": parameter,
        "series1": {"location": {"latitude": lat1, "longitude": lon1}, "period": {"start": start1, "end": end1}, "stats": s1},
        "series2": {"location": {"latitude": lat2, "longitude": lon2}, "period": {"start": start2, "end": end2}, "stats": s2},
        "difference_mean": diff_mean,
    }
