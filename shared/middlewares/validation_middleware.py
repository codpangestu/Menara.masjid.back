from typing import Any, Dict, Optional


def validate_required_fields(data: Dict[str, Any], required: list) -> Optional[str]:
    """Validate that required fields exist in data dict.
    Returns error message if validation fails, None if passes.
    """
    for field in required:
        if field not in data or data[field] is None or data[field] == "":
            return f"Field '{field}' is required"
    return None
