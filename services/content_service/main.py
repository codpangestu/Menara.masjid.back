"""
Content Service — MENARA API
Handles: home, informasi, kajian, acara, cerita, donasi, postingan, panduan, masjid public
Port: 8003
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

import uvicorn
from fastapi import FastAPI
from shared.config.environment import env
from shared.middlewares.error_middleware import global_exception_handler
from shared.middlewares.logging_middleware import logging_middleware
from shared.middlewares.cors import setup_cors

from services.content_service.routes.content_routes import router as content_router

app = FastAPI(
    title=f"{env.APP_NAME} - Content Service",
    version=env.APP_VERSION,
    docs_url="/docs" if env.DEBUG else None,
    redoc_url="/redoc" if env.DEBUG else None,
)

app.middleware("http")(logging_middleware)
app.add_exception_handler(Exception, global_exception_handler)
setup_cors(app)

app.include_router(content_router, prefix="/api/v1", tags=["Content"])


@app.get("/health")
def health():
    return {"service": "content", "status": "ok"}


if __name__ == "__main__":
    uvicorn.run("services.content_service.main:app", host="0.0.0.0", port=8003, reload=env.DEBUG)
