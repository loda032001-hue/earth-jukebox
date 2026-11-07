"""Pruebas de validación de ingesta."""

from app.services.ingest import validate


def test_validate_ok() -> None:
    rec = {"name": "Test", "audio_url": "https://example.com/a.ogg", "license": "CC BY 4.0", "source": "Test"}
    assert validate(rec)[0] is True


def test_validate_missing_field() -> None:
    rec = {"name": "Test", "audio_url": "https://example.com/a.ogg", "license": "CC BY 4.0"}
    ok, msg = validate(rec)
    assert ok is False
    assert "source" in msg


def test_validate_coordinates_require_source() -> None:
    rec = {"name": "T", "audio_url": "u", "license": "L", "source": "S", "latitude": 1.0, "longitude": 2.0, "location_precision": "exact"}
    ok, msg = validate(rec)
    assert ok is False
    assert "coordinate_source" in msg


def test_validate_unconfirmed_with_coords() -> None:
    rec = {"name": "T", "audio_url": "u", "license": "L", "source": "S", "latitude": 1.0, "longitude": 2.0, "location_precision": "unconfirmed", "coordinate_source": "test"}
    ok, msg = validate(rec)
    assert ok is False