"""Validación de registros para ingesta de sonidos."""

REQUIRED_FIELDS = ["name", "audio_url", "license", "source"]
VALID_PRECISION = {"exact", "approximate", "region", "unconfirmed"}


def validate(record: dict) -> tuple[bool, str]:
    for field in REQUIRED_FIELDS:
        if not record.get(field):
            return False, f"Falta campo obligatorio: {field}"

    precision = record.get("location_precision", "unconfirmed")
    if precision not in VALID_PRECISION:
        return False, f"location_precision inválida: {precision}"

    lat = record.get("latitude")
    lon = record.get("longitude")
    if lat is not None or lon is not None:
        if lat is None or lon is None:
            return False, "Coordenadas incompletas (lat/lon)"
        if not record.get("coordinate_source"):
            return False, "coordinate_source requerido si hay coordenadas"
        if precision == "unconfirmed":
            return False, "No se pueden tener coordenadas con precisión 'unconfirmed'"

    if precision in ("exact", "approximate") and (lat is None or lon is None):
        return False, f"Precisión '{precision}' requiere coordenadas"

    return True, "ok"