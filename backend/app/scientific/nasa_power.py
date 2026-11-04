"""Adaptador para la API de NASA POWER (Daily, punto)."""

from typing import Any

import httpx

from app.schemas.scientific import NasaPowerRequest, NasaPowerResponse

BASE_URL = "https://power.larc.nasa.gov/api"
FILL_VALUE = -999.0


async def fetch_daily(req: NasaPowerRequest) -> NasaPowerResponse:
    """Obtiene datos diarios de NASA POWER para un punto."""
    params_str = ",".join(req.parameters)
    url = (
        f"{BASE_URL}/temporal/daily/point"
        f"?parameters={params_str}&community={req.community}"
        f"&longitude={req.longitude}&latitude={req.latitude}"
        f"&start={req.start}&end={req.end}&format=JSON"
    )
    async with httpx.AsyncClient(timeout=30.0) as client:
        response = await client.get(url)
        response.raise_for_status()
        data: dict[str, Any] = response.json()

    props = data.get("properties", {})
    param_data = props.get("parameter", {})
    header = data.get("header", {})
    messages = data.get("messages", []) or []

    units = {}
    for p in req.parameters:
        meta = data.get("parameters", {}).get(p, {})
        units[p] = meta.get("units", "")

    # Limpiar valores fill (-999) -> None
    cleaned: dict[str, dict[str, float | None]] = {}
    for p in req.parameters:
        series = param_data.get(p, {})
        cleaned[p] = {}
        for date, value in series.items():
            if value is None or (isinstance(value, (int, float)) and value <= FILL_VALUE + 1):
                cleaned[p][date] = None
            else:
                cleaned[p][date] = float(value)

    return NasaPowerResponse(
        latitude=req.latitude,
        longitude=req.longitude,
        parameters=cleaned,
        units=units,
        start=header.get("start", req.start),
        end=header.get("end", req.end),
        source="NASA POWER (Daily, Point)",
        messages=messages,
    )
