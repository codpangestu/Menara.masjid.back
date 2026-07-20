from fastapi import APIRouter, Depends, Header
from sqlalchemy.orm import Session
from typing import Optional, Any
from shared.config.database import get_db
from shared.config.environment import env
from services.auth_service.services.auth_service import AuthService
from shared.middlewares.auth_middleware import get_current_user
from shared.schemas.auth import LoginRequest, TokenResponse, RegisterUserRequest
from shared.models.users import Users
from shared.utils.response_helper import ApiResponse

router = APIRouter()
service = AuthService()


@router.post("/login", response_model=TokenResponse)
def login(request: LoginRequest, db: Session = Depends(get_db)):
    result = service.login(db, request.email, request.password)
    return TokenResponse(
        access_token=result["access_token"],
        user=result["user"],
    )


@router.post("/login/admin-masjid", response_model=TokenResponse)
def login_admin_masjid(request: LoginRequest, db: Session = Depends(get_db)):
    result = service.login_admin_masjid(db, request.email, request.password)
    return TokenResponse(
        access_token=result["access_token"],
        user=result["user"],
    )


@router.post("/login/admin-pusat", response_model=TokenResponse)
def login_admin_pusat(request: LoginRequest, db: Session = Depends(get_db)):
    result = service.login_admin_pusat(db, request.email, request.password)
    return TokenResponse(
        access_token=result["access_token"],
        user=result["user"],
    )


@router.post("/register/user")
def register_user(
    request: RegisterUserRequest,
    x_api_key: Optional[str] = Header(None),
    db: Session = Depends(get_db),
):
    if not x_api_key or x_api_key != env.API_KEY:
        return {"status_code": "101", "status": "API KEY Invalid !"}
    return service.register_user(db, request.model_dump())


@router.get("/me")
def get_me(current_user: Users = Depends(get_current_user)):
    return service.get_me(current_user)


@router.post("/logout")
def logout():
    return service.logout()
