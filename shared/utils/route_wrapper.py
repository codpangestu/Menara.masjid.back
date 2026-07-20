from typing import Optional
from shared.utils.response_helper import api_key_invalid_response
from shared.config.environment import env


def verify_api_key(x_api_key: Optional[str]) -> bool:
    """Simple API key verification."""
    return x_api_key is not None and x_api_key == env.API_KEY


def require_api_key(x_api_key: Optional[str]):
    """Check API key and return error response if invalid."""
    if not verify_api_key(x_api_key):
        return api_key_invalid_response()
    return None
