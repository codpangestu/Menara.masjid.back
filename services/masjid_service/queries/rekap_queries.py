from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import Optional
from shared.models.transaksi import BukukasPenerimaan, BukukasPengeluaran


def get_rekap_penerimaan(
    db: Session,
    kode_org_baznas: Optional[str] = None,
    id_provinsi: Optional[int] = None,
    id_kabupaten_kota: Optional[int] = None,
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
):
    q = db.query(
        func.count(func.distinct(BukukasPenerimaan.id_jalur_akses)).label("jumlah_masjid"),
        func.coalesce(func.sum(BukukasPenerimaan.nominal_masuk), 0).label("total_penerimaan"),
        func.coalesce(func.sum(BukukasPenerimaan.jumlah_donatur), 0).label("total_donatur"),
    )

    if id_provinsi and id_kabupaten_kota:
        q = q.filter(
            BukukasPenerimaan.id_provinsi == id_provinsi,
            BukukasPenerimaan.id_kabupaten_kota == id_kabupaten_kota,
        )
    elif id_provinsi:
        q = q.filter(BukukasPenerimaan.id_provinsi == id_provinsi)
    elif kode_org_baznas:
        q = q.filter(BukukasPenerimaan.kode_org_baznas == kode_org_baznas)

    if start_date:
        q = q.filter(BukukasPenerimaan.tanggal >= start_date)
    if end_date:
        q = q.filter(BukukasPenerimaan.tanggal <= end_date)

    return q.first()


def get_rekap_pengeluaran(
    db: Session,
    kode_org_baznas: Optional[str] = None,
    id_provinsi: Optional[int] = None,
    id_kabupaten_kota: Optional[int] = None,
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
):
    q = db.query(
        func.count(func.distinct(BukukasPengeluaran.id_jalur_akses)).label("jumlah_masjid"),
        func.coalesce(func.sum(BukukasPengeluaran.nominal_keluar), 0).label("total_pengeluaran"),
        func.coalesce(func.sum(BukukasPengeluaran.jumlah_penerima_manfaat), 0).label("total_penerima_manfaat"),
    )

    if id_provinsi and id_kabupaten_kota:
        q = q.filter(
            BukukasPengeluaran.id_provinsi == id_provinsi,
            BukukasPengeluaran.id_kabupaten_kota == id_kabupaten_kota,
        )
    elif id_provinsi:
        q = q.filter(BukukasPengeluaran.id_provinsi == id_provinsi)
    elif kode_org_baznas:
        q = q.filter(BukukasPengeluaran.kode_org_baznas == kode_org_baznas)

    if start_date:
        q = q.filter(BukukasPengeluaran.tanggal >= start_date)
    if end_date:
        q = q.filter(BukukasPengeluaran.tanggal <= end_date)

    return q.first()


def get_rekap_by_masjid(
    db: Session,
    id_masjid: str,
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
) -> dict:
    p_query = db.query(
        func.coalesce(func.sum(BukukasPenerimaan.nominal_masuk), 0).label("total_penerimaan"),
        func.coalesce(func.sum(BukukasPenerimaan.jumlah_donatur), 0).label("total_donatur"),
    ).filter(BukukasPenerimaan.id_jalur_akses == id_masjid)

    pe_query = db.query(
        func.coalesce(func.sum(BukukasPengeluaran.nominal_keluar), 0).label("total_pengeluaran"),
        func.coalesce(func.sum(BukukasPengeluaran.jumlah_penerima_manfaat), 0).label("total_penerima_manfaat"),
    ).filter(BukukasPengeluaran.id_jalur_akses == id_masjid)

    if start_date:
        p_query = p_query.filter(BukukasPenerimaan.tanggal >= start_date)
        pe_query = pe_query.filter(BukukasPengeluaran.tanggal >= start_date)
    if end_date:
        p_query = p_query.filter(BukukasPenerimaan.tanggal <= end_date)
        pe_query = pe_query.filter(BukukasPengeluaran.tanggal <= end_date)

    p = p_query.first()
    pe = pe_query.first()

    result = {"id_masjid": id_masjid}
    if p:
        result.update(dict(p._mapping))
    if pe:
        result.update(dict(pe._mapping))
    return result
