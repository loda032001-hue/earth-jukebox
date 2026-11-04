"""Esquemas de sonidos naturales."""

from pydantic import BaseModel


class SoundCategory(BaseModel):
    slug: str
    name: str
    description: str | None = None


class NaturalSound(BaseModel):
    id: str
    name: str
    category: str
    description: str | None = None
    image_url: str | None = None
    audio_url: str | None = None
    duration_seconds: int | None = None
    country: str | None = None
    region: str | None = None
    continent: str | None = None
    ecosystem: str | None = None
    location_precision: str | None = None
    coordinate_source: str | None = None
    latitude: float | None = None
    longitude: float | None = None
    recorded_at: str | None = None
    author: str | None = None
    source: str | None = None
    license: str | None = None
    scientific_info: str | None = None
    tags: list[str] = []


class SoundListResponse(BaseModel):
    items: list[NaturalSound]
    total: int


class GeoSound(NaturalSound):
    pass


class GeoSearchResponse(BaseModel):
    center: dict
    radius_km: float
    items: list[NaturalSound]
    total: int
