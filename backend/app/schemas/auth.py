"""Esquemas de autenticación."""

from pydantic import BaseModel


class AuthCredentials(BaseModel):
    email: str
    password: str


class AuthResponse(BaseModel):
    access_token: str = ""
    user_id: str = ""
    email: str | None = None
    message: str | None = None


class ProfileResponse(BaseModel):
    user_id: str
    email: str | None = None
    display_name: str | None = None
