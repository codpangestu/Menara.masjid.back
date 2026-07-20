from sqlalchemy.orm import Session
from typing import Optional
from shared.models.users import Users
from shared.models.master import Levels, Labels
from shared.models.masjid import Masjid


def get_users_list(
    db: Session,
    id_provinsi: Optional[int] = None,
    id_kabupaten_kota: Optional[int] = None,
    kode_org_baznas: Optional[str] = None,
) -> list:
    q = db.query(
        Users.id_user, Users.nama, Users.email, Users.nohp,
        Users.jk, Users.kode_org_baznas, Users.id_jalur_akses,
        Users.id_level, Users.id_labels, Users.status_aktif,
        Users.created_at, Levels.nama_level, Labels.nama_labels,
        Masjid.nama_masjid, Masjid.alamat_masjid, Masjid.id_masjid,
    ).outerjoin(Levels, Users.id_level == Levels.id_level
    ).outerjoin(Labels, Users.id_labels == Labels.id_labels
    ).outerjoin(Masjid, Masjid.id_masjid == Users.id_jalur_akses)

    if id_provinsi:
        q = q.filter(Users.id_provinsi == id_provinsi)
    if id_kabupaten_kota:
        q = q.filter(Users.id_kabupaten_kota == id_kabupaten_kota)
    if kode_org_baznas:
        q = q.filter(Users.kode_org_baznas == kode_org_baznas)

    return q.order_by(Users.created_at.desc()).all()


def get_user_detail(db: Session, id_user: int):
    return db.query(
        Users.id_user, Users.nama, Users.email, Users.jk, Users.nohp,
        Users.id_jalur_akses, Users.id_level, Users.id_labels,
        Levels.nama_level, Labels.nama_labels,
        Masjid.nama_masjid, Masjid.id_masjid, Masjid.kode_org_baznas,
    ).outerjoin(Levels, Users.id_level == Levels.id_level
    ).outerjoin(Labels, Users.id_labels == Labels.id_labels
    ).outerjoin(Masjid, Masjid.id_masjid == Users.id_jalur_akses
    ).filter(Users.id_user == id_user).first()


def get_user_by_id(db: Session, id_user: int) -> Users | None:
    return db.query(Users).filter(Users.id_user == id_user).first()


def update_user_fields(db: Session, user: Users, **kwargs) -> Users:
    for key, value in kwargs.items():
        if value is not None:
            setattr(user, key, value)
    db.commit()
    return user


def delete_user(db: Session, user: Users) -> None:
    db.delete(user)
    db.commit()
