"""Pruebas de autenticación."""

import pytest
from fastapi.testclient import TestClient

from app.core.config import settings
from app.main import app

client = TestClient(app)

SUPABASE_CONFIGURED = bool(settings.supabase_url and settings.supabase_anon_key)


@pytest.mark.skipif(SUPABASE_CONFIGURED, reason="Supabase configurado: flujo cubierto por integración manual")
def test_signup_without_supabase() -> None:
    r = client.post("/api/auth/signup", json={"email": "a@b.com", "password": "123456"})
    assert r.status_code == 503


@pytest.mark.skipif(SUPABASE_CONFIGURED, reason="Supabase configurado: flujo cubierto por integración manual")
def test_favorites_without_supabase() -> None:
    r = client.get("/api/favorites?token=abc")
    assert r.status_code == 503
