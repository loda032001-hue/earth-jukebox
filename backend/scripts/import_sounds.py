"""Ingesta de grabaciones sonoras en Supabase (Earth Jukebox).

Uso:
  python backend/scripts/import_sounds.py --input data/sounds.json
"""

import argparse
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from dotenv import load_dotenv

load_dotenv()

from supabase import create_client

from app.services.ingest import validate


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    args = parser.parse_args()

    with open(args.input, encoding="utf-8") as f:
        records = json.load(f)

    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_SERVICE_ROLE_KEY")
    if not url or not key:
        print("ERROR: SUPABASE_URL o SUPABASE_SERVICE_ROLE_KEY no configurados")
        sys.exit(1)

    client = create_client(url, key)

    ok_count = 0
    skip_count = 0
    errors = []

    for i, rec in enumerate(records):
        valid, msg = validate(rec)
        if not valid:
            skip_count += 1
            errors.append({"index": i, "name": rec.get("name"), "reason": msg})
            print(f"[SKIP] {rec.get('name')}: {msg}")
            continue
        try:
            client.table("natural_sounds").upsert(rec).execute()
            ok_count += 1
            print(f"[OK] {rec.get('name')}")
        except Exception as exc:
            skip_count += 1
            errors.append({"index": i, "name": rec.get("name"), "reason": str(exc)})
            print(f"[ERROR] {rec.get('name')}: {exc}")

    print("\n=== RESUMEN ===")
    print(f"Insertados/actualizados: {ok_count}")
    print(f"Omitidos/errores: {skip_count}")
    if errors:
        print("Errores:")
        for e in errors:
            print(f"  - {e['name']}: {e['reason']}")

    report_path = os.path.join(os.path.dirname(__file__), "..", "import_report.json")
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump({"ok": ok_count, "skipped": skip_count, "errors": errors}, f, indent=2, ensure_ascii=False)
    print(f"Informe guardado en {report_path}")


if __name__ == "__main__":
    main()
