from sqlalchemy import Column, String, Integer, DateTime, Text, Date
from shared.config.database import Base
import datetime


class Informasi(Base):
    __tablename__ = "informasi"
    id_informasi = Column(Integer, primary_key=True, autoincrement=True)
    judul_informasi = Column(String(255), nullable=True)
    isi_informasi = Column(Text, nullable=True)
    foto_informasi = Column(String(255), nullable=True)
    slug_informasi = Column(String(255), nullable=True)
    id_user = Column(Integer, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)


class Kajian(Base):
    __tablename__ = "kajian"
    id_kajian = Column(Integer, primary_key=True, autoincrement=True)
    tgl_kajian = Column(Date, nullable=True)
    judul = Column(String(255), nullable=True)
    pemateri = Column(String(255), nullable=True)
    keterangan = Column(Text, nullable=True)
    poster = Column(String(255), nullable=True)
    slug_kajian = Column(String(255), nullable=True)
    status_aktif = Column(Integer, default=1)
    id_tema = Column(Integer, nullable=True)
    id_user = Column(Integer, nullable=True)
    id_masjid = Column(String(50), nullable=True)
    nama_masjid = Column(String(255), nullable=True)
    video_kajian = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)


class Acara(Base):
    __tablename__ = "acara"
    id_acara = Column(Integer, primary_key=True, autoincrement=True)
    tgl_acara = Column(Date, nullable=True)
    judul = Column(String(255), nullable=True)
    penulis = Column(String(255), nullable=True)
    keterangan = Column(Text, nullable=True)
    poster = Column(String(255), nullable=True)
    slug_acara = Column(String(255), nullable=True)
    status_aktif = Column(Integer, default=1)
    id_kategori_acara = Column(Integer, nullable=True)
    id_user = Column(Integer, nullable=True)
    id_masjid = Column(String(50), nullable=True)
    nama_masjid = Column(String(255), nullable=True)
    video_acara = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)


class Cerita(Base):
    __tablename__ = "cerita"
    id_cerita = Column(Integer, primary_key=True, autoincrement=True)
    tgl_cerita = Column(Date, nullable=True)
    judul = Column(String(255), nullable=True)
    penulis = Column(String(255), nullable=True)
    keterangan = Column(Text, nullable=True)
    poster = Column(String(255), nullable=True)
    slug_cerita = Column(String(255), nullable=True)
    status_aktif = Column(Integer, default=1)
    id_kategori_cerita = Column(Integer, nullable=True)
    id_user = Column(Integer, nullable=True)
    id_masjid = Column(String(50), nullable=True)
    video_cerita = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)


class Donasi(Base):
    __tablename__ = "donasi"
    id_donasi = Column(Integer, primary_key=True, autoincrement=True)
    tgl_donasi = Column(Date, nullable=True)
    judul = Column(String(255), nullable=True)
    penulis = Column(String(255), nullable=True)
    keterangan = Column(Text, nullable=True)
    jumlah_dana_terkumpul = Column(String(50), nullable=True)
    target_pengumpulan_dana = Column(String(50), nullable=True)
    batas_tgl_pengumpulan = Column(Date, nullable=True)
    kontak_informasi = Column(String(255), nullable=True)
    progres_status = Column(String(50), nullable=True)
    poster = Column(String(255), nullable=True)
    rekap_data_pengumpulan = Column(Text, nullable=True)
    slug_donasi = Column(String(255), nullable=True)
    status_aktif = Column(Integer, default=1)
    id_kategori_donasi = Column(Integer, nullable=True)
    id_user = Column(Integer, nullable=True)
    id_masjid = Column(String(50), nullable=True)
    video_donasi = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)


class Postingan(Base):
    __tablename__ = "postingan"
    id_postingan = Column(Integer, primary_key=True, autoincrement=True)
    tgl_postingan = Column(Date, nullable=True)
    judul = Column(String(255), nullable=True)
    penulis = Column(String(255), nullable=True)
    keterangan = Column(Text, nullable=True)
    poster = Column(String(255), nullable=True)
    slug_postingan = Column(String(255), nullable=True)
    status_aktif = Column(Integer, default=1)
    id_kategori_postingan = Column(Integer, nullable=True)
    id_user = Column(Integer, nullable=True)
    id_masjid = Column(String(50), nullable=True)
    video_postingan = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)


class PanduanPengguna(Base):
    __tablename__ = "panduan_pengguna"
    id_panduan_pengguna = Column(Integer, primary_key=True, autoincrement=True)
    judul = Column(String(255), nullable=True)
    keterangan = Column(Text, nullable=True)
    lampiran = Column(String(255), nullable=True)
    slug_panduan_pengguna = Column(String(255), nullable=True)
    status_aktif = Column(Integer, default=1)
    id_kategori_panduan_pengguna = Column(Integer, nullable=True)
    id_user = Column(Integer, nullable=True)
    video_panduan_pengguna = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)


class PanduanPengelola(Base):
    __tablename__ = "panduan_pengelola"
    id_panduan_pengelola = Column(Integer, primary_key=True, autoincrement=True)
    judul = Column(String(255), nullable=True)
    keterangan = Column(Text, nullable=True)
    lampiran = Column(String(255), nullable=True)
    slug_panduan_pengelola = Column(String(255), nullable=True)
    status_aktif = Column(Integer, default=1)
    id_kategori_panduan_pengelola = Column(Integer, nullable=True)
    id_user = Column(Integer, nullable=True)
    video_panduan_pengelola = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)


