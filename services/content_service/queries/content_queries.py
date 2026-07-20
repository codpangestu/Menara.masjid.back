from sqlalchemy.orm import Session
from typing import Optional
from shared.models.content import (
    Informasi, Kajian, Acara, Cerita, Donasi, Postingan,
    PanduanPengguna, PanduanPengelola, Pengumuman,
    Repository, DokumentasiPengembangan, DokumentasiPengujian,
    DokumentasiSosialisasi, InfoPemberitahuan, Infografis,
    Inspirasi, Infovideo, Infoayat, Infohadits, Infodoa,
)
from shared.models.masjid_detail import (
    Fasilitas, Images, Document, Bank, Medsos, Struktur, Kegiatan,
)
from shared.models.masjid import Masjid


def get_home_data(db: Session) -> dict:
    info = db.query(Informasi).order_by(Informasi.id_informasi.desc()).limit(6).all()
    repo = db.query(Repository).order_by(Repository.id_repository.desc()).limit(6).all()
    dok_pengembangan = db.query(DokumentasiPengembangan).order_by(DokumentasiPengembangan.id_dokumentasi_pengembangan.desc()).limit(6).all()
    dok_pengujian = db.query(DokumentasiPengujian).order_by(DokumentasiPengujian.id_dokumentasi_pengujian.desc()).limit(6).all()
    dok_sosialisasi = db.query(DokumentasiSosialisasi).order_by(DokumentasiSosialisasi.id_dokumentasi_sosialisasi.desc()).limit(6).all()
    postingan = db.query(Postingan).filter(Postingan.status_aktif == 1).order_by(Postingan.id_postingan.desc()).limit(14).all()
    panduan_pengguna = db.query(PanduanPengguna).order_by(PanduanPengguna.id_panduan_pengguna.desc()).limit(1).all()
    panduan_pengelola = db.query(PanduanPengelola).order_by(PanduanPengelola.id_panduan_pengelola.desc()).limit(1).all()
    masjid = db.query(Masjid).order_by(Masjid.id_masjid.desc()).limit(3).all()
    info_pemberitahuan = db.query(InfoPemberitahuan).order_by(InfoPemberitahuan.id_info_pemberitahuan.desc()).limit(1).all()
    infografis = db.query(Infografis).order_by(Infografis.id_infografis.desc()).limit(1).all()
    inspirasi = db.query(Inspirasi).order_by(Inspirasi.id_inspirasi.desc()).limit(1).all()
    infovideo = db.query(Infovideo).order_by(Infovideo.id_infovideo.desc()).limit(1).all()
    infoayat = db.query(Infoayat).order_by(Infoayat.id_infoayat.desc()).limit(1).all()
    infohadits = db.query(Infohadits).order_by(Infohadits.id_infohadits.desc()).limit(1).all()
    infodoa = db.query(Infodoa).order_by(Infodoa.id_infodoa.desc()).limit(1).all()

    return {
        "informasi": info,
        "repository": repo,
        "dokumentasi_pengembangan": dok_pengembangan,
        "dokumentasi_pengujian": dok_pengujian,
        "dokumentasi_sosialisasi": dok_sosialisasi,
        "postingan": postingan,
        "panduan_pengguna": panduan_pengguna,
        "panduan_pengelola": panduan_pengelola,
        "masjid": masjid,
        "info_pemberitahuan": info_pemberitahuan,
        "infografis": infografis,
        "inspirasi": inspirasi,
        "infovideo": infovideo,
        "infoayat": infoayat,
        "infohadits": infohadits,
        "infodoa": infodoa,
    }


def get_masjid_public_detail(db: Session, id_masjid: str) -> dict:

    fasilitas = db.query(Fasilitas).filter(Fasilitas.parent_id == id_masjid).all()
    foto = db.query(Images).filter(Images.parent_id == id_masjid).all()
    dokumen = db.query(Document).filter(Document.parent_id == id_masjid).all()
    bank = db.query(Bank).filter(Bank.parent_id == id_masjid).all()
    medsos = db.query(Medsos).filter(Medsos.parent_id == id_masjid).all()
    struktur = db.query(Struktur).filter(Struktur.parent_id == id_masjid).all()
    kegiatan = db.query(Kegiatan).filter(Kegiatan.parent_id == id_masjid).all()
    kajian = db.query(Kajian).filter(Kajian.id_masjid == id_masjid).all()
    acara = db.query(Acara).filter(Acara.id_masjid == id_masjid).all()
    cerita = db.query(Cerita).filter(Cerita.id_masjid == id_masjid).all()
    donasi = db.query(Donasi).filter(Donasi.id_masjid == id_masjid).all()
    postingan = db.query(Postingan).filter(Postingan.id_masjid == id_masjid).all()

    return {
        "fasilitas": fasilitas,
        "foto": foto,
        "dokumen": dokumen,
        "bank": bank,
        "medsos": medsos,
        "struktur": struktur,
        "kegiatan": kegiatan,
        "kajian": kajian,
        "acara": acara,
        "cerita": cerita,
        "donasi": donasi,
        "postingan": postingan,
    }


def list_informasi(db: Session, page: int = 1, per_page: int = 10) -> tuple:
    q = db.query(Informasi).order_by(Informasi.id_informasi.desc())
    total = q.count()
    data = q.offset((page - 1) * per_page).limit(per_page).all()
    return data, total


def detail_informasi(db: Session, slug: str) -> Informasi | None:
    return db.query(Informasi).filter(Informasi.slug_informasi == slug).first()


