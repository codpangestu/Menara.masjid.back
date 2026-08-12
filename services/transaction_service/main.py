"""
Transaction Service — MENARA API
Handles: bukukas penerimaan/pengeluaran, sync push/pull
Port: 8004
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

from services.transaction_service.routes.bukukas_routes import router as bukukas_router
from services.transaction_service.routes.sync_routes import router as sync_router

app = FastAPI(
    title=f"{env.APP_NAME} - Transaction Service",
    version=env.APP_VERSION,
    docs_url="/docs" if env.DEBUG else None,
    redoc_url="/redoc" if env.DEBUG else None,
)

app.middleware("http")(logging_middleware)
app.add_exception_handler(Exception, global_exception_handler)
setup_cors(app)

app.include_router(bukukas_router, prefix="/api/v1", tags=["BukuKas"])
app.include_router(sync_router, prefix="/api/v1", tags=["Sync"])


@app.get("/health")
def health():
    return {"service": "transaction", "status": "ok"}


if __name__ == "__main__":
    uvicorn.run("services.transaction_service.main:app", host="0.0.0.0", port=8004, reload=env.DEBUG)
