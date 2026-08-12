from fastapi import APIRouter, Depends, Query, Header, Body
from sqlalchemy.orm import Session
from typing import Optional, Any, Dict, List
from shared.config.database import get_db
from services.admin_service.services.admin_service import AdminService
from shared.utils.route_wrapper import verify_api_key
from shared.utils.response_helper import ApiResponse

router = APIRouter()
service = AdminService()


# ======================================================================
# MASJID CRUD
# ======================================================================

@router.post("/admin/masjid/create")
def create_masjid(
    data: Dict[str, Any] = Body(...),
    x_api_key: Optional[str] = Header(None),
    db: Session = Depends(get_db),
):
    if not verify_api_key(x_api_key):
        return ApiResponse(status_code="101", status="API KEY Invalid !")
    result = service.create_masjid(db, data)
    return ApiResponse(data=result)


@router.put("/admin/masjid/update/{id_masjid}")
def update_masjid(
    id_masjid: str,
    data: Dict[str, Any] = Body(...),
    x_api_key: Optional[str] = Header(None),
    db: Session = Depends(get_db),
):
    if not verify_api_key(x_api_key):
        return ApiResponse(status_code="101", status="API KEY Invalid !")
    if not service.update_masjid(db, id_masjid, data):
        return ApiResponse(status_code="404", status="Masjid tidak ditemukan")
    return ApiResponse(status_code="000", status="Sukses")


@router.delete("/admin/masjid/delete/{id_masjid}")
def delete_masjid(
    id_masjid: str,
    x_api_key: Optional[str] = Header(None),
    db: Session = Depends(get_db),
):
    if not verify_api_key(x_api_key):
        return ApiResponse(status_code="101", status="API KEY Invalid !")
    if not service.delete_masjid(db, id_masjid):
        return ApiResponse(status_code="404", status="Masjid tidak ditemukan")
    return ApiResponse(message="Data deleted successfully !")


# ======================================================================
# CONTENT CRUD
# ======================================================================

@router.post("/admin/content/{tipe}/create")
def create_content(
    tipe: str,
    data: Dict[str, Any] = Body(...),
    x_api_key: Optional[str] = Header(None),
    db: Session = Depends(get_db),
):
    if not verify_api_key(x_api_key):
        return ApiResponse(status_code="101", status="API KEY Invalid !")
    result, error = service.create_content(db, tipe, data)
    if error:
        return ApiResponse(status_code="400", status=error)
    return ApiResponse(data=result)


@router.put("/admin/content/{tipe}/update/{pk_value}")
def update_content(
    tipe: str,
    pk_value: Any,
    data: Dict[str, Any] = Body(...),
    x_api_key: Optional[str] = Header(None),
    db: Session = Depends(get_db),
):
    if not verify_api_key(x_api_key):
        return ApiResponse(status_code="101", status="API KEY Invalid !")
    ok, error = service.update_content(db, tipe, pk_value, data)
    if error:
        return ApiResponse(status_code="400", status=error)
    if not ok:
        return ApiResponse(status_code="404", status="Data tidak ditemukan")
    return ApiResponse(status_code="000", status="Sukses")


@router.delete("/admin/content/{tipe}/delete/{pk_value}")
def delete_content(
    tipe: str,
    pk_value: Any,
    x_api_key: Optional[str] = Header(None),
    db: Session = Depends(get_db),
):
    if not verify_api_key(x_api_key):
        return ApiResponse(status_code="101", status="API KEY Invalid !")
    ok, error = service.delete_content(db, tipe, pk_value)
    if error:
        return ApiResponse(status_code="400", status=error)
    if not ok:
        return ApiResponse(status_code="404", status="Data tidak ditemukan")
    return ApiResponse(message="Data deleted successfully !")


# ======================================================================
# MASTER DATA CRUD
# ======================================================================

@router.post("/admin/master/{tipe}/create")
def create_master(
    tipe: str,
    data: Dict[str, Any] = Body(...),
    x_api_key: Optional[str] = Header(None),
    db: Session = Depends(get_db),
):
    if not verify_api_key(x_api_key):
        return ApiResponse(status_code="101", status="API KEY Invalid !")
    result, error = service.create_master(db, tipe, data)
    if error:
        return ApiResponse(status_code="400", status=error)
    return ApiResponse(data=result)


@router.put("/admin/master/{tipe}/update/{pk_value}")
def update_master(
    tipe: str,
    pk_value: int,
    data: Dict[str, Any] = Body(...),
    x_api_key: Optional[str] = Header(None),
    db: Session = Depends(get_db),
):
    if not verify_api_key(x_api_key):
        return ApiResponse(status_code="101", status="API KEY Invalid !")
    ok, error = service.update_master(db, tipe, pk_value, data)
    if error:
        return ApiResponse(status_code="400", status=error)
    if not ok:
        return ApiResponse(status_code="404", status="Data tidak ditemukan")
    return ApiResponse(status_code="000", status="Sukses")


