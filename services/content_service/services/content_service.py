from sqlalchemy.orm import Session
from typing import Optional
from services.content_service.queries.content_queries import (
    get_home_data, get_masjid_public_detail,
    list_informasi, detail_informasi,
    list_kajian, detail_kajian,
    list_content_with_filters, detail_content,
    list_guide, detail_guide,
    list_dynamic_content, detail_dynamic_content,
)
from services.masjid_service.queries.masjid_queries import search_masjid_public
from shared.schemas.base import model_to_dict


class ContentService:
    def get_home(self, db: Session) -> dict:
        raw = get_home_data(db)
        return {
            "informasi": [self._format_content(i, "informasi") for i in raw["informasi"]],
            "repository": [self._format_content(r, "repository") for r in raw["repository"]],
            "dokumentasi_pengembangan": [self._format_content(d, "dokumentasi_pengembangan") for d in raw["dokumentasi_pengembangan"]],
            "dokumentasi_pengujian": [self._format_content(d, "dokumentasi_pengujian") for d in raw["dokumentasi_pengujian"]],
            "dokumentasi_sosialisasi": [self._format_content(d, "dokumentasi_sosialisasi") for d in raw["dokumentasi_sosialisasi"]],
            "postingan": [self._format_content(p, "postingan") for p in raw["postingan"]],
            "panduan_pengguna": [self._format_content(p, "panduan_pengguna") for p in raw["panduan_pengguna"]],
            "panduan_pengelola": [self._format_content(p, "panduan_pengelola") for p in raw["panduan_pengelola"]],
            "masjid": [self._format_masjid_simple(m) for m in raw["masjid"]],
            "info_pemberitahuan": [self._format_content(i, "info_pemberitahuan") for i in raw["info_pemberitahuan"]],
            "infografis": [self._format_content(i, "infografis") for i in raw["infografis"]],
            "inspirasi": [self._format_content(i, "inspirasi") for i in raw["inspirasi"]],
            "infovideo": [self._format_content(i, "infovideo") for i in raw["infovideo"]],
            "infoayat": [self._format_content(i, "infoayat") for i in raw["infoayat"]],
            "infohadits": [self._format_content(i, "infohadits") for i in raw["infohadits"]],
            "infodoa": [self._format_content(i, "infodoa") for i in raw["infodoa"]],
        }

    def get_informasi(self, db: Session, page: int = 1, per_page: int = 10) -> dict:
        data, total = list_informasi(db, page, per_page)
        return {
            "data": [self._format_content(i, "informasi") for i in data],
            "total": total, "page": page, "per_page": per_page,
        }

    def get_detail_informasi(self, db: Session, slug: str):
        result = detail_informasi(db, slug)
        if not result:
            return None
        return self._format_content(result, "informasi")

    def get_kajian(self, db: Session, tema=None, judul=None, page=1, per_page=10) -> dict:
        data, total = list_kajian(db, tema, judul, page, per_page)
        return {
            "data": [self._format_content(k, "kajian") for k in data],
            "total": total,
        }

    def get_detail_kajian(self, db: Session, slug: str):
        result = detail_kajian(db, slug)
        if not result:
            return None
        return self._format_content(result, "kajian")

    def get_content_list(self, db: Session, content_type: str, kategori=None, judul=None) -> list:
        data = list_content_with_filters(db, content_type, kategori, judul)
        return [self._format_content(d, content_type) for d in data]

    def get_content_detail(self, db: Session, content_type: str, slug: str):
        result = detail_content(db, content_type, slug)
        if not result:
            return None
        return self._format_content(result, content_type)

    def get_guide_list(self, db: Session, guide_type: str, kategori=None, judul=None) -> list:
        data = list_guide(db, guide_type, kategori, judul)
        return [self._format_content(d, guide_type.replace("-", "_")) for d in data]

    def get_guide_detail(self, db: Session, guide_type: str, slug: str):
        result = detail_guide(db, guide_type, slug)
        if not result:
            return None
        return self._format_content(result, guide_type.replace("-", "_"))

    def get_dynamic_list(self, db: Session, prefix: str, page=1, per_page=10) -> list:
        data = list_dynamic_content(db, prefix, page, per_page)
        return [self._format_content(d, prefix.replace("-", "_")) for d in data]

    def get_dynamic_detail(self, db: Session, prefix: str, slug: str):
        result = detail_dynamic_content(db, prefix, slug)
        if not result:
            return None
        return self._format_content(result, prefix.replace("-", "_"))

    def get_masjid_public_detail_by_search(
        self, db: Session,
        nama=None, jenis=None, tipologi=None,
        id_provinsi=None, id_kabupaten_kota=None, id_kecamatan=None,
    ) -> list:
        data = search_masjid_public(
            db, nama, jenis, tipologi, id_provinsi, id_kabupaten_kota, id_kecamatan,
        )
        return [model_to_dict(m) for m in data]

    def get_masjid_public_detail(self, db: Session, slug: str):
        from services.masjid_service.queries.masjid_queries import get_masjid_by_slug
        m = get_masjid_by_slug(db, slug)
        if not m:
            return None

        related = get_masjid_public_detail(db, m.id_masjid)
        data = self._format_masjid_simple(m)
        data.update({
            "fasilitas": [{"id": f.id_fasilitas, "nama": f.nama_fasilitas, "foto": f.foto_fasilitas, "keterangan": f.keterangan} for f in related["fasilitas"]],
            "foto": [{"id": f.id, "nama": f.name, "src": f.src} for f in related["foto"]],
            "dokumen": [{"id": d.id, "nama": d.document_name, "tipe": d.document_type, "src": d.document_src} for d in related["dokumen"]],
            "bank": [{"id": b.id_bank, "nama": b.nama_bank, "norek": b.norek, "atas_nama": b.atas_nama} for b in related["bank"]],
            "medsos": [{"id": m2.id_medsos, "nama": m2.name_medsos, "link": m2.url_medsos} for m2 in related["medsos"]],
            "struktur": [{"id": s.id_struktur, "nama": s.nama_struktur, "foto": s.foto_struktur, "jenis": s.jenis_struktur} for s in related["struktur"]],
            "kegiatan": [{"id": k.id_kegiatan, "nama": k.nama_kegiatan, "foto": k.foto_kegiatan, "jenis": k.jenis_kegiatan} for k in related["kegiatan"]],
            "kajian": [self._format_content(d, "kajian") for d in related["kajian"]],
            "acara": [self._format_content(d, "acara") for d in related["acara"]],
            "cerita": [self._format_content(d, "cerita") for d in related["cerita"]],
            "donasi": [self._format_content(d, "donasi") for d in related["donasi"]],
            "postingan": [self._format_content(d, "postingan") for d in related["postingan"]],
        })
        return data

    def _format_content(self, item, tipe: str) -> dict:
        """Format content item to dict based on type."""
        if not item:
            return {}

        pk_columns = list(item.__table__.primary_key.columns.keys())
        base = {"id": getattr(item, pk_columns[0], None) if pk_columns else None}

        for attr in ["judul", "judul_informasi", "judul_repository", "judul_info_pemberitahuan",
                     "judul_infografis", "judul_inspirasi", "judul_infovideo", "judul_infoayat",
                     "judul_infohadits", "judul_infodoa", "judul_video", "nama"]:
            val = getattr(item, attr, None)
            if val:
                base["judul" if "judul" in attr or attr == "nama" else attr] = val
                break

        for attr in ["keterangan", "isi_informasi", "isi_repository", "isi",
                     "deskripsi", "deskripsi_saran_dan_masukan", "isi_info_pemberitahuan",
                     "isi_infografis", "isi_inspirasi", "isi_infovideo", "isi_infoayat",
                     "isi_infohadits", "isi_infodoa"]:
            val = getattr(item, attr, None)
            if val:
                base["isi"] = val
                break

        for attr in ["foto_informasi", "foto_repository", "foto_dokumentasi_pengembangan",
                     "poster", "thumbnail", "foto_fasilitas", "foto_kegiatan", "foto_struktur",
                     "gambar_logo", "gambar_mitra_kerjasama", "gambar_qris", "avatar", "src",
                     "foto_info_pemberitahuan", "foto_infografis", "foto_inspirasi",
                     "foto_infovideo", "foto_infoayat", "foto_infohadits", "foto_infodoa"]:
            val = getattr(item, attr, None)
            if val:
                base["foto"] = val
                break

        for attr in ["created_at", "upload_time", "tgl_kajian", "tgl_acara", "tgl_cerita",
                     "tgl_donasi", "tgl_postingan", "tgl_pengumuman", "tgl_video", "tanggal"]:
            val = getattr(item, attr, None)
            if val:
                base["tanggal"] = str(val)
                break

        for attr in ["slug_masjid", "slug_kajian", "slug_acara", "slug_cerita", "slug_donasi",
                     "slug_postingan", "slug_panduan_pengguna", "slug_panduan_pengelola",
                     "slug_pengumuman", "slug_repository", "slug_dokumentasi_pengembangan",
                     "slug_dokumentasi_pengujian", "slug_dokumentasi_sosialisasi", "slug_informasi",
                     "slug_info_pemberitahuan", "slug_infografis", "slug_inspirasi",
                     "slug_infovideo", "slug_infoayat", "slug_infohadits", "slug_infodoa",
                     "slug_video"]:
            val = getattr(item, attr, None)
            if val:
                base["slug"] = val
                break

        for attr in ["pemateri", "penulis"]:
            val = getattr(item, attr, None)
            if val:
                base["penulis"] = val
                break

        base["tipe"] = tipe
        return base

    def _format_masjid_simple(self, m) -> dict:
        """Format masjid to simple dict."""
        if not m:
            return {}
        return {
            "id_masjid": m.id_masjid,
            "nama_masjid": m.nama_masjid,
            "slug_masjid": m.slug_masjid,
            "jenis_masjid": m.jenis_masjid,
            "tipologi": m.tipologi,
            "alamat_masjid": m.alamat_masjid,
            "thumbnail": m.thumbnail,
            "deskripsi": m.deskripsi,
            "background_warna_website": m.background_warna_website,
            "warna_tulisan_website": m.warna_tulisan_website,
            "running_text_website": m.running_text_website,
            "nohp_masjid": m.nohp_masjid,
            "email_masjid": m.email_masjid,
            "id_provinsi": m.id_provinsi,
            "id_kabupaten_kota": m.id_kabupaten_kota,
            "id_kecamatan": m.id_kecamatan,
            "id_kelurahan_desa": m.id_kelurahan_desa,
        }
