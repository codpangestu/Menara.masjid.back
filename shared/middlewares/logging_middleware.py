import logging
import time
from fastapi import Request

logger = logging.getLogger("menara-api")


async def logging_middleware(request: Request, call_next):
    """Log incoming requests and their duration."""
    start = time.time()
    response = await call_next(request)
    duration = time.time() - start

    logger.info(
        "%s %s - %s (%.2fs)",
        request.method,
        request.url.path,
        response.status_code,
        duration,
    )
    return response
