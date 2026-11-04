"""Clientes Supabase (preparados)."""

from supabase import Client, create_client

from app.core.config import settings


def get_supabase_client() -> Client | None:
    """Cliente anónimo (para Auth)."""
    if not settings.supabase_url or not settings.supabase_anon_key:
        return None
    return create_client(settings.supabase_url, settings.supabase_anon_key)


def get_service_client() -> Client | None:
    """Cliente con service role (para operaciones de backend que bypassan RLS)."""
    if not settings.supabase_url or not settings.supabase_service_role_key:
        return None
    return create_client(settings.supabase_url, settings.supabase_service_role_key)
