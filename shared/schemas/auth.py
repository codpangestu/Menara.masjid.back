from pydantic import BaseModel
from typing import Optional, Any


class LoginRequest(BaseModel):
    email: str
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: Any = None


class RegisterUserRequest(BaseModel):
    id_jalur_akses: str
    nama: str
    jk: str
    alamat: str
    email: str
    nohp: Optional[str] = ""
    kode_org_baznas: Optional[str] = ""
    id_labels: int
    catatan: Optional[str] = ""
