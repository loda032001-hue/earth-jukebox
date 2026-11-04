"""Pruebas geográficas."""

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_geo_sounds() -> None:
    r = client.get("/api/geo/sounds")
    assert r.status_code == 200
    # Los registros iniciales no tienen coordenadas verificables
    assert isinstance(r.json(), list)


def test_geo_search() -> None:
    r = client.get("/api/geo/search?lat=0&lon=0&radius_km=100")
    assert r.status_code == 200
    body = r.json()
    assert body["radius_km"] == 100.0
    assert "items" in body