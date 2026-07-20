from sqlalchemy.orm import Session
from typing import Any, Dict, List, Optional
from services.admin_service.queries.admin_queries import create_record, update_record, delete_record, list_pengajuan, sync_masjid_detail_replace
from shared.models.masjid import Masjid
from shared.models.content import (
    Informasi, Kajian, Acara, Cerita, Donasi, Postingan,
    PanduanPengguna, PanduanPengelola, Pengumuman,
    Repository, DokumentasiPengembangan, DokumentasiPengujian,
    DokumentasiSosialisasi, InfoPemberitahuan, Infografis,
    Inspirasi, Infovideo, Infoayat, Infohadits, Infodoa,
)
from shared.models.master import (
    Levels, Labels, JenisDana, JenisHarta, JenisLaporan,
    JenisPerolehanAset, LabelInfoDana, Tema,
    KategoriAcara, KategoriCerita, KategoriDonasi, KategoriPostingan,
    KategoriPanduanPengguna, KategoriPanduanPengelola, KategoriMenaraVideo,
)
from shared.models.transaksi import (
    BukukasPenerimaan, BukukasPengeluaran, Kas, Coa,
    BukuAset, BerkasLaporan, SaranDanMasukan,
)
from shared.models.masjid_detail import (
    Fasilitas, Images, Document, Bank, Medsos, Logo,
    MitraKerjasama, Qris, Struktur, Kegiatan, Videos,
)
from shared.models.wilayah import Provinsi, KabupatenKota, Kecamatan, KelurahanDesa
from shared.models.pengajuan import PengajuanMasjid
from shared.schemas.base import model_to_dict
from shared.utils.response_helper import ApiResponse


