from sqlalchemy.orm import Session, joinedload
from sqlalchemy import func
from typing import Optional
from shared.models.masjid import Masjid
from shared.models.users import Users
from shared.models.transaksi import BukukasPenerimaan, BukukasPengeluaran
from shared.models.master import Levels, Labels


def get_masjid_by_id(db: Session, id_masjid: str) -> Masjid | None:
    return db.query(Masjid).filter(Masjid.id_masjid == id_masjid).first()


def get_masjid_by_slug(db: Session, slug: str) -> Masjid | None:
    return db.query(Masjid).filter(Masjid.slug_masjid == slug).first()


def get_list_masjid(
    db: Session,
    page: int = 1,
    per_page: int = 10,
    kode_org_baznas: Optional[str] = None,
    id_provinsi: Optional[int] = None,
    id_kabupaten_kota: Optional[int] = None,
    keyword_nama: Optional[str] = None,
    keyword_alamat: Optional[str] = None,
    keyword_label: Optional[str] = None,
) -> tuple:
    q = db.query(Masjid)
    if kode_org_baznas:
        q = q.filter(Masjid.kode_org_baznas == kode_org_baznas)
    if id_provinsi:
        q = q.filter(Masjid.id_provinsi == id_provinsi)
    if id_kabupaten_kota:
        q = q.filter(Masjid.id_kabupaten_kota == id_kabupaten_kota)
    if keyword_nama:
        q = q.filter(Masjid.nama_masjid.like(f"%{keyword_nama}%"))
    if keyword_alamat:
        q = q.filter(Masjid.alamat_masjid.like(f"%{keyword_alamat}%"))
    if keyword_label:
        q = q.filter(Masjid.label_upz.like(f"%{keyword_label}%"))

    total = q.count()
    data = q.order_by(Masjid.created_at.desc()).offset((page - 1) * per_page).limit(per_page).all()
    return data, total


def get_masjid_by_wilayah(
    db: Session,
    id_provinsi: int,
    id_kabupaten_kota: Optional[int] = None,
    keyword_nama_masjid: Optional[str] = None,
    keyword_alamat_masjid: Optional[str] = None,
    keyword_label_masjid: Optional[str] = None,
    page: int = 1,
    per_page: int = 10,
) -> list:
    q = db.query(
        Masjid.id_masjid, Masjid.nama_masjid, Masjid.kode_org_baznas,
        Masjid.jenis_masjid, Masjid.tipologi, Masjid.alamat_masjid,
        Masjid.daya_tampung, Masjid.label_upz, Masjid.noregis_simas,
        Masjid.slug_masjid, Masjid.id_provinsi, Masjid.id_kabupaten_kota,
        func.coalesce(func.sum(BukukasPenerimaan.nominal_masuk), 0).label("total_penerimaan"),
        func.coalesce(func.sum(BukukasPengeluaran.nominal_keluar), 0).label("total_pengeluaran"),
    ).outerjoin(
        BukukasPenerimaan, Masjid.id_masjid == BukukasPenerimaan.id_jalur_akses
    ).outerjoin(
        BukukasPengeluaran, Masjid.id_masjid == BukukasPengeluaran.id_jalur_akses
    ).filter(Masjid.id_provinsi == id_provinsi)

    if id_kabupaten_kota:
        q = q.filter(Masjid.id_kabupaten_kota == id_kabupaten_kota)
    if keyword_nama_masjid:
        q = q.filter(Masjid.nama_masjid.like(f"%{keyword_nama_masjid}%"))
    if keyword_alamat_masjid:
        q = q.filter(Masjid.alamat_masjid.like(f"%{keyword_alamat_masjid}%"))
    if keyword_label_masjid:
        q = q.filter(Masjid.label_upz.like(f"%{keyword_label_masjid}%"))

    q = q.group_by(Masjid.id_masjid).order_by(Masjid.created_at.desc())
    q = q.offset((page - 1) * per_page).limit(per_page)
    return q.all()


def get_pengurus_by_masjid(db: Session, id_masjid: str) -> list:
    return db.query(Users, Levels, Labels, Masjid).join(
        Levels, Users.id_level == Levels.id_level, isouter=True
    ).join(
        Labels, Users.id_labels == Labels.id_labels, isouter=True
    ).join(
        Masjid, Masjid.id_masjid == Users.id_jalur_akses, isouter=True
    ).filter(Users.id_jalur_akses == id_masjid).all()


def search_masjid_public(
    db: Session,
    nama: Optional[str] = None,
    jenis: Optional[str] = None,
    tipologi: Optional[str] = None,
    id_provinsi: Optional[int] = None,
    id_kabupaten_kota: Optional[int] = None,
    id_kecamatan: Optional[int] = None,
) -> list:
    q = db.query(Masjid).filter(Masjid.status_aktif == 1)
    if nama:
        q = q.filter(Masjid.nama_masjid.like(f"%{nama}%"))
    if jenis:
        q = q.filter(Masjid.jenis_masjid == jenis)
    if tipologi:
        q = q.filter(Masjid.tipologi == tipologi)
    if id_provinsi:
        q = q.filter(Masjid.id_provinsi == id_provinsi)
    if id_kabupaten_kota:
        q = q.filter(Masjid.id_kabupaten_kota == id_kabupaten_kota)
    if id_kecamatan:
        q = q.filter(Masjid.id_kecamatan == id_kecamatan)
    return q.order_by(Masjid.created_at.desc()).all()
