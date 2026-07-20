from sqlalchemy import Column, String, Integer, DateTime, Text
from shared.config.database import Base
import datetime


class Levels(Base):
    __tablename__ = "levels"
    id_level = Column(Integer, primary_key=True, autoincrement=True)
    nama_level = Column(String(100), nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)


class Labels(Base):
    __tablename__ = "labels"
    id_labels = Column(Integer, primary_key=True, autoincrement=True)
    nama_labels = Column(String(100), nullable=True)
    parent_id = Column(Integer, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)


class JenisDana(Base):
    __tablename__ = "jenis_dana"
    id_jenis_dana = Column(Integer, primary_key=True, autoincrement=True)
    nama_jenis_dana = Column(String(255), nullable=True)
    parent_id = Column(Integer, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)


class JenisHarta(Base):
    __tablename__ = "jenis_harta"
    id_jenis_harta = Column(Integer, primary_key=True, autoincrement=True)
    nama_jenis_harta = Column(String(255), nullable=True)
    parent_id = Column(Integer, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)


class JenisLaporan(Base):
    __tablename__ = "jenis_laporan"
    id_jenis_laporan = Column(Integer, primary_key=True, autoincrement=True)
    nama_jenis_laporan = Column(String(255), nullable=True)
    parent_id = Column(Integer, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)


class JenisPerolehanAset(Base):
    __tablename__ = "jenis_perolehan_aset"
    id_jenis_perolehan_aset = Column(Integer, primary_key=True, autoincrement=True)
    nama_jenis_perolehan_aset = Column(String(255), nullable=True)
    parent_id = Column(Integer, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)


class LabelInfoDana(Base):
    __tablename__ = "label_info_dana"
    id_label_info_dana = Column(Integer, primary_key=True, autoincrement=True)
    nama_label_info_dana = Column(String(255), nullable=True)
    parent_id = Column(Integer, nullable=True)


class Tema(Base):
    __tablename__ = "tema"
    id_tema = Column(Integer, primary_key=True, autoincrement=True)
    nama_tema = Column(String(255), nullable=True)
    parent_id = Column(String(50), nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)


class KategoriAcara(Base):
    __tablename__ = "kategori_acara"
    id_kategori_acara = Column(Integer, primary_key=True, autoincrement=True)
    nama_kategori_acara = Column(String(255), nullable=True)
    parent_id = Column(String(50), nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)


class KategoriCerita(Base):
    __tablename__ = "kategori_cerita"
    id_kategori_cerita = Column(Integer, primary_key=True, autoincrement=True)
    nama_kategori_cerita = Column(String(255), nullable=True)
    parent_id = Column(String(50), nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)


class KategoriDonasi(Base):
    __tablename__ = "kategori_donasi"
    id_kategori_donasi = Column(Integer, primary_key=True, autoincrement=True)
    nama_kategori_donasi = Column(String(255), nullable=True)
    parent_id = Column(String(50), nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)


class KategoriPostingan(Base):
    __tablename__ = "kategori_postingan"
    id_kategori_postingan = Column(Integer, primary_key=True, autoincrement=True)
    nama_kategori_postingan = Column(String(255), nullable=True)
    parent_id = Column(String(50), nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)


class KategoriPanduanPengguna(Base):
    __tablename__ = "kategori_panduan_pengguna"
    id_kategori_panduan_pengguna = Column(Integer, primary_key=True, autoincrement=True)
    nama_kategori_panduan_pengguna = Column(String(255), nullable=True)
    parent_id = Column(String(50), nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)


class KategoriPanduanPengelola(Base):
    __tablename__ = "kategori_panduan_pengelola"
    id_kategori_panduan_pengelola = Column(Integer, primary_key=True, autoincrement=True)
    nama_kategori_panduan_pengelola = Column(String(255), nullable=True)
    parent_id = Column(String(50), nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)


class KategoriMenaraVideo(Base):
    __tablename__ = "kategori_menara_video"
    id_kategori_menara_video = Column(Integer, primary_key=True, autoincrement=True)
    nama_kategori_menara_video = Column(String(255), nullable=True)
    parent_id = Column(String(50), nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
