"""Pruebas del motor de sonificación."""

from app.sonification.engine import normalize_series, sonify


def test_normalize_series() -> None:
    out = normalize_series([0.0, 5.0, 10.0])
    assert out == [0.0, 0.5, 1.0]


def test_normalize_series_none() -> None:
    out = normalize_series([None, 5.0, None])
    assert out[0] is None
    assert out[2] is None
    assert out[1] == 0.5


def test_sonify() -> None:
    params = {
        "T2M": {"20240101": 10.0, "20240102": 20.0},
        "PRECTOTCORR": {"20240101": 0.0, "20240102": 5.0},
    }
    series, normalized, rules = sonify(params)
    assert "T2M" in normalized
    assert len(normalized["T2M"]) == 2
    assert any(r.variable == "T2M" for r in rules)