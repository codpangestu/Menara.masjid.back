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
        items = []
        for d in data:
            item = model_to_dict(d)
            # Alias `id` (PK id_pengajuan) agar konsisten dengan tipe frontend
            item["id"] = item.get("id_pengajuan")
            items.append(item)
        return {
            "data": items,
            "total": total,
        }

    def create_pengajuan(self, db: Session, data: dict) -> dict:
        """
        Buat pengajuan masjid (langkah 1). Kode masjid & slug diterbitkan LANGSUNG
        (bukan menunggu approval) agar pemohon bisa langsung melanjutkan ke langkah 2
        (daftar admin masjid dengan kode tsb). Record masjid & user admin baru dibuat
        saat Admin BAZNAS menyetujui pengajuan.
        """
        import secrets
        from shared.models.masjid import Masjid

        # Generate kode unik (format: MSJ-XXXXXX)
        kode = None
        for _ in range(10):
            candidate = "MSJ-" + secrets.token_hex(3).upper()
            exists = db.query(Masjid).filter(Masjid.kode_org_baznas == candidate).first()
            if not exists:
                kode = candidate
                break
        if not kode:
            return {"error": "Gagal membuat kode masjid. Silakan coba lagi."}

        data["kode_org_baznas"] = kode
        data["slug_masjid"] = self._make_slug(data.get("nama_masjid"), kode)
        obj = create_record(db, PengajuanMasjid, data)
        return {"id": obj.id_pengajuan, "kode_org_baznas": kode, "slug_masjid": obj.slug_masjid}

    def update_pengajuan(self, db: Session, pk_value: int, data: dict) -> dict | None:
        """
        Update pengajuan (langkah 2): simpan data admin pemohon.
        Jika status='disetujui', otomatis AKTIVASI — membuat record masjid
        (memakai kode yang sudah diterbitkan saat create) + user Admin Masjid
        dari data pemohon, SEKALIGUS dalam sekali konfirmasi.
        Mengembalikan dict pengajuan terbaru, dict {"error": ...} jika ada
        masalah validasi, atau None jika tidak ditemukan.
        """
        status = str(data.get("status_pengajuan", "")).lower()

        # Guard: aktivasi memerlukan data admin pemohon lengkap (nama + email),
        # agar tidak ada masjid teraktivasi tanpa akun Admin Masjid.
        if status == "disetujui":
            existing = db.query(PengajuanMasjid).filter(
                PengajuanMasjid.id_pengajuan == pk_value
            ).first()
            if existing is None:
                return None
            if not (existing.nama_pemohon and existing.email_pemohon):
                return {"error": "Data admin pemohon belum lengkap. Pemohon harus menyelesaikan pendaftaran admin masjid terlebih dahulu."}

        obj = update_record(db, PengajuanMasjid, pk_value, data)
        if obj is None:
            return None

        if status == "disetujui":
            self._activate_pengajuan(db, obj)
        return model_to_dict(obj)

    def _activate_pengajuan(self, db: Session, pengajuan: PengajuanMasjid) -> None:
        """Aktivasi: buat masjid + user Admin Masjid dari data pengajuan (sekali konfirmasi)."""
        from shared.models.masjid import Masjid
        from services.auth_service.queries.auth_queries import create_user, get_user_by_email
        from shared.utils.jwt_helper import get_password_hash
        from shared.config.constants import (
            DEFAULT_PASSWORD, DEFAULT_AVATAR, JALUR_MASJID, DEFAULT_USER_LEVEL,
        )

        kode = pengajuan.kode_org_baznas
        if not kode:
            return

        # 1) Buat record masjid (id_masjid = kode masjid)
        existing = db.query(Masjid).filter(Masjid.kode_org_baznas == kode).first()
        if not existing:
            masjid = Masjid(
                id_masjid=kode,
                kode_org_baznas=kode,
                nama_masjid=pengajuan.nama_masjid,
                alamat_masjid=pengajuan.alamat_masjid,
                email_masjid=pengajuan.email_pemohon or pengajuan.email_masjid,
                nohp_masjid=pengajuan.nohp_masjid,
                id_provinsi=pengajuan.id_provinsi,
                id_kabupaten_kota=pengajuan.id_kabupaten_kota,
                id_kecamatan=pengajuan.id_kecamatan,
                id_kelurahan_desa=pengajuan.id_kelurahan_desa,
                slug_masjid=pengajuan.slug_masjid or self._make_slug(pengajuan.nama_masjid, kode),
                status_aktif=1,
            )
            db.add(masjid)
            db.commit()
            db.refresh(masjid)

        # 2) Buat user Admin Masjid dari data pemohon (jika belum ada / email unik)
        email = (pengajuan.email_pemohon or "").strip()
        if email and not get_user_by_email(db, email):
            user = create_user(
                db,
                jalur_akses=JALUR_MASJID,
                id_jalur_akses=kode,
                nama=pengajuan.nama_pemohon,
                jk=pengajuan.jk_pemohon,
                nohp=pengajuan.nohp_pemohon,
                email=email,
                alamat=pengajuan.alamat_pemohon,
                kode_org_baznas=kode,
                password=get_password_hash(DEFAULT_PASSWORD),
                id_level=2,  # Admin Masjid
                id_labels=1,  # Admin
                avatar=DEFAULT_AVATAR,
                status_aktif=1,
                catatan="Dibuat via persetujuan pengajuan masjid",
            )
            pengajuan.id_user = user.id_user
            db.commit()
            db.refresh(pengajuan)

    @staticmethod
    def _make_slug(nama: str | None, suffix: str) -> str:
        """Buat slug unik dari nama masjid."""
        import re
        if not nama:
            return suffix.lower()
        base = re.sub(r"[^a-z0-9]+", "-", nama.lower()).strip("-")
        return f"{base}-{suffix.lower()}" if base else suffix.lower()

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
