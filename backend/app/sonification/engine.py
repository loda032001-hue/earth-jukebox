"""Motor de sonificación (Etapa 4)."""

from app.schemas.scientific import SonificationRule


MAPPING: list[SonificationRule] = [
    SonificationRule(
        variable="T2M",
        musical_parameter="pitch (altura tonal)",
        description="Temperatura a 2m normalizada a [0,1] se asigna a altura tonal.",
    ),
    SonificationRule(
        variable="PRECTOTCORR",
        musical_parameter="amplitude/rhythm density",
        description="Precipitación normalizada controla densidad rítmica y amplitud.",
    ),
    SonificationRule(
        variable="WS10M",
        musical_parameter="modulation/tempo",
        description="Velocidad del viento normalizada controla modulación y tempo.",
    ),
]


def normalize_series(values: list[float | None]) -> list[float | None]:
    nums = [v for v in values if v is not None]
    if not nums:
        return [None for _ in values]
    lo, hi = min(nums), max(nums)
    if hi == lo:
        return [0.5 if v is not None else None for v in values]
    out: list[float | None] = []
    for v in values:
        if v is None:
            out.append(None)
        else:
            out.append((v - lo) / (hi - lo))
    return out


def sonify(parameters: dict[str, dict[str, float | None]]) -> tuple[dict, dict, list[SonificationRule]]:
    """Devuelve (series, normalized, rules) para las variables disponibles."""
    series = {}
    normalized = {}
    rules = []
    for var, dates in parameters.items():
        # ordenar por fecha
        ordered = dict(sorted(dates.items()))
        vals = list(ordered.values())
        series[var] = ordered
        normalized[var] = dict(zip(ordered.keys(), normalize_series(vals)))
        # regla si existe
        for r in MAPPING:
            if r.variable == var:
                rules.append(r)
    if not rules:
        rules = [SonificationRule(variable=v, musical_parameter="generic", description="Mapeo genérico.") for v in parameters]
    return series, normalized, rules
