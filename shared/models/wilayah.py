from sqlalchemy import Column, String, Integer
from shared.config.database import Base


class Provinsi(Base):
    __tablename__ = "provinsi"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nama_provinsi = Column(String(255), nullable=True)


class KabupatenKota(Base):
    __tablename__ = "kabupaten_kota"
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_provinsi = Column(Integer, nullable=True)
    nama_kabupaten_kota = Column(String(255), nullable=True)


class Kecamatan(Base):
    __tablename__ = "kecamatan"
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_kabupaten_kota = Column(Integer, nullable=True)
    nama_kecamatan = Column(String(255), nullable=True)


class KelurahanDesa(Base):
    __tablename__ = "kelurahan_desa"
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_kecamatan = Column(Integer, nullable=True)
    nama_kelurahan_desa = Column(String(255), nullable=True)
