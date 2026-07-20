from sqlalchemy import Column, String, Integer, DateTime, Text, Numeric, Date
from shared.config.database import Base
import datetime


class BukukasPenerimaan(Base):
    __tablename__ = "bukukas_penerimaan"
    id_bukukas_penerimaan = Column(Integer, primary_key=True, autoincrement=True)
    jalur_akses = Column(String(50), nullable=True)
    tanggal = Column(Date, nullable=True)
    nominal_masuk = Column(Numeric(15, 2), nullable=True, default=0)
    jumlah_donatur = Column(Integer, nullable=True, default=0)
    keterangan = Column(Text, nullable=True)
    lampiran = Column(String(255), nullable=True)
    id_jenis_dana = Column(Integer, nullable=True)
    id_jenis_harta = Column(Integer, nullable=True)
    id_label_info_dana = Column(Integer, nullable=True)
    id_level = Column(Integer, nullable=True)
    id_jalur_akses = Column(String(50), nullable=True)
    id_provinsi = Column(Integer, nullable=True)
    id_kabupaten_kota = Column(Integer, nullable=True)
    id_kecamatan = Column(Integer, nullable=True)
    id_kelurahan_desa = Column(Integer, nullable=True)
    kode_org_baznas = Column(String(50), nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)


class BukukasPengeluaran(Base):
    __tablename__ = "bukukas_pengeluaran"
    id_bukukas_pengeluaran = Column(Integer, primary_key=True, autoincrement=True)
    jalur_akses = Column(String(50), nullable=True)
    tanggal = Column(Date, nullable=True)
    nominal_keluar = Column(Numeric(15, 2), nullable=True, default=0)
    jumlah_penerima_manfaat = Column(Integer, nullable=True, default=0)
    keterangan = Column(Text, nullable=True)
    lampiran = Column(String(255), nullable=True)
    id_jenis_dana = Column(Integer, nullable=True)
    id_jenis_harta = Column(Integer, nullable=True)
    id_label_info_dana = Column(Integer, nullable=True)
    id_level = Column(Integer, nullable=True)
    id_jalur_akses = Column(String(50), nullable=True)
    nama_masjid = Column(String(255), nullable=True)
    id_provinsi = Column(Integer, nullable=True)
    id_kabupaten_kota = Column(Integer, nullable=True)
    id_kecamatan = Column(Integer, nullable=True)
    id_kelurahan_desa = Column(Integer, nullable=True)
    kode_org_baznas = Column(String(50), nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)


class BukuAset(Base):
    __tablename__ = "buku_aset"
    id_buku_aset = Column(Integer, primary_key=True, autoincrement=True)
    jalur_akses = Column(String(50), nullable=True)
    id_jalur_akses = Column(String(50), nullable=True)
    tanggal = Column(Date, nullable=True)
    nama_barang = Column(String(255), nullable=True)
    jumlah = Column(Integer, nullable=True)
    harga_perolehan = Column(Numeric(15, 2), nullable=True)
    tahun_perolehan = Column(String(10), nullable=True)
    lokasi = Column(String(255), nullable=True)
    id_jenis_perolehan_aset = Column(Integer, nullable=True)
    id_provinsi = Column(Integer, nullable=True)
    id_kabupaten_kota = Column(Integer, nullable=True)
    id_kecamatan = Column(Integer, nullable=True)
    id_kelurahan_desa = Column(Integer, nullable=True)
    catatan = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)


class BerkasLaporan(Base):
    __tablename__ = "berkas_laporan"
    id_berkas_laporan = Column(Integer, primary_key=True, autoincrement=True)
    jalur_akses = Column(String(50), nullable=True)
    id_jalur_akses = Column(String(50), nullable=True)
    tanggal = Column(Date, nullable=True)
    nama_laporan = Column(String(255), nullable=True)
    tahun_periode = Column(String(10), nullable=True)
    id_jenis_laporan = Column(Integer, nullable=True)
    file_laporan = Column(String(255), nullable=True)
    id_provinsi = Column(Integer, nullable=True)
    id_kabupaten_kota = Column(Integer, nullable=True)
    id_kecamatan = Column(Integer, nullable=True)
    id_kelurahan_desa = Column(Integer, nullable=True)
    catatan = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)


class Kas(Base):
    __tablename__ = "kas"
    id_kas = Column(Integer, primary_key=True, autoincrement=True)
    parent_id = Column(String(50), nullable=True)
    coa = Column(String(50), nullable=True)
    jenis_kas = Column(String(50), nullable=True)
    pj = Column(String(255), nullable=True)
    tipe = Column(String(20), nullable=True)
    uraian = Column(Text, nullable=True)
    masuk = Column(Numeric(15, 2), nullable=True, default=0)
    keluar = Column(Numeric(15, 2), nullable=True, default=0)
    sisa_dana = Column(Numeric(15, 2), nullable=True)
    pemakaian = Column(Numeric(15, 2), nullable=True)
    status_kas = Column(String(50), nullable=True, default="proses")
    metode_bayar = Column(String(50), nullable=True)
    catatan_kas = Column(Text, nullable=True)
    lampiran = Column(String(255), nullable=True)
    bukti_laporan = Column(String(255), nullable=True)
    uraian_laporan = Column(Text, nullable=True)
    scan_pengajuan = Column(String(255), nullable=True)
    scan_pertum = Column(String(255), nullable=True)
    bukti_bayar = Column(String(255), nullable=True)
    report_date = Column(Date, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    created_by = Column(Integer, nullable=True)


class Coa(Base):
    __tablename__ = "coa"
    id = Column(Integer, primary_key=True, autoincrement=True)
    kode = Column(String(50), nullable=True)
    tahun = Column(String(10), nullable=True)
    jenis = Column(String(20), nullable=True)
    nama = Column(String(255), nullable=True)
    nominal = Column(Numeric(15, 2), nullable=True, default=0)
    tipe = Column(String(20), nullable=True)
    parent_id = Column(String(50), nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)


class SaranDanMasukan(Base):
    __tablename__ = "saran_dan_masukan"
    id_saran_dan_masukan = Column(Integer, primary_key=True, autoincrement=True)
    kode_org_baznas = Column(String(50), nullable=True)
    jalur_akses = Column(String(50), nullable=True)
    id_jalur_akses = Column(String(50), nullable=True)
    judul_saran_dan_masukan = Column(String(255), nullable=True)
    deskripsi_saran_dan_masukan = Column(Text, nullable=True)
    lampiran = Column(String(255), nullable=True)
    id_level = Column(Integer, nullable=True)
    id_provinsi = Column(Integer, nullable=True)
    id_kabupaten_kota = Column(Integer, nullable=True)
    id_kecamatan = Column(Integer, nullable=True)
    id_kelurahan_desa = Column(Integer, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
