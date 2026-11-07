"""Pruebas de paginación del catálogo."""

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_pagination_limit() -> None:
    r = client.get("/api/sounds?limit=1&offset=0")
    assert r.status_code == 200
    body = r.json()
    assert len(body["items"]) <= 1
    assert body["total"] >= len(body["items"])