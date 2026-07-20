"""
Masjid Service — MENARA API
Handles: masjid CRUD, wilayah, rekap, master data (tema, kategori)
Port: 8002
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

import uvicorn
from fastapi import FastAPI
from shared.config.environment import env
from shared.middlewares.error_middleware import global_exception_handler
from shared.middlewares.logging_middleware import logging_middleware

from services.masjid_service.routes.masjid_routes import router as masjid_router
from services.masjid_service.routes.wilayah_routes import router as wilayah_router

app = FastAPI(
    title=f"{env.APP_NAME} - Masjid Service",
    version=env.APP_VERSION,
    docs_url="/docs" if env.DEBUG else None,
    redoc_url="/redoc" if env.DEBUG else None,
)

app.middleware("http")(logging_middleware)
app.add_exception_handler(Exception, global_exception_handler)

app.include_router(masjid_router, prefix="/api/v1", tags=["Masjid"])
app.include_router(wilayah_router, prefix="/api/v1", tags=["Wilayah"])


@app.get("/health")
def health():
    return {"service": "masjid", "status": "ok"}


if __name__ == "__main__":
    uvicorn.run("services.masjid_service.main:app", host="0.0.0.0", port=8002, reload=env.DEBUG)
