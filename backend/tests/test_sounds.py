"""Pruebas del catálogo de sonidos."""

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_categories() -> None:
    r = client.get("/api/sounds/categories")
    assert r.status_code == 200
    data = r.json()
    assert len(data) >= 10
    assert any(c["slug"] == "rain" for c in data)


def test_sounds_list() -> None:
    r = client.get("/api/sounds")
    assert r.status_code == 200
    body = r.json()
    assert body["total"] >= 1
    assert len(body["items"]) == body["total"]


def test_sound_detail_404() -> None:
    r = client.get("/api/sounds/does-not-exist")
    assert r.status_code == 404


def test_sound_filter_category() -> None:
    r = client.get("/api/sounds?category=rain")
    assert r.status_code == 200
    body = r.json()
    assert all(s["category"] == "rain" for s in body["items"])