from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import Optional
from shared.config.database import get_db
from services.content_service.services.content_service import ContentService
from shared.utils.response_helper import ApiResponse

router = APIRouter()
service = ContentService()


# ===== HOME / BERANDA =====

@router.get("/home")
def get_home_data(db: Session = Depends(get_db)):
    data = service.get_home(db)
    return ApiResponse(data=data)


# ===== INFORMASI =====

@router.get("/informasi")
def list_informasi(
    page: int = Query(1, ge=1),
    per_page: int = Query(10, ge=1),
    db: Session = Depends(get_db),
):
    result = service.get_informasi(db, page, per_page)
    return ApiResponse(**result)


@router.get("/informasi/{slug}")
def detail_informasi(slug: str, db: Session = Depends(get_db)):
    data = service.get_detail_informasi(db, slug)
    if not data:
        return ApiResponse(status_code="404", status="Tidak ditemukan")
    return ApiResponse(data=data)


# ===== KAJIAN =====

@router.get("/kajian")
def list_kajian(
    tema: Optional[int] = None,
    judul: Optional[str] = None,
    page: int = Query(1, ge=1),
    per_page: int = Query(10, ge=1),
    db: Session = Depends(get_db),
):
    result = service.get_kajian(db, tema, judul, page, per_page)
    return ApiResponse(**result)


@router.get("/kajian/{slug}")
def detail_kajian(slug: str, db: Session = Depends(get_db)):
    data = service.get_detail_kajian(db, slug)
    if not data:
        return ApiResponse(status_code="404", status="Tidak ditemukan")
    return ApiResponse(data=data)


# ===== ACARA, CERITA, DONASI, POSTINGAN, PENGUMUMAN =====

_CONTENT_TYPES = ["acara", "cerita", "donasi", "postingan", "pengumuman"]


def _make_list_ep(content_type: str):
    def handler(
        kategori: Optional[int] = None,
        judul: Optional[str] = None,
        db: Session = Depends(get_db),
    ):
        data = service.get_content_list(db, content_type, kategori, judul)
        return ApiResponse(data=data)
    return handler


def _make_detail_ep(content_type: str):
    def handler(slug: str, db: Session = Depends(get_db)):
        data = service.get_content_detail(db, content_type, slug)
        if not data:
            return ApiResponse(status_code="404", status="Tidak ditemukan")
        return ApiResponse(data=data)
    return handler


for ct in _CONTENT_TYPES:
    router.get(f"/{ct}")(_make_list_ep(ct))
    router.get(f"/{ct}/{{slug}}")(_make_detail_ep(ct))


# ===== PANDUAN =====

@router.get("/panduan-pengguna")
def list_panduan_pengguna(
    kategori: Optional[int] = None,
    judul: Optional[str] = None,
    db: Session = Depends(get_db),
):
    data = service.get_guide_list(db, "panduan-pengguna", kategori, judul)
    return ApiResponse(data=data)


@router.get("/panduan-pengguna/{slug}")
def detail_panduan_pengguna(slug: str, db: Session = Depends(get_db)):
    data = service.get_guide_detail(db, "panduan-pengguna", slug)
    if not data:
        return ApiResponse(status_code="404", status="Tidak ditemukan")
    return ApiResponse(data=data)


@router.get("/panduan-pengelola")
def list_panduan_pengelola(
    kategori: Optional[int] = None,
    judul: Optional[str] = None,
    db: Session = Depends(get_db),
):
    data = service.get_guide_list(db, "panduan-pengelola", kategori, judul)
    return ApiResponse(data=data)


@router.get("/panduan-pengelola/{slug}")
def detail_panduan_pengelola(slug: str, db: Session = Depends(get_db)):
    data = service.get_guide_detail(db, "panduan-pengelola", slug)
    if not data:
        return ApiResponse(status_code="404", status="Tidak ditemukan")
    return ApiResponse(data=data)


# ===== MASJID PUBLIC DETAIL =====

@router.get("/masjid/{slug}")
def public_masjid_detail(slug: str, db: Session = Depends(get_db)):
    data = service.get_masjid_public_detail(db, slug)
    if not data:
        return ApiResponse(status_code="404", status="Masjid tidak ditemukan")
    return ApiResponse(data=data)


@router.get("/masjid/search")
def search_masjid(
    nama: Optional[str] = None,
    jenis: Optional[str] = None,
    tipologi: Optional[str] = None,
    id_provinsi: Optional[int] = None,
    id_kabupaten_kota: Optional[int] = None,
    id_kecamatan: Optional[int] = None,
    db: Session = Depends(get_db),
):
    data = service.get_masjid_public_detail_by_search(
        db, nama, jenis, tipologi, id_provinsi, id_kabupaten_kota, id_kecamatan,
    )
    return ApiResponse(data=data)


# ===== DYNAMIC CONTENT ROUTES =====

_DYNAMIC_PREFIXES = [
    "repository", "dokumentasi-pengembangan", "dokumentasi-pengujian",
    "dokumentasi-sosialisasi", "info-pemberitahuan", "infografis",
    "inspirasi", "infovideo", "infoayat", "infohadits", "infodoa",
]


def _make_dynamic_list_ep(prefix: str):
    def handler(
        page: int = Query(1, ge=1),
        per_page: int = Query(10, ge=1),
        db: Session = Depends(get_db),
    ):
        data = service.get_dynamic_list(db, prefix, page, per_page)
        return ApiResponse(data=data)
    return handler


def _make_dynamic_detail_ep(prefix: str):
    def handler(slug: str, db: Session = Depends(get_db)):
        data = service.get_dynamic_detail(db, prefix, slug)
        if not data:
            return ApiResponse(status_code="404", status="Tidak ditemukan")
        return ApiResponse(data=data)
    return handler


for prefix in _DYNAMIC_PREFIXES:
    router.get(f"/{prefix}")(_make_dynamic_list_ep(prefix))
    router.get(f"/{prefix}/{{slug}}")(_make_dynamic_detail_ep(prefix))
