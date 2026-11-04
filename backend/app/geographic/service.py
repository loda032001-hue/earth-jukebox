"""Servicios geográficos (Etapa 3). Placeholder en Etapa 1."""


def haversine_km(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """Distancia Haversine en kilómetros (implementación completa en Etapa 3)."""
    import math

    r = 6371.0
    p1 = math.radians(lat1)
    p2 = math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlmb = math.radians(lon2 - lon1)
    a = math.sin(dphi / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dlmb / 2) ** 2
    return 2 * r * math.asin(math.sqrt(a))
