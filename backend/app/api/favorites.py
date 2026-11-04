"""Favoritos persistentes (Supabase)."""

from fastapi import APIRouter, HTTPException, Query

from app.core.supabase import get_supabase_client, get_service_client

router = APIRouter(prefix="/favorites", tags=["favorites"])


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
async def list_favorites(token: str = Query(...)) -> list[dict]:
    uid = _user_id(token)
    svc = get_service_client()
    if svc is None:
        raise HTTPException(status_code=503, detail="Supabase no configurado")
    try:
        res = svc.table("favorites").select("*").eq("user_id", uid).execute()
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc
    return res.data or []


@router.post("")
async def add_favorite(payload: dict) -> dict:
    token = payload.get("token")
    sound_id = payload.get("sound_id")
    if not token or not sound_id:
        raise HTTPException(status_code=400, detail="token y sound_id requeridos")
    uid = _user_id(token)
    svc = get_service_client()
    if svc is None:
        raise HTTPException(status_code=503, detail="Supabase no configurado")
    try:
        res = svc.table("favorites").insert({"user_id": uid, "sound_id": sound_id}).execute()
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc
    return {"ok": True, "data": res.data}


@router.delete("/{sound_id}")
async def remove_favorite(sound_id: str, token: str = Query(...)) -> dict:
    uid = _user_id(token)
    svc = get_service_client()
    if svc is None:
        raise HTTPException(status_code=503, detail="Supabase no configurado")
    try:
        svc.table("favorites").delete().eq("user_id", uid).eq("sound_id", sound_id).execute()
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc
    return {"ok": True}
