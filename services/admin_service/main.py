"""
Admin Service — MENARA API
Handles: admin CRUD (masjid, content, master, wilayah, transaksi, pengajuan), master data
Port: 8005
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

import uvicorn
from fastapi import FastAPI
from shared.config.environment import env
from shared.middlewares.error_middleware import global_exception_handler
from shared.middlewares.logging_middleware import logging_middleware

from services.admin_service.routes.admin_routes import router as admin_router
from services.admin_service.routes.master_routes import router as master_router

app = FastAPI(
    title=f"{env.APP_NAME} - Admin Service",
    version=env.APP_VERSION,
    docs_url="/docs" if env.DEBUG else None,
    redoc_url="/redoc" if env.DEBUG else None,
)

app.middleware("http")(logging_middleware)
app.add_exception_handler(Exception, global_exception_handler)

app.include_router(admin_router, prefix="/api/v1", tags=["Admin"])
app.include_router(master_router, prefix="/api/v1", tags=["Master"])


@app.get("/health")
def health():
    return {"service": "admin", "status": "ok"}


if __name__ == "__main__":
    uvicorn.run("services.admin_service.main:app", host="0.0.0.0", port=8005, reload=env.DEBUG)
