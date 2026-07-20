from fastapi import Request, status
from fastapi.responses import JSONResponse
from shared.utils.app_error import AppError


async def global_exception_handler(request: Request, exc: Exception):
    """Global exception handler for all unhandled exceptions."""
    if isinstance(exc, AppError):
        return JSONResponse(
            status_code=exc.status_code,
            content={
                "status_code": str(exc.status_code),
                "status": str(exc).split(":")[0] if ":" in str(exc) else exc.detail,
                "detail": exc.detail,
            },
        )

    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "status_code": "500",
            "status": "Internal Server Error",
            "detail": str(exc),
        },
    )
