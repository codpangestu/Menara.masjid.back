from fastapi import APIRouter, Depends, Query, Header
from sqlalchemy.orm import Session
from typing import Optional
from shared.config.database import get_db
from services.admin_service.services.master_service import MasterService
from shared.utils.route_wrapper import require_api_key
from shared.utils.response_helper import ApiResponse

router = APIRouter()
service = MasterService()


@router.get("/levels")
def get_levels(
    id_level: Optional[int] = Query(None),
    x_api_key: Optional[str] = Header(None),
    db: Session = Depends(get_db),
):
    err = require_api_key(x_api_key)
    if err:
        return err
    return ApiResponse(data=service.get_levels(db, id_level))


@router.get("/labels")
def get_labels(
    id_labels: Optional[int] = Query(None),
    x_api_key: Optional[str] = Header(None),
    db: Session = Depends(get_db),
):
    err = require_api_key(x_api_key)
    if err:
        return err
    return ApiResponse(data=service.get_labels(db, id_labels))


@router.get("/jenis-dana")
def get_jenis_dana(
    id_jenis_dana: Optional[int] = Query(None),
    x_api_key: Optional[str] = Header(None),
    db: Session = Depends(get_db),
):
    err = require_api_key(x_api_key)
    if err:
        return err
    return ApiResponse(data=service.get_jenis_dana(db, id_jenis_dana))


@router.get("/jenis-harta")
def get_jenis_harta(
    id_jenis_harta: Optional[int] = Query(None),
    x_api_key: Optional[str] = Header(None),
    db: Session = Depends(get_db),
):
    err = require_api_key(x_api_key)
    if err:
        return err
    return ApiResponse(data=service.get_jenis_harta(db, id_jenis_harta))


@router.get("/label-info-dana")
def get_label_info_dana(
    id_label_info_dana: Optional[int] = Query(None),
    x_api_key: Optional[str] = Header(None),
    db: Session = Depends(get_db),
):
    err = require_api_key(x_api_key)
    if err:
        return err
    return ApiResponse(data=service.get_label_info_dana(db, id_label_info_dana))


@router.get("/tema")
def get_tema(parent_id: Optional[str] = Query(None), db: Session = Depends(get_db)):
    return ApiResponse(data=service.get_tema(db, parent_id))


@router.get("/kategori-acara")
def get_kategori_acara(parent_id: Optional[str] = Query(None), db: Session = Depends(get_db)):
    return ApiResponse(data=service.get_kategori_acara(db, parent_id))


@router.get("/kategori-cerita")
def get_kategori_cerita(parent_id: Optional[str] = Query(None), db: Session = Depends(get_db)):
    return ApiResponse(data=service.get_kategori_cerita(db, parent_id))


@router.get("/kategori-donasi")
def get_kategori_donasi(parent_id: Optional[str] = Query(None), db: Session = Depends(get_db)):
    return ApiResponse(data=service.get_kategori_donasi(db, parent_id))


@router.get("/kategori-postingan")
def get_kategori_postingan(parent_id: Optional[str] = Query(None), db: Session = Depends(get_db)):
    return ApiResponse(data=service.get_kategori_postingan(db, parent_id))
