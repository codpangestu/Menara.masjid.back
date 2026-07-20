from sqlalchemy.orm import Session
from typing import Optional
from services.admin_service.queries.master_queries import (
    get_levels, get_labels, get_jenis_dana, get_jenis_harta, get_label_info_dana,
    get_tema, get_kategori_acara, get_kategori_cerita, get_kategori_donasi,
    get_kategori_postingan,
)
from shared.schemas.base import model_to_dict


class MasterService:
    def get_levels(self, db: Session, id_level: Optional[int] = None) -> list:
        return [model_to_dict(d) for d in get_levels(db, id_level)]

    def get_labels(self, db: Session, id_labels: Optional[int] = None) -> list:
        return [model_to_dict(d) for d in get_labels(db, id_labels)]

    def get_jenis_dana(self, db: Session, id_jenis_dana: Optional[int] = None) -> list:
        return [model_to_dict(d) for d in get_jenis_dana(db, id_jenis_dana)]

    def get_jenis_harta(self, db: Session, id_jenis_harta: Optional[int] = None) -> list:
        return [model_to_dict(d) for d in get_jenis_harta(db, id_jenis_harta)]

    def get_label_info_dana(self, db: Session, id_label_info_dana: Optional[int] = None) -> list:
        return [model_to_dict(d) for d in get_label_info_dana(db, id_label_info_dana)]

    def get_tema(self, db: Session, parent_id: Optional[str] = None) -> list:
        return [model_to_dict(d) for d in get_tema(db, parent_id)]

    def get_kategori_acara(self, db: Session, parent_id: Optional[str] = None) -> list:
        return [model_to_dict(d) for d in get_kategori_acara(db, parent_id)]

    def get_kategori_cerita(self, db: Session, parent_id: Optional[str] = None) -> list:
        return [model_to_dict(d) for d in get_kategori_cerita(db, parent_id)]

    def get_kategori_donasi(self, db: Session, parent_id: Optional[str] = None) -> list:
        return [model_to_dict(d) for d in get_kategori_donasi(db, parent_id)]

    def get_kategori_postingan(self, db: Session, parent_id: Optional[str] = None) -> list:
        return [model_to_dict(d) for d in get_kategori_postingan(db, parent_id)]
