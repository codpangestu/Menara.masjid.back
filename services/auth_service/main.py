"""
Auth Service — MENARA API
Handles: authentication, user management
Port: 8001
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

import uvicorn
from fastapi import FastAPI
from shared.config.environment import env
from shared.middlewares.error_middleware import global_exception_handler
from shared.middlewares.logging_middleware import logging_middleware

from services.auth_service.routes.auth_routes import router as auth_router
from services.auth_service.routes.users_routes import router as users_router

app = FastAPI(
    title=f"{env.APP_NAME} - Auth Service",
    version=env.APP_VERSION,
    docs_url="/docs" if env.DEBUG else None,
    redoc_url="/redoc" if env.DEBUG else None,
)

app.middleware("http")(logging_middleware)
app.add_exception_handler(Exception, global_exception_handler)

app.include_router(auth_router, prefix="/api/v1", tags=["Auth"])
app.include_router(users_router, prefix="/api/v1", tags=["Users"])


@app.get("/health")
def health():
    return {"service": "auth", "status": "ok"}


if __name__ == "__main__":
    uvicorn.run("services.auth_service.main:app", host="0.0.0.0", port=8001, reload=env.DEBUG)