class Pengumuman(Base):
    __tablename__ = "pengumuman"
    id_pengumuman = Column(Integer, primary_key=True, autoincrement=True)
    tgl_pengumuman = Column(Date, nullable=True)
    judul = Column(String(255), nullable=True)
    penulis = Column(String(255), nullable=True)
    keterangan = Column(Text, nullable=True)
    poster = Column(String(255), nullable=True)
    slug_pengumuman = Column(String(255), nullable=True)
    status_aktif = Column(Integer, default=1)
    id_kategori_pengumuman = Column(Integer, nullable=True)
    id_user = Column(Integer, nullable=True)
    id_masjid = Column(String(50), nullable=True)
    video_pengumuman = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)


class Repository(Base):
    __tablename__ = "repository"
    id_repository = Column(Integer, primary_key=True, autoincrement=True)
    judul_repository = Column(String(255), nullable=True)
    isi_repository = Column(Text, nullable=True)
    foto_repository = Column(String(255), nullable=True)
    id_user = Column(Integer, nullable=True)
    slug_repository = Column(String(255), nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)


class DokumentasiPengembangan(Base):
    __tablename__ = "dokumentasi_pengembangan"
    id_dokumentasi_pengembangan = Column(Integer, primary_key=True, autoincrement=True)
    judul_dokumentasi_pengembangan = Column(String(255), nullable=True)
    isi_dokumentasi_pengembangan = Column(Text, nullable=True)
    foto_dokumentasi_pengembangan = Column(String(255), nullable=True)
    id_user = Column(Integer, nullable=True)
    slug_dokumentasi_pengembangan = Column(String(255), nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)


class DokumentasiPengujian(Base):
    __tablename__ = "dokumentasi_pengujian"
    id_dokumentasi_pengujian = Column(Integer, primary_key=True, autoincrement=True)
    judul_dokumentasi_pengujian = Column(String(255), nullable=True)
    isi_dokumentasi_pengujian = Column(Text, nullable=True)
    foto_dokumentasi_pengujian = Column(String(255), nullable=True)
    id_user = Column(Integer, nullable=True)
    slug_dokumentasi_pengujian = Column(String(255), nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)


class DokumentasiSosialisasi(Base):
    __tablename__ = "dokumentasi_sosialisasi"
    id_dokumentasi_sosialisasi = Column(Integer, primary_key=True, autoincrement=True)
    judul_dokumentasi_sosialisasi = Column(String(255), nullable=True)
    isi_dokumentasi_sosialisasi = Column(Text, nullable=True)
    foto_dokumentasi_sosialisasi = Column(String(255), nullable=True)
    id_user = Column(Integer, nullable=True)
    slug_dokumentasi_sosialisasi = Column(String(255), nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)


class InfoPemberitahuan(Base):
    __tablename__ = "info_pemberitahuan"
    id_info_pemberitahuan = Column(Integer, primary_key=True, autoincrement=True)
    judul_info_pemberitahuan = Column(String(255), nullable=True)
    isi_info_pemberitahuan = Column(Text, nullable=True)
    foto_info_pemberitahuan = Column(String(255), nullable=True)
    id_user = Column(Integer, nullable=True)
    slug_info_pemberitahuan = Column(String(255), nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)


class Infografis(Base):
    __tablename__ = "infografis"
    id_infografis = Column(Integer, primary_key=True, autoincrement=True)
    judul_infografis = Column(String(255), nullable=True)
    isi_infografis = Column(Text, nullable=True)
    foto_infografis = Column(String(255), nullable=True)
    id_user = Column(Integer, nullable=True)
    slug_infografis = Column(String(255), nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)


class Inspirasi(Base):
    __tablename__ = "inspirasi"
    id_inspirasi = Column(Integer, primary_key=True, autoincrement=True)
    judul_inspirasi = Column(String(255), nullable=True)
    isi_inspirasi = Column(Text, nullable=True)
    foto_inspirasi = Column(String(255), nullable=True)
    id_user = Column(Integer, nullable=True)
    slug_inspirasi = Column(String(255), nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)


class Infovideo(Base):
    __tablename__ = "infovideo"
    id_infovideo = Column(Integer, primary_key=True, autoincrement=True)
    judul_infovideo = Column(String(255), nullable=True)
    isi_infovideo = Column(Text, nullable=True)
    iframe_infovideo = Column(Text, nullable=True)
    foto_infovideo = Column(String(255), nullable=True)
    id_user = Column(Integer, nullable=True)
    slug_infovideo = Column(String(255), nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)


class Infoayat(Base):
    __tablename__ = "infoayat"
    id_infoayat = Column(Integer, primary_key=True, autoincrement=True)
    judul_infoayat = Column(String(255), nullable=True)
    isi_infoayat = Column(Text, nullable=True)
    foto_infoayat = Column(String(255), nullable=True)
    id_user = Column(Integer, nullable=True)
    slug_infoayat = Column(String(255), nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)


class Infohadits(Base):
    __tablename__ = "infohadits"
    id_infohadits = Column(Integer, primary_key=True, autoincrement=True)
    judul_infohadits = Column(String(255), nullable=True)
    isi_infohadits = Column(Text, nullable=True)
    foto_infohadits = Column(String(255), nullable=True)
    id_user = Column(Integer, nullable=True)
    slug_infohadits = Column(String(255), nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)


class Infodoa(Base):
    __tablename__ = "infodoa"
    id_infodoa = Column(Integer, primary_key=True, autoincrement=True)
    judul_infodoa = Column(String(255), nullable=True)
    isi_infodoa = Column(Text, nullable=True)
    foto_infodoa = Column(String(255), nullable=True)
    id_user = Column(Integer, nullable=True)
    slug_infodoa = Column(String(255), nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