@router.delete("/admin/master/{tipe}/delete/{pk_value}")
def delete_master(
    tipe: str,
    pk_value: int,
    x_api_key: Optional[str] = Header(None),
    db: Session = Depends(get_db),
):
    if not verify_api_key(x_api_key):
        return ApiResponse(status_code="101", status="API KEY Invalid !")
    ok, error = service.delete_master(db, tipe, pk_value)
    if error:
        return ApiResponse(status_code="400", status=error)
    if not ok:
        return ApiResponse(status_code="404", status="Data tidak ditemukan")
    return ApiResponse(message="Data deleted successfully !")


# ======================================================================
# WILAYAH CRUD
# ======================================================================

@router.post("/admin/wilayah/{tipe}/create")
def create_wilayah(
    tipe: str,
    data: Dict[str, Any] = Body(...),
    x_api_key: Optional[str] = Header(None),
    db: Session = Depends(get_db),
):
    if not verify_api_key(x_api_key):
        return ApiResponse(status_code="101", status="API KEY Invalid !")
    result, error = service.create_wilayah(db, tipe, data)
    if error:
        return ApiResponse(status_code="400", status=error)
    return ApiResponse(data=result)


@router.put("/admin/wilayah/{tipe}/update/{pk_value}")
def update_wilayah(
    tipe: str,
    pk_value: int,
    data: Dict[str, Any] = Body(...),
    x_api_key: Optional[str] = Header(None),
    db: Session = Depends(get_db),
):
    if not verify_api_key(x_api_key):
        return ApiResponse(status_code="101", status="API KEY Invalid !")
    ok, error = service.update_wilayah(db, tipe, pk_value, data)
    if error:
        return ApiResponse(status_code="400", status=error)
    if not ok:
        return ApiResponse(status_code="404", status="Data tidak ditemukan")
    return ApiResponse(status_code="000", status="Sukses")


@router.delete("/admin/wilayah/{tipe}/delete/{pk_value}")
def delete_wilayah(
    tipe: str,
    pk_value: int,
    x_api_key: Optional[str] = Header(None),
    db: Session = Depends(get_db),
):
    if not verify_api_key(x_api_key):
        return ApiResponse(status_code="101", status="API KEY Invalid !")
    ok, error = service.delete_wilayah(db, tipe, pk_value)
    if error:
        return ApiResponse(status_code="400", status=error)
    if not ok:
        return ApiResponse(status_code="404", status="Data tidak ditemukan")
    return ApiResponse(message="Data deleted successfully !")


# ======================================================================
# MASJID DETAIL CRUD
# ======================================================================

@router.post("/admin/detail/{tipe}/create")
def create_detail(
    tipe: str,
    data: Dict[str, Any] = Body(...),
    x_api_key: Optional[str] = Header(None),
    db: Session = Depends(get_db),
):
    if not verify_api_key(x_api_key):
        return ApiResponse(status_code="101", status="API KEY Invalid !")
    result, error = service.create_detail(db, tipe, data)
    if error:
        return ApiResponse(status_code="400", status=error)
    return ApiResponse(data=result)


@router.put("/admin/detail/{tipe}/update/{pk_value}")
def update_detail(
    tipe: str,
    pk_value: int,
    data: Dict[str, Any] = Body(...),
    x_api_key: Optional[str] = Header(None),
    db: Session = Depends(get_db),
):
    if not verify_api_key(x_api_key):
        return ApiResponse(status_code="101", status="API KEY Invalid !")
    ok, error = service.update_detail(db, tipe, pk_value, data)
    if error:
        return ApiResponse(status_code="400", status=error)
    if not ok:
        return ApiResponse(status_code="404", status="Data tidak ditemukan")
    return ApiResponse(status_code="000", status="Sukses")


@router.delete("/admin/detail/{tipe}/delete/{pk_value}")
def delete_detail(
    tipe: str,
    pk_value: int,
    x_api_key: Optional[str] = Header(None),
    db: Session = Depends(get_db),
):
    if not verify_api_key(x_api_key):
        return ApiResponse(status_code="101", status="API KEY Invalid !")
    ok, error = service.delete_detail(db, tipe, pk_value)
    if error:
        return ApiResponse(status_code="400", status=error)
    if not ok:
        return ApiResponse(status_code="404", status="Data tidak ditemukan")
    return ApiResponse(message="Data deleted successfully !")


# ======================================================================
# TRANSAKSI CRUD
# ======================================================================

@router.post("/admin/transaksi/{tipe}/create")
def create_transaksi(
    tipe: str,
    data: Dict[str, Any] = Body(...),
    x_api_key: Optional[str] = Header(None),
    db: Session = Depends(get_db),
):
    if not verify_api_key(x_api_key):
        return ApiResponse(status_code="101", status="API KEY Invalid !")
    result, error = service.create_transaksi(db, tipe, data)
    if error:
        return ApiResponse(status_code="400", status=error)
    return ApiResponse(data=result)


