from sqlalchemy.orm import Session
from typing import Optional
from services.masjid_service.queries.wilayah_queries import get_provinsi, get_kabupaten_kota, get_kecamatan, get_kelurahan_desa
from shared.schemas.base import model_to_dict


class WilayahService:
    def get_provinsi(self, db: Session, id: Optional[int] = None) -> list:
        data = get_provinsi(db, id)
        return [model_to_dict(d) for d in data]

    def get_kabupaten_kota(self, db: Session, id_provinsi: Optional[int] = None) -> list:
        data = get_kabupaten_kota(db, id_provinsi)
        return [model_to_dict(d) for d in data]

    def get_kecamatan(self, db: Session, id_kabupaten_kota: Optional[int] = None) -> list:
        data = get_kecamatan(db, id_kabupaten_kota)
        return [model_to_dict(d) for d in data]

    def get_kelurahan_desa(self, db: Session, id_kecamatan: Optional[int] = None) -> list:
        data = get_kelurahan_desa(db, id_kecamatan)
        return [model_to_dict(d) for d in data]
