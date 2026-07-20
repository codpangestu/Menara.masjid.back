from typing import Any, Optional
from datetime import datetime, date
from decimal import Decimal


def model_to_dict(obj):
    """Convert SQLAlchemy model instance to a plain dict for JSON serialization."""
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
