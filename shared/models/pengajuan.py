from sqlalchemy import Column, String, Integer, DateTime, Text
from shared.config.database import Base
import datetime


class PengajuanMasjid(Base):
    __tablename__ = "pengajuan_masjid"
    id_pengajuan = Column(Integer, primary_key=True, autoincrement=True)
    nama_masjid = Column(String(255), nullable=True)
    alamat_masjid = Column(Text, nullable=True)
    email_masjid = Column(String(255), nullable=True)
    nohp_masjid = Column(String(50), nullable=True)
    id_provinsi = Column(Integer, nullable=True)
    id_kabupaten_kota = Column(Integer, nullable=True)
    id_kecamatan = Column(Integer, nullable=True)
    id_kelurahan_desa = Column(Integer, nullable=True)
    status_pengajuan = Column(String(50), nullable=True, default="Menunggu")
    id_user = Column(Integer, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)


class PengajuanUserMasjid(Base):
    __tablename__ = "pengajuan_user_masjid"
    id_pengajuan = Column(Integer, primary_key=True, autoincrement=True)
    id_masjid = Column(String(50), nullable=True)
    nama = Column(String(255), nullable=True)
    email = Column(String(255), nullable=True)
    nohp = Column(String(50), nullable=True)
    status_pengajuan = Column(String(50), nullable=True, default="Menunggu")
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