class AdminService:
    _CONTENT_MODELS = {
        "informasi": Informasi, "kajian": Kajian, "acara": Acara,
        "cerita": Cerita, "donasi": Donasi, "postingan": Postingan,
        "panduan-pengguna": PanduanPengguna, "panduan-pengelola": PanduanPengelola,
        "pengumuman": Pengumuman, "repository": Repository,
        "dokumentasi-pengembangan": DokumentasiPengembangan,
        "dokumentasi-pengujian": DokumentasiPengujian,
        "dokumentasi-sosialisasi": DokumentasiSosialisasi,
        "info-pemberitahuan": InfoPemberitahuan, "infografis": Infografis,
        "inspirasi": Inspirasi, "infovideo": Infovideo,
        "infoayat": Infoayat, "infohadits": Infohadits, "infodoa": Infodoa,
    }

    _MASTER_MODELS = {
        "levels": Levels, "labels": Labels, "jenis-dana": JenisDana,
        "jenis-harta": JenisHarta, "jenis-laporan": JenisLaporan,
        "jenis-perolehan-aset": JenisPerolehanAset, "label-info-dana": LabelInfoDana,
        "tema": Tema, "kategori-acara": KategoriAcara, "kategori-cerita": KategoriCerita,
        "kategori-donasi": KategoriDonasi, "kategori-postingan": KategoriPostingan,
        "kategori-panduan-pengguna": KategoriPanduanPengguna,
        "kategori-panduan-pengelola": KategoriPanduanPengelola,
        "kategori-menara-video": KategoriMenaraVideo,
    }

    _WILAYAH_MODELS = {
        "provinsi": Provinsi, "kabupaten-kota": KabupatenKota,
        "kecamatan": Kecamatan, "kelurahan-desa": KelurahanDesa,
    }

    _DETAIL_MODELS = {
        "fasilitas": Fasilitas, "images": Images, "dokumen": Document,
        "bank": Bank, "medsos": Medsos, "logo": Logo,
        "mitra-kerjasama": MitraKerjasama, "qris": Qris,
        "struktur": Struktur, "kegiatan": Kegiatan, "videos": Videos,
    }

    _TRANSAKSI_MODELS = {
        "bukukas-penerimaan": BukukasPenerimaan,
        "bukukas-pengeluaran": BukukasPengeluaran,
        "kas": Kas, "coa": Coa, "buku-aset": BukuAset,
        "berkas-laporan": BerkasLaporan, "saran-masukan": SaranDanMasukan,
    }

    # --- Masjid CRUD ---
    def create_masjid(self, db: Session, data: dict) -> dict:
        obj = create_record(db, Masjid, data)
        from services.admin_service.queries.admin_queries import _get_pk
        pk = _get_pk(Masjid)
        return {pk: getattr(obj, pk)}

    def update_masjid(self, db: Session, id_masjid: str, data: dict) -> bool:
        obj = update_record(db, Masjid, id_masjid, data)
        return obj is not None

    def delete_masjid(self, db: Session, id_masjid: str) -> bool:
        return delete_record(db, Masjid, id_masjid)

    # --- Content CRUD ---
    def create_content(self, db: Session, tipe: str, data: dict):
        if tipe not in self._CONTENT_MODELS:
            return None, f"Tipe konten '{tipe}' tidak dikenal"
        model = self._CONTENT_MODELS[tipe]
        obj = create_record(db, model, data)
        from services.admin_service.queries.admin_queries import _get_pk
        pk = _get_pk(model)
        return {pk: getattr(obj, pk)}, None

    def update_content(self, db: Session, tipe: str, pk_value: Any, data: dict):
        if tipe not in self._CONTENT_MODELS:
            return None, f"Tipe konten '{tipe}' tidak dikenal"
        model = self._CONTENT_MODELS[tipe]
        obj = update_record(db, model, pk_value, data)
        return obj is not None, None

    def delete_content(self, db: Session, tipe: str, pk_value: Any):
        if tipe not in self._CONTENT_MODELS:
            return False, f"Tipe konten '{tipe}' tidak dikenal"
        model = self._CONTENT_MODELS[tipe]
        return delete_record(db, model, pk_value), None

    # --- Master CRUD ---
    def create_master(self, db: Session, tipe: str, data: dict):
        if tipe not in self._MASTER_MODELS:
            return None, f"Tipe master '{tipe}' tidak dikenal"
        model = self._MASTER_MODELS[tipe]
        obj = create_record(db, model, data)
        from services.admin_service.queries.admin_queries import _get_pk
        pk = _get_pk(model)
        return {pk: getattr(obj, pk)}, None

    def update_master(self, db: Session, tipe: str, pk_value: int, data: dict):
        if tipe not in self._MASTER_MODELS:
            return None, f"Tipe master '{tipe}' tidak dikenal"
        model = self._MASTER_MODELS[tipe]
        obj = update_record(db, model, pk_value, data)
        return obj is not None, None

    def delete_master(self, db: Session, tipe: str, pk_value: int):
        if tipe not in self._MASTER_MODELS:
            return False, f"Tipe master '{tipe}' tidak dikenal"
        model = self._MASTER_MODELS[tipe]
        return delete_record(db, model, pk_value), None

    # --- Wilayah CRUD ---
    def create_wilayah(self, db: Session, tipe: str, data: dict):
        if tipe not in self._WILAYAH_MODELS:
            return None, f"Tipe wilayah '{tipe}' tidak dikenal"
        model = self._WILAYAH_MODELS[tipe]
        obj = create_record(db, model, data)
        from services.admin_service.queries.admin_queries import _get_pk
        pk = _get_pk(model)
        return {pk: getattr(obj, pk)}, None

    def update_wilayah(self, db: Session, tipe: str, pk_value: int, data: dict):
        if tipe not in self._WILAYAH_MODELS:
            return None, f"Tipe wilayah '{tipe}' tidak dikenal"
        model = self._WILAYAH_MODELS[tipe]
        obj = update_record(db, model, pk_value, data)
        return obj is not None, None

    def delete_wilayah(self, db: Session, tipe: str, pk_value: int):
        if tipe not in self._WILAYAH_MODELS:
            return False, f"Tipe wilayah '{tipe}' tidak dikenal"
        model = self._WILAYAH_MODELS[tipe]
        return delete_record(db, model, pk_value), None

    # --- Masjid Detail CRUD ---
    def create_detail(self, db: Session, tipe: str, data: dict):
        if tipe not in self._DETAIL_MODELS:
            return None, f"Tipe detail '{tipe}' tidak dikenal"
        model = self._DETAIL_MODELS[tipe]
        obj = create_record(db, model, data)
        from services.admin_service.queries.admin_queries import _get_pk
        pk = _get_pk(model)
        return {pk: getattr(obj, pk)}, None

    def update_detail(self, db: Session, tipe: str, pk_value: int, data: dict):
        if tipe not in self._DETAIL_MODELS:
            return None, f"Tipe detail '{tipe}' tidak dikenal"
        model = self._DETAIL_MODELS[tipe]
        obj = update_record(db, model, pk_value, data)
        return obj is not None, None

    def delete_detail(self, db: Session, tipe: str, pk_value: int):
        if tipe not in self._DETAIL_MODELS:
            return False, f"Tipe detail '{tipe}' tidak dikenal"
        model = self._DETAIL_MODELS[tipe]
        return delete_record(db, model, pk_value), None

    # --- Transaksi CRUD ---
    def create_transaksi(self, db: Session, tipe: str, data: dict):
        if tipe not in self._TRANSAKSI_MODELS:
            return None, f"Tipe transaksi '{tipe}' tidak dikenal"
        model = self._TRANSAKSI_MODELS[tipe]
        obj = create_record(db, model, data)
        from services.admin_service.queries.admin_queries import _get_pk
        pk = _get_pk(model)
        return {pk: getattr(obj, pk)}, None

    def update_transaksi(self, db: Session, tipe: str, pk_value: int, data: dict):
        if tipe not in self._TRANSAKSI_MODELS:
            return None, f"Tipe transaksi '{tipe}' tidak dikenal"
        model = self._TRANSAKSI_MODELS[tipe]
        obj = update_record(db, model, pk_value, data)
        return obj is not None, None

    def delete_transaksi(self, db: Session, tipe: str, pk_value: int):
        if tipe not in self._TRANSAKSI_MODELS:
            return False, f"Tipe transaksi '{tipe}' tidak dikenal"
        model = self._TRANSAKSI_MODELS[tipe]
        return delete_record(db, model, pk_value), None

    # --- Pengajuan ---
    def list_pengajuan(self, db: Session, page: int = 1, per_page: int = 10) -> dict:
        data, total = list_pengajuan(db, page, per_page)
        return {
            "data": [model_to_dict(d) for d in data],
            "total": total,
        }

    def create_pengajuan(self, db: Session, data: dict) -> dict:
        obj = create_record(db, PengajuanMasjid, data)
        return {"id_pengajuan_masjid": obj.id_pengajuan_masjid}

    def update_pengajuan(self, db: Session, pk_value: int, data: dict) -> bool:
        obj = update_record(db, PengajuanMasjid, pk_value, data)
        return obj is not None

    def delete_pengajuan(self, db: Session, pk_value: int) -> bool:
        return delete_record(db, PengajuanMasjid, pk_value)

    # --- Bulk Sync Detail ---
    def sync_masjid_detail(self, db: Session, id_masjid: str, data: Dict[str, List[Dict[str, Any]]]) -> dict:
        mapping = {
            "fasilitas": Fasilitas, "images": Images, "dokumen": Document,
            "bank": Bank, "medsos": Medsos, "logo": Logo,
            "mitra_kerjasama": MitraKerjasama, "qris": Qris,
            "struktur": Struktur, "kegiatan": Kegiatan, "videos": Videos,
        }
        results = {}
        for key, model in mapping.items():
            items = data.get(key, [])
            if not items:
                continue
            created = sync_masjid_detail_replace(db, model, id_masjid, items)
            results[key] = created
        db.commit()
        return results
