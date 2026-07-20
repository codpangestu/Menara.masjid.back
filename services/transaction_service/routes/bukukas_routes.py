from fastapi import APIRouter, Depends, Query, Header
from sqlalchemy.orm import Session
from typing import Optional
from shared.config.database import get_db
from services.transaction_service.services.bukukas_service import BukuKasService
from shared.utils.route_wrapper import require_api_key
from shared.utils.response_helper import ApiResponse

router = APIRouter()
service = BukuKasService()


@router.get("/bukukas-penerimaan/list")
def list_penerimaan(
    kode_org_baznas: Optional[str] = None,
    id_provinsi: Optional[int] = None,
    id_kabupaten_kota: Optional[int] = None,
    id_jenis_dana: Optional[int] = None,
    id_label_info_dana: Optional[int] = None,
    page: int = Query(1, ge=1),
    per_page: int = Query(10, ge=1, le=100),
    x_api_key: Optional[str] = Header(None),
    db: Session = Depends(get_db),
):
    err = require_api_key(x_api_key)
    if err:
        return err
    result = service.get_penerimaan(
        db, kode_org_baznas=kode_org_baznas, id_provinsi=id_provinsi,
        id_kabupaten_kota=id_kabupaten_kota, id_jenis_dana=id_jenis_dana,
        id_label_info_dana=id_label_info_dana, page=page, per_page=per_page,
    )
    return ApiResponse(
        data=result["data"],
        total=result["total"],
        page=result["page"],
        per_page=result["per_page"],
    )


@router.get("/bukukas-penerimaan/command-center")
def list_penerimaan_cc(
    kode_org_baznas: Optional[str] = None,
    page: int = Query(1, ge=1),
    per_page: int = Query(10, ge=1, le=100),
    x_api_key: Optional[str] = Header(None),
    db: Session = Depends(get_db),
):
    err = require_api_key(x_api_key)
    if err:
        return err
    data = service.get_penerimaan_cc(
        db, kode_org_baznas=kode_org_baznas, page=page, per_page=per_page,
    )
    return ApiResponse(data=data)


@router.get("/bukukas-pengeluaran/list")
def list_pengeluaran(
    kode_org_baznas: Optional[str] = None,
    id_provinsi: Optional[int] = None,
    id_kabupaten_kota: Optional[int] = None,
    id_jenis_dana: Optional[int] = None,
    id_label_info_dana: Optional[int] = None,
    page: int = Query(1, ge=1),
    per_page: int = Query(10, ge=1, le=100),
    x_api_key: Optional[str] = Header(None),
    db: Session = Depends(get_db),
):
    err = require_api_key(x_api_key)
    if err:
        return err
    result = service.get_pengeluaran(
        db, kode_org_baznas=kode_org_baznas, id_provinsi=id_provinsi,
        id_kabupaten_kota=id_kabupaten_kota, id_jenis_dana=id_jenis_dana,
        id_label_info_dana=id_label_info_dana, page=page, per_page=per_page,
    )
    return ApiResponse(
        data=result["data"],
        total=result["total"],
        page=result["page"],
        per_page=result["per_page"],
    )


@router.get("/bukukas-pengeluaran/command-center")
def list_pengeluaran_cc(
    kode_org_baznas: Optional[str] = None,
    page: int = Query(1, ge=1),
    per_page: int = Query(10, ge=1, le=100),
    x_api_key: Optional[str] = Header(None),
    db: Session = Depends(get_db),
):
    err = require_api_key(x_api_key)
    if err:
        return err
    data = service.get_pengeluaran_cc(
        db, kode_org_baznas=kode_org_baznas, page=page, per_page=per_page,
    )
    return ApiResponse(data=data)
