from sqlalchemy import Column, String, Integer, DateTime, Text, Date
from sqlalchemy.orm import relationship
from shared.config.database import Base
import datetime


class Users(Base):
    __tablename__ = "users"

    id_user = Column(Integer, primary_key=True, autoincrement=True)
    kode_org_baznas = Column(String(50), nullable=True)
    jalur_akses = Column(String(50), nullable=True)
    nama = Column(String(255), nullable=True)
    jk = Column(String(10), nullable=True)
    nohp = Column(String(50), nullable=True)
    email = Column(String(255), nullable=True, unique=True)
    password = Column(String(255), nullable=True)
    alamat = Column(Text, nullable=True)
    avatar = Column(String(255), nullable=True, default="user-default.png")
    id_level = Column(Integer, nullable=True)
    id_labels = Column(Integer, nullable=True)
    status_aktif = Column(Integer, default=1)
    id_jalur_akses = Column(String(50), nullable=True)
    id_provinsi = Column(Integer, nullable=True)
    id_kabupaten_kota = Column(Integer, nullable=True)
    id_kecamatan = Column(Integer, nullable=True)
    id_kelurahan_desa = Column(Integer, nullable=True)
    catatan = Column(Text, nullable=True)
    show_saldo = Column(Integer, default=1)
    last_login = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
