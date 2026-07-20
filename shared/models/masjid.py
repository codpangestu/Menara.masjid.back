from sqlalchemy import Column, String, Integer, DateTime, Text, Float
from shared.config.database import Base
import datetime


class Masjid(Base):
    __tablename__ = "masjid"

    id_masjid = Column(String(50), primary_key=True)
    kode_org_baznas = Column(String(50), nullable=True)
    nama_masjid = Column(String(255), nullable=True)
    jenis_masjid = Column(String(50), nullable=True)
    tipologi = Column(String(50), nullable=True)
    alamat_masjid = Column(Text, nullable=True)
    link_maps = Column(Text, nullable=True)
    status_masjid = Column(String(50), nullable=True)
    status_tanah = Column(String(50), nullable=True)
    luas_tanah = Column(String(50), nullable=True)
    luas_bangunan = Column(String(50), nullable=True)
    daya_tampung = Column(String(50), nullable=True)
    thumbnail = Column(String(255), nullable=True, default="masjid-default.jpg")
    deskripsi = Column(Text, nullable=True)
    slug_masjid = Column(String(255), nullable=True, unique=True)
    status_aktif = Column(Integer, default=1)
    noregis_simas = Column(String(255), nullable=True)
    running_text_website = Column(Text, nullable=True)
    background_warna_website = Column(String(50), nullable=True)
    warna_tulisan_website = Column(String(50), nullable=True)
    kode_upz = Column(String(50), nullable=True)
    nama_upz = Column(String(255), nullable=True)
    label_upz = Column(String(50), nullable=True)
    no_sk_upz = Column(String(255), nullable=True)
    id_provinsi = Column(Integer, nullable=True)
    id_kabupaten_kota = Column(Integer, nullable=True)
    id_kecamatan = Column(Integer, nullable=True)
    id_kelurahan_desa = Column(Integer, nullable=True)
    email_masjid = Column(String(255), nullable=True)
    nohp_masjid = Column(String(50), nullable=True)
    web_masjid = Column(String(255), nullable=True)
    video_masjid = Column(Text, nullable=True)
    show_saldo = Column(Integer, default=1)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