@router.put("/admin/transaksi/{tipe}/update/{pk_value}")
def update_transaksi(
    tipe: str,
    pk_value: int,
    data: Dict[str, Any] = Body(...),
    x_api_key: Optional[str] = Header(None),
    db: Session = Depends(get_db),
):
    if not verify_api_key(x_api_key):
        return ApiResponse(status_code="101", status="API KEY Invalid !")
    ok, error = service.update_transaksi(db, tipe, pk_value, data)
    if error:
        return ApiResponse(status_code="400", status=error)
    if not ok:
        return ApiResponse(status_code="404", status="Data tidak ditemukan")
    return ApiResponse(status_code="000", status="Sukses")


@router.delete("/admin/transaksi/{tipe}/delete/{pk_value}")
def delete_transaksi(
    tipe: str,
    pk_value: int,
    x_api_key: Optional[str] = Header(None),
    db: Session = Depends(get_db),
):
    if not verify_api_key(x_api_key):
        return ApiResponse(status_code="101", status="API KEY Invalid !")
    ok, error = service.delete_transaksi(db, tipe, pk_value)
    if error:
        return ApiResponse(status_code="400", status=error)
    if not ok:
        return ApiResponse(status_code="404", status="Data tidak ditemukan")
    return ApiResponse(message="Data deleted successfully !")


# ======================================================================
# PENGAJUAN CRUD
# ======================================================================

@router.get("/admin/pengajuan/list")
def list_pengajuan(
    page: int = Query(1, ge=1),
    per_page: int = Query(10, ge=1),
    x_api_key: Optional[str] = Header(None),
    db: Session = Depends(get_db),
):
    if not verify_api_key(x_api_key):
        return ApiResponse(status_code="101", status="API KEY Invalid !")
    result = service.list_pengajuan(db, page, per_page)
    return ApiResponse(data=result["data"], total=result["total"])


@router.post("/admin/pengajuan/create")
def create_pengajuan(
    data: Dict[str, Any] = Body(...),
    x_api_key: Optional[str] = Header(None),
    db: Session = Depends(get_db),
):
    if not verify_api_key(x_api_key):
        return ApiResponse(status_code="101", status="API KEY Invalid !")
    result = service.create_pengajuan(db, data)
    if "error" in result:
        return ApiResponse(status_code="500", status=result["error"])
    # Response berisi kode masjid + slug yang diterbitkan langsung, agar pemohon
    # bisa lanjut ke langkah 2 (daftar admin masjid) dengan kode tsb.
    return ApiResponse(status_code="000", status="Sukses", data=result)


@router.put("/admin/pengajuan/update/{pk_value}")
def update_pengajuan(
    pk_value: int,
    data: Dict[str, Any] = Body(...),
    x_api_key: Optional[str] = Header(None),
    db: Session = Depends(get_db),
):
    if not verify_api_key(x_api_key):
        return ApiResponse(status_code="101", status="API KEY Invalid !")
    status_req = str((data or {}).get("status_pengajuan", "")).lower()
    result = service.update_pengajuan(db, pk_value, data)
    if not result:
        return ApiResponse(status_code="404", status="Data tidak ditemukan")
    if "error" in result:
        return ApiResponse(status_code="400", status=result["error"])
    # Saat disetujui, response menyertakan kode masjid (aktivasi masjid + admin)
    if status_req == "disetujui":
        kode = result.get("kode_org_baznas")
        return ApiResponse(status_code="000", status="Sukses", data={"kode_org_baznas": kode})
    return ApiResponse(status_code="000", status="Sukses")


@router.delete("/admin/pengajuan/delete/{pk_value}")
def delete_pengajuan(
    pk_value: int,
    x_api_key: Optional[str] = Header(None),
    db: Session = Depends(get_db),
):
    if not verify_api_key(x_api_key):
        return ApiResponse(status_code="101", status="API KEY Invalid !")
    if not service.delete_pengajuan(db, pk_value):
        return ApiResponse(status_code="404", status="Data tidak ditemukan")
    return ApiResponse(message="Data deleted successfully !")


# ======================================================================
# BULK SYNC DETAIL
# ======================================================================

@router.post("/admin/masjid/{id_masjid}/sync-detail")
def sync_masjid_detail(
    id_masjid: str,
    data: Dict[str, List[Dict[str, Any]]] = Body(...),
    x_api_key: Optional[str] = Header(None),
    db: Session = Depends(get_db),
):
    if not verify_api_key(x_api_key):
        return ApiResponse(status_code="101", status="API KEY Invalid !")
    results = service.sync_masjid_detail(db, id_masjid, data)
    return ApiResponse(data=results)
