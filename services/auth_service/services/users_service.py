from sqlalchemy.orm import Session
from typing import Optional
from services.auth_service.queries.users_queries import (
    get_users_list, get_user_detail, get_user_by_id, update_user_fields, delete_user,
)
from services.auth_service.queries.auth_queries import get_user_by_email, create_user
from shared.utils.jwt_helper import get_password_hash
from shared.config.constants import DEFAULT_PASSWORD, DEFAULT_AVATAR, DEFAULT_USER_LEVEL, JALUR_MASJID


class UsersService:
    def get_list(self, db: Session, id_provinsi: Optional[int] = None,
                 id_kabupaten_kota: Optional[int] = None,
                 kode_org_baznas: Optional[str] = None) -> list:
        results = get_users_list(db, id_provinsi, id_kabupaten_kota, kode_org_baznas)
        return [dict(r._mapping) for r in results]

    def get_detail(self, db: Session, id_user: int):
        result = get_user_detail(db, id_user)
        if not result:
            return None
        return dict(result._mapping)

    def register(self, db: Session, **kwargs):
        user = create_user(
            db,
            jalur_akses=JALUR_MASJID,
            id_jalur_akses=kwargs.get("id_jalur_akses", ""),
            nama=kwargs.get("nama"),
            jk=kwargs.get("jk", ""),
            alamat=kwargs.get("alamat", ""),
            email=kwargs.get("email"),
            nohp=kwargs.get("nohp", ""),
            kode_org_baznas=kwargs.get("kode_org_baznas", ""),
            password=get_password_hash(DEFAULT_PASSWORD),
            id_level=DEFAULT_USER_LEVEL,
            id_labels=kwargs.get("id_labels", 0),
            avatar=DEFAULT_AVATAR,
            status_aktif=1,
            catatan=kwargs.get("catatan", ""),
        )
        return {"id_user": user.id_user}

    def update(self, db: Session, id_user: int, **kwargs) -> bool:
        user = get_user_by_id(db, id_user)
        if not user:
            return False
        update_user_fields(db, user, **kwargs)
        return True

    def delete(self, db: Session, id_user: int) -> bool:
        user = get_user_by_id(db, id_user)
        if not user:
            return False
        delete_user(db, user)
        return True
