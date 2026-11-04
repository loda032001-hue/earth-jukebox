"""Rutas de autenticación (Supabase Auth)."""

from fastapi import APIRouter, HTTPException

from app.core.supabase import get_supabase_client
from app.schemas.auth import AuthCredentials, AuthResponse, ProfileResponse

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/signup", response_model=AuthResponse)
async def signup(creds: AuthCredentials) -> AuthResponse:
    client = get_supabase_client()
    if client is None:
        raise HTTPException(status_code=503, detail="Supabase no configurado")
    try:
        res = client.auth.sign_up({"email": creds.email, "password": creds.password})
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    if not res.user:
        raise HTTPException(status_code=400, detail="No se pudo crear el usuario")
    if not res.session:
        return AuthResponse(
            access_token="",
            user_id=res.user.id,
            email=res.user.email,
            message="Registro creado. Confirma tu email para iniciar sesión (o desactiva la confirmación en Supabase para desarrollo).",
        )
    return AuthResponse(access_token=res.session.access_token, user_id=res.user.id, email=res.user.email)


@router.post("/login", response_model=AuthResponse)
async def login(creds: AuthCredentials) -> AuthResponse:
    client = get_supabase_client()
    if client is None:
        raise HTTPException(status_code=503, detail="Supabase no configurado")
    try:
        res = client.auth.sign_in_with_password({"email": creds.email, "password": creds.password})
    except Exception as exc:
        raise HTTPException(status_code=401, detail=str(exc)) from exc
    if not res.user or not res.session:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    return AuthResponse(access_token=res.session.access_token, user_id=res.user.id, email=res.user.email)


@router.get("/me", response_model=ProfileResponse)
async def me(token: str) -> ProfileResponse:
    client = get_supabase_client()
    if client is None:
        raise HTTPException(status_code=503, detail="Supabase no configurado")
    try:
        user = client.auth.get_user(token)
    except Exception as exc:
        raise HTTPException(status_code=401, detail=str(exc)) from exc
    if not user or not user.user:
        raise HTTPException(status_code=401, detail="Token inválido")
    return ProfileResponse(user_id=user.user.id, email=user.user.email)
