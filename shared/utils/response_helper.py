from pydantic import BaseModel, ConfigDict
from typing import Optional, Any
from datetime import datetime, date
from decimal import Decimal


class ApiResponse(BaseModel):
    """Standard API response model used across all endpoints."""
    model_config = ConfigDict(extra="allow")

    status_code: str = "000"
    status: str = "Sukses"
    message: Optional[str] = None
    data: Any = None
    error: Optional[str] = None
    links: Optional[Any] = None
    total: Optional[int] = None
    page: Optional[int] = None
    per_page: Optional[int] = None


def model_to_dict(obj):
    """
    Convert SQLAlchemy model instance to a plain dict for JSON serialization.
    Handles datetime, date, and Decimal types that are not natively JSON-serializable.
    """
    if obj is None:
        return None
    result = {}
    for column in obj.__table__.columns:
        value = getattr(obj, column.name)
        if isinstance(value, datetime):
            value = value.isoformat()
        elif isinstance(value, date):
            value = value.isoformat()
        elif isinstance(value, Decimal):
            value = float(value)
        result[column.name] = value
    return result


def api_key_invalid_response():
    """Return standard API key invalid response."""
    return ApiResponse(status_code="101", status="API KEY Invalid !")


def not_found_response(message: str = "Tidak ditemukan"):
    """Return standard not found response."""
    return ApiResponse(status_code="404", status=message)
