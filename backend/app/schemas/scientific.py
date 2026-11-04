"""Esquemas científicos y de sonificación."""

from pydantic import BaseModel


class NasaPowerRequest(BaseModel):
    latitude: float
    longitude: float
    parameters: list[str]
    start: str
    end: str
    community: str = "SB"


class NasaPowerResponse(BaseModel):
    latitude: float
    longitude: float
    parameters: dict
    units: dict
    start: str
    end: str
    source: str
    messages: list[str] = []


class SonificationRule(BaseModel):
    variable: str
    musical_parameter: str
    description: str


class SonificationResponse(BaseModel):
    latitude: float
    longitude: float
    start: str
    end: str
    rules: list[SonificationRule]
    series: dict
    normalized: dict
    note: str
