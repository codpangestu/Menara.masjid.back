from sqlalchemy.orm import Session
from typing import Optional
from shared.models.wilayah import Provinsi, KabupatenKota, Kecamatan, KelurahanDesa


def get_provinsi(db: Session, id: Optional[int] = None) -> list:
    q = db.query(Provinsi)
    if id:
        q = q.filter(Provinsi.id == id)
    return q.order_by(Provinsi.id.desc()).all()


def get_kabupaten_kota(db: Session, id_provinsi: Optional[int] = None) -> list:
    q = db.query(KabupatenKota)
    if id_provinsi:
        q = q.filter(KabupatenKota.id_provinsi == id_provinsi)
    return q.order_by(KabupatenKota.id.desc()).all()


def get_kecamatan(db: Session, id_kabupaten_kota: Optional[int] = None) -> list:
    q = db.query(Kecamatan)
    if id_kabupaten_kota:
        q = q.filter(Kecamatan.id_kabupaten_kota == id_kabupaten_kota)
    return q.order_by(Kecamatan.id.desc()).all()


def get_kelurahan_desa(db: Session, id_kecamatan: Optional[int] = None) -> list:
    q = db.query(KelurahanDesa)
    if id_kecamatan:
        q = q.filter(KelurahanDesa.id_kecamatan == id_kecamatan)
    return q.order_by(KelurahanDesa.id.desc()).all()
