"""Composiciones guardadas (Supabase)."""

from fastapi import APIRouter, HTTPException, Query

from app.core.supabase import get_supabase_client, get_service_client

router = APIRouter(prefix="/compositions", tags=["compositions"])


def _user_id(token: str) -> str:
    client = get_supabase_client()
    if client is None:
        raise HTTPException(status_code=503, detail="Supabase no configurado")
    try:
        user = client.auth.get_user(token)
    except Exception as exc:
        raise HTTPException(status_code=401, detail=str(exc)) from exc
    if not user or not user.user:
        raise HTTPException(status_code=401, detail="Token inválido")
    return user.user.id


@router.get("")
async def list_compositions(token: str = Query(...)) -> list[dict]:
    uid = _user_id(token)
    svc = get_service_client()
    if svc is None:
        raise HTTPException(status_code=503, detail="Supabase no configurado")
    try:
        res = svc.table("compositions").select("*").eq("user_id", uid).execute()
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc
    return res.data or []


@router.post("")
async def save_composition(payload: dict) -> dict:
    token = payload.get("token")
    name = payload.get("name", "Sin nombre")
    data = payload.get("data", {})
    if not token:
        raise HTTPException(status_code=400, detail="token requerido")
    uid = _user_id(token)
    svc = get_service_client()
    if svc is None:
        raise HTTPException(status_code=503, detail="Supabase no configurado")
    try:
        res = svc.table("compositions").insert({"user_id": uid, "name": name, "data": data}).execute()
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc
    return {"ok": True, "data": res.data}
