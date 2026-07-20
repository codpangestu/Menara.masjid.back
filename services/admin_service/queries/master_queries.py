from sqlalchemy.orm import Session
from typing import Optional
from shared.models.master import (
    Levels, Labels, JenisDana, JenisHarta, LabelInfoDana,
    KategoriAcara, KategoriCerita, KategoriDonasi, KategoriPostingan,
    Tema,
)
from shared.schemas.base import model_to_dict


def get_levels(db: Session, id_level: Optional[int] = None) -> list:
    q = db.query(Levels)
    if id_level:
        q = q.filter(Levels.id_level == id_level)
    return q.order_by(Levels.created_at.desc()).all()


def get_labels(db: Session, id_labels: Optional[int] = None) -> list:
    q = db.query(Labels)
    if id_labels:
        q = q.filter(Labels.id_labels == id_labels)
    return q.order_by(Labels.created_at.desc()).all()


def get_jenis_dana(db: Session, id_jenis_dana: Optional[int] = None) -> list:
    q = db.query(JenisDana)
    if id_jenis_dana:
        q = q.filter(JenisDana.id_jenis_dana == id_jenis_dana)
    return q.order_by(JenisDana.created_at.desc()).all()


def get_jenis_harta(db: Session, id_jenis_harta: Optional[int] = None) -> list:
    q = db.query(JenisHarta)
    if id_jenis_harta:
        q = q.filter(JenisHarta.id_jenis_harta == id_jenis_harta)
    return q.order_by(JenisHarta.created_at.desc()).all()


def get_label_info_dana(db: Session, id_label_info_dana: Optional[int] = None) -> list:
    q = db.query(LabelInfoDana)
    if id_label_info_dana:
        q = q.filter(LabelInfoDana.id_label_info_dana == id_label_info_dana)
    return q.order_by(LabelInfoDana.id_label_info_dana.desc()).all()


def get_tema(db: Session, parent_id: Optional[str] = None) -> list:
    q = db.query(Tema)
    if parent_id:
        q = q.filter(Tema.parent_id == parent_id)
    return q.all()


def get_kategori_acara(db: Session, parent_id: Optional[str] = None) -> list:
    q = db.query(KategoriAcara)
    if parent_id:
        q = q.filter(KategoriAcara.parent_id == parent_id)
    return q.all()


def get_kategori_cerita(db: Session, parent_id: Optional[str] = None) -> list:
    q = db.query(KategoriCerita)
    if parent_id:
        q = q.filter(KategoriCerita.parent_id == parent_id)
    return q.all()


def get_kategori_donasi(db: Session, parent_id: Optional[str] = None) -> list:
    q = db.query(KategoriDonasi)
    if parent_id:
        q = q.filter(KategoriDonasi.parent_id == parent_id)
    return q.all()


def get_kategori_postingan(db: Session, parent_id: Optional[str] = None) -> list:
    q = db.query(KategoriPostingan)
    if parent_id:
        q = q.filter(KategoriPostingan.parent_id == parent_id)
    return q.all()
