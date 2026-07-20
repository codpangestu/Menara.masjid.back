from sqlalchemy import Column, String, Integer, DateTime, Text, Date
from shared.config.database import Base
import datetime


class Fasilitas(Base):
    __tablename__ = "fasilitas"
    id_fasilitas = Column(Integer, primary_key=True, autoincrement=True)
    parent_id = Column(String(50), nullable=True)
    nama_fasilitas = Column(String(255), nullable=True)
    foto_fasilitas = Column(String(255), nullable=True)
    keterangan = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)


class Images(Base):
    __tablename__ = "images"
    id = Column(Integer, primary_key=True, autoincrement=True)
    parent_id = Column(String(50), nullable=True)
    name = Column(String(255), nullable=True)
    src = Column(String(255), nullable=True)
    description = Column(Text, nullable=True)


class Document(Base):
    __tablename__ = "document"
    id = Column(Integer, primary_key=True, autoincrement=True)
    parent_id = Column(String(50), nullable=True)
    document_name = Column(String(255), nullable=True)
    document_src = Column(String(255), nullable=True)
    document_type = Column(String(50), nullable=True)
    document_number = Column(String(50), nullable=True)
    document_category = Column(String(50), nullable=True)
    document_date = Column(Date, nullable=True)
    is_active = Column(Integer, default=1)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)


class Bank(Base):
    __tablename__ = "bank"
    id_bank = Column(Integer, primary_key=True, autoincrement=True)
    parent_id = Column(String(50), nullable=True)
    nama_bank = Column(String(255), nullable=True)
    norek = Column(String(50), nullable=True)
    atas_nama = Column(String(255), nullable=True)
    logo_bank = Column(String(255), nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)


class Medsos(Base):
    __tablename__ = "medsos"
    id_medsos = Column(Integer, primary_key=True, autoincrement=True)
    parent_id = Column(String(50), nullable=True)
    icon_medsos = Column(String(255), nullable=True)
    name_medsos = Column(String(255), nullable=True)
    url_medsos = Column(String(255), nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)


class Logo(Base):
    __tablename__ = "logo"
    id_logo = Column(Integer, primary_key=True, autoincrement=True)
    parent_id = Column(String(50), nullable=True)
    nama_logo = Column(String(255), nullable=True)
    gambar_logo = Column(String(255), nullable=True)
    jenis_logo = Column(String(50), nullable=True)
    keterangan = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)


class MitraKerjasama(Base):
    __tablename__ = "mitra_kerjasama"
    id_mitra_kerjasama = Column(Integer, primary_key=True, autoincrement=True)
    parent_id = Column(String(50), nullable=True)
    nama_mitra_kerjasama = Column(String(255), nullable=True)
    gambar_mitra_kerjasama = Column(String(255), nullable=True)
    keterangan = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)


class Qris(Base):
    __tablename__ = "qris"
    id_qris = Column(Integer, primary_key=True, autoincrement=True)
    parent_id = Column(String(50), nullable=True)
    nama_qris = Column(String(255), nullable=True)
    gambar_qris = Column(String(255), nullable=True)
    keterangan = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)


class Struktur(Base):
    __tablename__ = "struktur"
    id_struktur = Column(Integer, primary_key=True, autoincrement=True)
    parent_id = Column(String(50), nullable=True)
    nama_struktur = Column(String(255), nullable=True)
    foto_struktur = Column(String(255), nullable=True)
    jenis_struktur = Column(String(50), nullable=True)
    keterangan = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)


class Kegiatan(Base):
    __tablename__ = "kegiatan"
    id_kegiatan = Column(Integer, primary_key=True, autoincrement=True)
    parent_id = Column(String(50), nullable=True)
    nama_kegiatan = Column(String(255), nullable=True)
    foto_kegiatan = Column(String(255), nullable=True)
    jenis_kegiatan = Column(String(50), nullable=True)
    keterangan = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)


class Videos(Base):
    __tablename__ = "videos"
    id_video = Column(Integer, primary_key=True, autoincrement=True)
    parent_id = Column(String(50), nullable=True)
    tgl_video = Column(Date, nullable=True)
    judul_video = Column(String(255), nullable=True)
    iframe_video = Column(Text, nullable=True)
    deskripsi_video = Column(Text, nullable=True)
    id_tema = Column(Integer, nullable=True)
    slug_video = Column(String(255), nullable=True, unique=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