def list_kajian(db: Session, tema: Optional[int] = None, judul: Optional[str] = None, page: int = 1, per_page: int = 10) -> tuple:
    q = db.query(Kajian).filter(Kajian.status_aktif == 1)
    if tema:
        q = q.filter(Kajian.id_tema == tema)
    if judul:
        q = q.filter(Kajian.judul.like(f"%{judul}%"))
    total = q.count()
    data = q.order_by(Kajian.tgl_kajian.desc()).offset((page - 1) * per_page).limit(per_page).all()
    return data, total


def detail_kajian(db: Session, slug: str) -> Kajian | None:
    return db.query(Kajian).filter(Kajian.slug_kajian == slug).first()


_CONTENT_LIST_MODELS = {
    "acara": (Acara, "status_aktif", "id_kategori_acara", "judul", "tgl_acara"),
    "cerita": (Cerita, "status_aktif", "id_kategori_cerita", "judul", "tgl_cerita"),
    "donasi": (Donasi, "status_aktif", "id_kategori_donasi", "judul", "tgl_donasi"),
    "postingan": (Postingan, "status_aktif", "id_kategori_postingan", "judul", "tgl_postingan"),
    "pengumuman": (Pengumuman, "status_aktif", "id_kategori_pengumuman", "judul", "tgl_pengumuman"),
}

_CONTENT_DETAIL_MAP = {
    "acara": (Acara, "slug_acara"),
    "cerita": (Cerita, "slug_cerita"),
    "donasi": (Donasi, "slug_donasi"),
    "postingan": (Postingan, "slug_postingan"),
    "pengumuman": (Pengumuman, "slug_pengumuman"),
}

_CONTENT_GUIDE_MAP = {
    "panduan-pengguna": (PanduanPengguna, "slug_panduan_pengguna", "id_kategori_panduan_pengguna", PanduanPengguna.created_at),
    "panduan-pengelola": (PanduanPengelola, "slug_panduan_pengelola", "id_kategori_panduan_pengelola", PanduanPengelola.created_at),
}

_DYNAMIC_CONTENT_MAP = {
    "repository": (Repository, "slug_repository", "id_repository"),
    "dokumentasi-pengembangan": (DokumentasiPengembangan, "slug_dokumentasi_pengembangan", "id_dokumentasi_pengembangan"),
    "dokumentasi-pengujian": (DokumentasiPengujian, "slug_dokumentasi_pengujian", "id_dokumentasi_pengujian"),
    "dokumentasi-sosialisasi": (DokumentasiSosialisasi, "slug_dokumentasi_sosialisasi", "id_dokumentasi_sosialisasi"),
    "info-pemberitahuan": (InfoPemberitahuan, "slug_info_pemberitahuan", "id_info_pemberitahuan"),
    "infografis": (Infografis, "slug_infografis", "id_infografis"),
    "inspirasi": (Inspirasi, "slug_inspirasi", "id_inspirasi"),
    "infovideo": (Infovideo, "slug_infovideo", "id_infovideo"),
    "infoayat": (Infoayat, "slug_infoayat", "id_infoayat"),
    "infohadits": (Infohadits, "slug_infohadits", "id_infohadits"),
    "infodoa": (Infodoa, "slug_infodoa", "id_infodoa"),
}


def list_content_with_filters(
    db: Session, content_type: str,
    kategori: Optional[int] = None, judul: Optional[str] = None,
) -> list:
    if content_type not in _CONTENT_LIST_MODELS:
        return []
    model, status_field, kategori_field, _, order_field = _CONTENT_LIST_MODELS[content_type]
    q = db.query(model).filter(getattr(model, status_field) == 1)
    if kategori:
        q = q.filter(getattr(model, kategori_field) == kategori)
    if judul:
        q = q.filter(getattr(model, "judul").like(f"%{judul}%"))
    return q.order_by(getattr(model, order_field).desc()).all()


def detail_content(db: Session, content_type: str, slug: str):
    if content_type not in _CONTENT_DETAIL_MAP:
        return None
    model, slug_field = _CONTENT_DETAIL_MAP[content_type]
    return db.query(model).filter(getattr(model, slug_field) == slug).first()


def list_guide(db: Session, guide_type: str, kategori: Optional[int] = None, judul: Optional[str] = None) -> list:
    if guide_type not in _CONTENT_GUIDE_MAP:
        return []
    model, _, kategori_field, order_field = _CONTENT_GUIDE_MAP[guide_type]
    q = db.query(model).filter(model.status_aktif == 1)
    if kategori:
        q = q.filter(getattr(model, kategori_field) == kategori)
    if judul:
        q = q.filter(model.judul.like(f"%{judul}%"))
    return q.order_by(order_field.desc()).all()


def detail_guide(db: Session, guide_type: str, slug: str):
    if guide_type not in _CONTENT_GUIDE_MAP:
        return None
    model, slug_field, _, _ = _CONTENT_GUIDE_MAP[guide_type]
    return db.query(model).filter(getattr(model, slug_field) == slug).first()


def list_dynamic_content(db: Session, prefix: str, page: int = 1, per_page: int = 10) -> list:
    if prefix not in _DYNAMIC_CONTENT_MAP:
        return []
    model, _, id_field = _DYNAMIC_CONTENT_MAP[prefix]
    return db.query(model).order_by(getattr(model, id_field).desc()).offset((page - 1) * per_page).limit(per_page).all()


def detail_dynamic_content(db: Session, prefix: str, slug: str):
    if prefix not in _DYNAMIC_CONTENT_MAP:
        return None
    model, slug_field, _ = _DYNAMIC_CONTENT_MAP[prefix]
    return db.query(model).filter(getattr(model, slug_field) == slug).first()
