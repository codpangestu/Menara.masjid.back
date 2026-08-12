"""
CORS configuration for MENARA API microservices.

Mengizinkan request dari browser (frontend) ke API microservices.
Tanpa ini, browser memblokir semua request lintas-origin (mis. login
dari http://localhost:3000 ke http://localhost:8001) dengan error CORS.
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from shared.config.environment import env

# Origin frontend yang diizinkan memanggil API dari browser.
# Dev: port Vite default (5173) + port proyek ini (3000/3001).
# Production: tambahkan domain via env CORS_ORIGINS (comma separated).
DEFAULT_CORS_ORIGINS = [
    "http://localhost:3000",
    "http://localhost:3001",
    "http://localhost:5173",
    "http://127.0.0.1:3000",
    "http://127.0.0.1:3001",
    "http://127.0.0.1:5173",
]


def get_cors_origins() -> list[str]:
    """Gabungkan origin default dengan env CORS_ORIGINS (optional)."""
    origins = list(DEFAULT_CORS_ORIGINS)
    extra = (env.CORS_ORIGINS or "").strip()
    if extra:
        origins += [o.strip() for o in extra.split(",") if o.strip()]
    return origins


def setup_cors(app: FastAPI) -> None:
    """Pasang CORSMiddleware pada FastAPI app (dipanggil di tiap main.py)."""
    app.add_middleware(
        CORSMiddleware,
        allow_origins=get_cors_origins(),
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
