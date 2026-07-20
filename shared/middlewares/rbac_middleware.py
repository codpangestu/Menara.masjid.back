from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from shared.middlewares.auth_middleware import get_current_user
from shared.middlewares.auth_middleware import get_current_user  # noqa


def get_current_active_user(current_user=Depends(get_current_user)):
    """Get current active user (status_aktif == 1)."""
    if current_user.status_aktif != 1:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Inactive user account",
        )
    return current_user


def require_roles(allowed_roles: List[str]):
    """Dependency factory for role-based access control."""
    def role_checker(current_user=Depends(get_current_active_user)):
        if current_user.jalur_akses not in allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Access denied. Required roles: {', '.join(allowed_roles)}",
            )
        return current_user
    return role_checker
