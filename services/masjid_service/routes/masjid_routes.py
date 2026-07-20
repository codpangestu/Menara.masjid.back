from fastapi import APIRouter, Depends, Query, Header
from sqlalchemy.orm import Session
from typing import Optional
from shared.config.database import get_db
from services.masjid_service.services.masjid_service import MasjidService
from shared.utils.route_wrapper import require_api_key
from shared.utils.response_helper import ApiResponse

router = APIRouter()
service = MasjidService()


@router.get("/masjid/detail/{id_masjid}")
def get_detail_masjid(id_masjid: str, db: Session = Depends(get_db)):
    data = service.get_detail(db, id_masjid)
    return ApiResponse(data=data)


@router.get("/masjid/list")
def get_list_masjid(
    page: int = Query(1, ge=1),
    per_page: int = Query(10, ge=1, le=100),
    kode_org_baznas: Optional[str] = None,
    id_provinsi: Optional[int] = None,
    id_kabupaten_kota: Optional[int] = None,
    keyword_nama: Optional[str] = None,
    keyword_alamat: Optional[str] = None,
    keyword_label: Optional[str] = None,
    x_api_key: Optional[str] = Header(None),
    db: Session = Depends(get_db),
):
    err = require_api_key(x_api_key)
    if err:
        return err
    result = service.get_list(
        db, page, per_page, kode_org_baznas, id_provinsi,
        id_kabupaten_kota, keyword_nama, keyword_alamat, keyword_label,
    )
    return ApiResponse(
        data=result["data"],
        links=f"?page={page}&per_page={per_page}",
    )


@router.get("/masjid/by-wilayah")
def get_masjid_by_wilayah(
    id_provinsi: int,
    id_kabupaten_kota: Optional[int] = None,
    keyword_nama_masjid: Optional[str] = None,
    keyword_alamat_masjid: Optional[str] = None,
    keyword_label_masjid: Optional[str] = None,
    page: int = Query(1, ge=1),
    per_page: int = Query(10, ge=1, le=100),
    x_api_key: Optional[str] = Header(None),
    db: Session = Depends(get_db),
):
    err = require_api_key(x_api_key)
    if err:
        return err
    results = service.get_by_wilayah(
        db, id_provinsi, id_kabupaten_kota, keyword_nama_masjid,
        keyword_alamat_masjid, keyword_label_masjid, page, per_page,
    )
    return ApiResponse(data=[dict(r._mapping) for r in results])


@router.get("/masjid/pengurus/{id_masjid}")
def get_pengurus_masjid(
    id_masjid: str,
    x_api_key: Optional[str] = Header(None),
    db: Session = Depends(get_db),
):
    err = require_api_key(x_api_key)
    if err:
        return err
    data = service.get_pengurus(db, id_masjid)
    return ApiResponse(data=data)


# ===== REKAP ENDPOINTS =====

@router.get("/rekap/penerimaan")
def get_rekap_penerimaan(
    kode_org_baznas: Optional[str] = None,
    id_provinsi: Optional[int] = None,
    id_kabupaten_kota: Optional[int] = None,
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    x_api_key: Optional[str] = Header(None),
    db: Session = Depends(get_db),
):
    err = require_api_key(x_api_key)
    if err:
        return err
    result = service.get_rekap_penerimaan(
        db, kode_org_baznas=kode_org_baznas, id_provinsi=id_provinsi,
        id_kabupaten_kota=id_kabupaten_kota, start_date=start_date, end_date=end_date,
    )
    return ApiResponse(data=dict(result._mapping) if result else {})


@router.get("/rekap/pengeluaran")
def get_rekap_pengeluaran(
    kode_org_baznas: Optional[str] = None,
    id_provinsi: Optional[int] = None,
    id_kabupaten_kota: Optional[int] = None,
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    x_api_key: Optional[str] = Header(None),
    db: Session = Depends(get_db),
):
    err = require_api_key(x_api_key)
    if err:
        return err
    result = service.get_rekap_pengeluaran(
        db, kode_org_baznas=kode_org_baznas, id_provinsi=id_provinsi,
        id_kabupaten_kota=id_kabupaten_kota, start_date=start_date, end_date=end_date,
    )
    return ApiResponse(data=dict(result._mapping) if result else {})


@router.get("/rekap/by-masjid/{id_masjid}")
def get_rekap_by_masjid(
    id_masjid: str,
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    x_api_key: Optional[str] = Header(None),
    db: Session = Depends(get_db),
):
    err = require_api_key(x_api_key)
    if err:
        return err
    result = service.get_rekap_by_masjid(db, id_masjid, start_date=start_date, end_date=end_date)
    return ApiResponse(data=result)
