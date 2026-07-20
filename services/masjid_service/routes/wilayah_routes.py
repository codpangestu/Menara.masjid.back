from fastapi import APIRouter, Depends, Query, Header
from sqlalchemy.orm import Session
from typing import Optional
from shared.config.database import get_db
from services.masjid_service.services.wilayah_service import WilayahService
from shared.utils.route_wrapper import require_api_key
from shared.utils.response_helper import ApiResponse

router = APIRouter()
service = WilayahService()


@router.get("/provinsi")
def get_provinsi(
    id: Optional[int] = Query(None),
    x_api_key: Optional[str] = Header(None),
    db: Session = Depends(get_db),
):
    err = require_api_key(x_api_key)
    if err:
        return err
    data = service.get_provinsi(db, id)
    return ApiResponse(data=data)


@router.get("/kabupaten-kota")
def get_kabupaten_kota(
    id_provinsi: Optional[int] = Query(None),
    x_api_key: Optional[str] = Header(None),
    db: Session = Depends(get_db),
):
    err = require_api_key(x_api_key)
    if err:
        return err
    data = service.get_kabupaten_kota(db, id_provinsi)
    return ApiResponse(data=data)


@router.get("/kecamatan")
def get_kecamatan(
    id_kabupaten_kota: Optional[int] = Query(None),
    x_api_key: Optional[str] = Header(None),
    db: Session = Depends(get_db),
):
    err = require_api_key(x_api_key)
    if err:
        return err
    data = service.get_kecamatan(db, id_kabupaten_kota)
    return ApiResponse(data=data)


@router.get("/kelurahan-desa")
def get_kelurahan_desa(
    id_kecamatan: Optional[int] = Query(None),
    x_api_key: Optional[str] = Header(None),
    db: Session = Depends(get_db),
):
    err = require_api_key(x_api_key)
    if err:
        return err
    data = service.get_kelurahan_desa(db, id_kecamatan)
    return ApiResponse(data=data)
