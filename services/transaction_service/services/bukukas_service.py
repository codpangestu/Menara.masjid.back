from sqlalchemy.orm import Session
from typing import Optional
from services.transaction_service.queries.bukukas_queries import (
    list_penerimaan, list_penerimaan_cc, list_pengeluaran, list_pengeluaran_cc,
)


class BukuKasService:
    def get_penerimaan(self, db: Session, **kwargs) -> dict:
        data, total = list_penerimaan(db, **kwargs)
        items = [
            {
                "kode_org_baznas": r[0].kode_org_baznas,
                "nominal_masuk": float(r[0].nominal_masuk or 0),
                "jumlah_donatur": r[0].jumlah_donatur,
                "keterangan": r[0].keterangan,
                "tanggal": str(r[0].tanggal) if r[0].tanggal else None,
                "nama_jenis_dana": r[1],
                "nama_jenis_harta": r[2],
                "nama_label_info_dana": r[3],
                "nama_masjid": r[4],
                "alamat_masjid": r[5],
            }
            for r in data
        ]
        return {
            "data": items,
            "total": total,
            "page": kwargs.get("page", 1),
            "per_page": kwargs.get("per_page", 10),
        }

    def get_penerimaan_cc(self, db: Session, **kwargs) -> list:
        data = list_penerimaan_cc(db, **kwargs)
        return [
            {
                "id_bukukas_penerimaan": r.id_bukukas_penerimaan,
                "id_jalur_akses": r.id_jalur_akses,
                "nominal_masuk": float(r.nominal_masuk or 0),
                "jumlah_donatur": r.jumlah_donatur,
                "keterangan": r.keterangan,
                "id_jenis_dana": r.id_jenis_dana,
                "id_jenis_harta": r.id_jenis_harta,
                "tanggal": str(r.tanggal) if r.tanggal else None,
                "created_at": str(r.created_at) if r.created_at else None,
            }
            for r in data
        ]

    def get_pengeluaran(self, db: Session, **kwargs) -> dict:
        data, total = list_pengeluaran(db, **kwargs)
        items = [
            {
                "kode_org_baznas": r[0].kode_org_baznas,
                "nominal_keluar": float(r[0].nominal_keluar or 0),
                "jumlah_penerima_manfaat": r[0].jumlah_penerima_manfaat,
                "keterangan": r[0].keterangan,
                "tanggal": str(r[0].tanggal) if r[0].tanggal else None,
                "nama_jenis_dana": r[1],
                "nama_jenis_harta": r[2],
                "nama_label_info_dana": r[3],
                "nama_masjid": r[4],
                "alamat_masjid": r[5],
            }
            for r in data
        ]
        return {
            "data": items,
            "total": total,
            "page": kwargs.get("page", 1),
            "per_page": kwargs.get("per_page", 10),
        }

    def get_pengeluaran_cc(self, db: Session, **kwargs) -> list:
        data = list_pengeluaran_cc(db, **kwargs)
        return [
            {
                "id_bukukas_pengeluaran": r.id_bukukas_pengeluaran,
                "id_jalur_akses": r.id_jalur_akses,
                "nominal_keluar": float(r.nominal_keluar or 0),
                "jumlah_penerima_manfaat": r.jumlah_penerima_manfaat,
                "keterangan": r.keterangan,
                "id_jenis_dana": r.id_jenis_dana,
                "id_jenis_harta": r.id_jenis_harta,
                "tanggal": str(r.tanggal) if r.tanggal else None,
                "created_at": str(r.created_at) if r.created_at else None,
            }
            for r in data
        ]
