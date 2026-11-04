"""Adaptador para la API de NASA POWER (Daily, punto)."""

from typing import Any

import httpx

from app.schemas.scientific import NasaPowerRequest, NasaPowerResponse

BASE_URL = "https://power.larc.nasa.gov/api"
FILL_VALUE = -999.0


import asyncio

from app.core.cache import nasa_power_cache

_locks: dict[str, asyncio.Lock] = {}


def _cache_key(req: NasaPowerRequest) -> str:
    return f"{req.latitude},{req.longitude},{','.join(sorted(req.parameters))},{req.start},{req.end},{req.community}"


async def fetch_daily(req: NasaPowerRequest) -> NasaPowerResponse:
    """Obtiene datos diarios de NASA POWER para un punto (con caché)."""
    key = _cache_key(req)
    cached = nasa_power_cache.get(key)
    if cached is not None:
        return cached

    lock = _locks.setdefault(key, asyncio.Lock())
    async with lock:
        # Re-check after acquiring lock
        cached = nasa_power_cache.get(key)
        if cached is not None:
            return cached

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

        cleaned: dict[str, dict[str, float | None]] = {}
        for p in req.parameters:
            series = param_data.get(p, {})
            cleaned[p] = {}
            for date, value in series.items():
                if value is None or (isinstance(value, (int, float)) and value <= FILL_VALUE + 1):
                    cleaned[p][date] = None
                else:
                    cleaned[p][date] = float(value)

        result = NasaPowerResponse(
            latitude=req.latitude,
            longitude=req.longitude,
            parameters=cleaned,
            units=units,
            start=header.get("start", req.start),
            end=header.get("end", req.end),
            source="NASA POWER (Daily, Point)",
            messages=messages,
        )
        nasa_power_cache.set(key, result)
        return result
