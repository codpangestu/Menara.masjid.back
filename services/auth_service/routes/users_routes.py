from fastapi import APIRouter, Depends, Header
from sqlalchemy.orm import Session
from typing import Optional
from shared.config.database import get_db
from services.auth_service.services.users_service import UsersService
from shared.utils.route_wrapper import require_api_key
from shared.utils.response_helper import ApiResponse

router = APIRouter()
service = UsersService()


@router.get("/users/list")
def get_list_users(
    id_provinsi: Optional[int] = None,
    id_kabupaten_kota: Optional[int] = None,
    kode_org_baznas: Optional[str] = None,
    x_api_key: Optional[str] = Header(None),
    db: Session = Depends(get_db),
):
    err = require_api_key(x_api_key)
    if err:
        return err
    data = service.get_list(db, id_provinsi, id_kabupaten_kota, kode_org_baznas)
    return ApiResponse(data=data)


@router.get("/users/detail/{id_user}")
def get_detail_user(
    id_user: int,
    x_api_key: Optional[str] = Header(None),
    db: Session = Depends(get_db),
):
    err = require_api_key(x_api_key)
    if err:
        return err
    data = service.get_detail(db, id_user)
    if not data:
        return ApiResponse(status_code="404", status="User tidak ditemukan")
    return ApiResponse(data=data)


@router.post("/users/register")
def register_user(
    nama: str,
    email: str,
    jk: str = "",
    alamat: str = "",
    nohp: str = "",
    id_jalur_akses: str = "",
    kode_org_baznas: str = "",
    id_labels: int = 0,
    catatan: str = "",
    x_api_key: Optional[str] = Header(None),
    db: Session = Depends(get_db),
):
    err = require_api_key(x_api_key)
    if err:
        return err
    result = service.register(
        db, nama=nama, email=email, jk=jk, alamat=alamat,
        nohp=nohp, id_jalur_akses=id_jalur_akses,
        kode_org_baznas=kode_org_baznas, id_labels=id_labels, catatan=catatan,
    )
    return ApiResponse(data=result)


@router.put("/users/update/{id_user}")
def update_user(
    id_user: int,
    nama: Optional[str] = None,
    email: Optional[str] = None,
    jk: Optional[str] = None,
    alamat: Optional[str] = None,
    nohp: Optional[str] = None,
    id_jalur_akses: Optional[str] = None,
    id_level: Optional[int] = None,
    id_labels: Optional[int] = None,
    status_aktif: Optional[int] = None,
    kode_org_baznas: Optional[str] = None,
    x_api_key: Optional[str] = Header(None),
    db: Session = Depends(get_db),
):
    err = require_api_key(x_api_key)
    if err:
        return err
    ok = service.update(
        db, id_user, nama=nama, email=email, jk=jk, alamat=alamat,
        nohp=nohp, id_jalur_akses=id_jalur_akses,
        id_level=id_level, id_labels=id_labels, status_aktif=status_aktif,
        kode_org_baznas=kode_org_baznas,
    )
    if not ok:
        return ApiResponse(status_code="404", status="User tidak ditemukan")
    return ApiResponse(status_code="000", status="Sukses")


@router.delete("/users/delete/{id_user}")
def delete_user(
    id_user: int,
    x_api_key: Optional[str] = Header(None),
    db: Session = Depends(get_db),
):
    err = require_api_key(x_api_key)
    if err:
        return err
    ok = service.delete(db, id_user)
    if not ok:
        return ApiResponse(status_code="404", status="User tidak ditemukan")
    return ApiResponse(message="Data deleted successfully !")
