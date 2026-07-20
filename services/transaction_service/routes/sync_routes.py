from fastapi import APIRouter, Depends, Header
from sqlalchemy.orm import Session
from typing import Optional
from pydantic import BaseModel
from typing import Dict, List, Any
from shared.config.database import get_db
from shared.config.environment import env
from services.transaction_service.services.sync_service import SyncService
from shared.utils.response_helper import ApiResponse

router = APIRouter()
service = SyncService()


class SyncPushRequest(BaseModel):
    data: Dict[str, list]


@router.post("/sync-push")
def sync_push(
    request: SyncPushRequest,
    x_api_key: Optional[str] = Header(None),
    db: Session = Depends(get_db),
):
    if not x_api_key or x_api_key != env.API_KEY:
        return ApiResponse(status_code="101", status="API KEY Invalid !")
    return service.push(request.data)


@router.get("/sync-pull")
def sync_pull(
    last_sync: Optional[str] = None,
    tables: Optional[str] = None,
    x_api_key: Optional[str] = Header(None),
    db: Session = Depends(get_db),
):
    if not x_api_key or x_api_key != env.API_KEY:
        return ApiResponse(status_code="101", status="API KEY Invalid !")
    return service.pull(tables, last_sync)
