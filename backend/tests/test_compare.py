"""Pruebas de comparación (unidad)."""

from app.api.compare import stats


def test_stats() -> None:
    s = stats([1.0, 2.0, 3.0])
    assert s["count"] == 3
    assert s["mean"] == 2.0
    assert s["min"] == 1.0
    assert s["max"] == 3.0


def test_stats_empty() -> None:
    s = stats([])
    assert s["count"] == 0
    assert s["mean"] is None