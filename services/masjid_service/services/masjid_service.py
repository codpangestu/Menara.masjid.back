from fastapi import HTTPException
from sqlalchemy.orm import Session
from typing import Optional
from services.masjid_service.queries.masjid_queries import (
    get_masjid_by_id, get_masjid_by_slug, get_list_masjid,
    get_masjid_by_wilayah, get_pengurus_by_masjid, search_masjid_public,
)
from services.masjid_service.queries.rekap_queries import get_rekap_penerimaan, get_rekap_pengeluaran, get_rekap_by_masjid
from shared.schemas.base import model_to_dict


class MasjidService:
    def get_detail(self, db: Session, id_masjid: str):
        masjid = get_masjid_by_id(db, id_masjid)
        if not masjid:
            raise HTTPException(status_code=404, detail="Masjid tidak ditemukan")
        return model_to_dict(masjid)

    def get_list(self, db: Session, page: int = 1, per_page: int = 10,
                 kode_org_baznas: Optional[str] = None,
                 id_provinsi: Optional[int] = None,
                 id_kabupaten_kota: Optional[int] = None,
                 keyword_nama: Optional[str] = None,
                 keyword_alamat: Optional[str] = None,
                 keyword_label: Optional[str] = None) -> dict:
        data, total = get_list_masjid(
            db, page, per_page, kode_org_baznas, id_provinsi,
            id_kabupaten_kota, keyword_nama, keyword_alamat, keyword_label,
        )
        items = [
            {
                "id_masjid": m.id_masjid,
                "nama_masjid": m.nama_masjid,
                "kode_org_baznas": m.kode_org_baznas,
                "jenis_masjid": m.jenis_masjid,
                "tipologi": m.tipologi,
                "alamat_masjid": m.alamat_masjid,
                "slug_masjid": m.slug_masjid,
                "daya_tampung": m.daya_tampung,
                "label_upz": m.label_upz,
                "id_provinsi": m.id_provinsi,
                "id_kabupaten_kota": m.id_kabupaten_kota,
            }
            for m in data
        ]
        return {"data": items, "total": total, "page": page, "per_page": per_page}

    def get_by_wilayah(self, db: Session, id_provinsi: int,
                       id_kabupaten_kota: Optional[int] = None,
                       keyword_nama_masjid: Optional[str] = None,
                       keyword_alamat_masjid: Optional[str] = None,
                       keyword_label_masjid: Optional[str] = None,
                       page: int = 1, per_page: int = 10) -> list:
        return get_masjid_by_wilayah(
            db, id_provinsi, id_kabupaten_kota, keyword_nama_masjid,
            keyword_alamat_masjid, keyword_label_masjid, page, per_page,
        )

    def get_pengurus(self, db: Session, id_masjid: str) -> list:
        results = get_pengurus_by_masjid(db, id_masjid)
        data = []
        for u, lv, lb, m in results:
            data.append({
                "id_user": u.id_user,
                "nama": u.nama,
                "email": u.email,
                "nama_level": lv.nama_level if lv else None,
                "nama_labels": lb.nama_labels if lb else None,
                "id_jalur_akses": u.id_jalur_akses,
                "nama_masjid": m.nama_masjid if m else None,
            })
        return data

    def search_public(self, db: Session, nama: Optional[str] = None,
                      jenis: Optional[str] = None,
                      tipologi: Optional[str] = None,
                      id_provinsi: Optional[int] = None,
                      id_kabupaten_kota: Optional[int] = None,
                      id_kecamatan: Optional[int] = None) -> list:
        return search_masjid_public(
            db, nama, jenis, tipologi, id_provinsi, id_kabupaten_kota, id_kecamatan,
        )

    def get_rekap_penerimaan(self, db: Session, **kwargs):
        return get_rekap_penerimaan(db, **kwargs)

    def get_rekap_pengeluaran(self, db: Session, **kwargs):
        return get_rekap_pengeluaran(db, **kwargs)

    def get_rekap_by_masjid(self, db: Session, id_masjid: str, **kwargs):
        return get_rekap_by_masjid(db, id_masjid, **kwargs)
