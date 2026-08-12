-- ============================================================
-- MENARA Database — Initial Schema
-- Migration 001: Create all core tables
-- ============================================================

-- Drop database if exists, then create
-- CREATE DATABASE IF NOT EXISTS menara_masjid_revamp;
-- USE menara_masjid_revamp;

-- ============================================================
-- MASTER DATA
-- ============================================================

CREATE TABLE IF NOT EXISTS levels (
    id_level INT AUTO_INCREMENT PRIMARY KEY,
    nama_level VARCHAR(255),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS labels (
    id_labels INT AUTO_INCREMENT PRIMARY KEY,
    nama_labels VARCHAR(255),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS jenis_dana (
    id_jenis_dana INT AUTO_INCREMENT PRIMARY KEY,
    nama_jenis_dana VARCHAR(255),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS jenis_harta (
    id_jenis_harta INT AUTO_INCREMENT PRIMARY KEY,
    nama_jenis_harta VARCHAR(255),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS label_info_dana (
    id_label_info_dana INT AUTO_INCREMENT PRIMARY KEY,
    nama_label_info_dana VARCHAR(255),
    kode_label_info_dana VARCHAR(50),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS tema (
    id_tema INT AUTO_INCREMENT PRIMARY KEY,
    nama_tema VARCHAR(255),
    parent_id VARCHAR(50),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- ============================================================
-- WILAYAH
-- ============================================================

CREATE TABLE IF NOT EXISTS provinsi (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nama VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS kabupaten_kota (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_provinsi INT,
    nama VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS kecamatan (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_kabupaten_kota INT,
    nama VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS kelurahan_desa (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_kecamatan INT,
    nama VARCHAR(255)
);

-- ============================================================
-- USERS
-- ============================================================

CREATE TABLE IF NOT EXISTS users (
    id_user INT AUTO_INCREMENT PRIMARY KEY,
    kode_org_baznas VARCHAR(50),
    jalur_akses VARCHAR(50),
    nama VARCHAR(255),
    jk VARCHAR(10),
    nohp VARCHAR(50),
    email VARCHAR(255) UNIQUE,
    password VARCHAR(255),
    alamat TEXT,
    avatar VARCHAR(255) DEFAULT 'user-default.png',
    id_level INT,
    id_labels INT,
    status_aktif INT DEFAULT 1,
    id_jalur_akses VARCHAR(50),
    id_provinsi INT,
    id_kabupaten_kota INT,
    id_kecamatan INT,
    id_kelurahan_desa INT,
    catatan TEXT,
    show_saldo INT DEFAULT 1,
    last_login DATETIME,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- ============================================================
-- MASJID
-- ============================================================

CREATE TABLE IF NOT EXISTS masjid (
    id_masjid VARCHAR(50) PRIMARY KEY,
    kode_org_baznas VARCHAR(50),
    nama_masjid VARCHAR(255),
    jenis_masjid VARCHAR(50),
    tipologi VARCHAR(50),
    alamat_masjid TEXT,
    link_maps TEXT,
    status_masjid VARCHAR(50),
    status_tanah VARCHAR(50),
    luas_tanah VARCHAR(50),
    luas_bangunan VARCHAR(50),
    daya_tampung VARCHAR(50),
    thumbnail VARCHAR(255) DEFAULT 'masjid-default.jpg',
    deskripsi TEXT,
    slug_masjid VARCHAR(255) UNIQUE,
    status_aktif INT DEFAULT 1,
    noregis_simas VARCHAR(255),
    running_text_website TEXT,
    background_warna_website VARCHAR(50),
    warna_tulisan_website VARCHAR(50),
    kode_upz VARCHAR(50),
    nama_upz VARCHAR(255),
    label_upz VARCHAR(50),
    no_sk_upz VARCHAR(255),
    id_provinsi INT,
    id_kabupaten_kota INT,
    id_kecamatan INT,
    id_kelurahan_desa INT,
    email_masjid VARCHAR(255),
    nohp_masjid VARCHAR(50),
    web_masjid VARCHAR(255),
    video_masjid TEXT,
    show_saldo INT DEFAULT 1,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- ============================================================
-- MASJID DETAIL
-- ============================================================

CREATE TABLE IF NOT EXISTS fasilitas (
    id_fasilitas INT AUTO_INCREMENT PRIMARY KEY,
    parent_id VARCHAR(50),
    nama_fasilitas VARCHAR(255),
    foto_fasilitas VARCHAR(255),
    keterangan TEXT
);

CREATE TABLE IF NOT EXISTS images (
    id INT AUTO_INCREMENT PRIMARY KEY,
    parent_id VARCHAR(50),
    name VARCHAR(255),
    src VARCHAR(500)
);

CREATE TABLE IF NOT EXISTS document (
    id INT AUTO_INCREMENT PRIMARY KEY,
    parent_id VARCHAR(50),
    document_name VARCHAR(255),
    document_type VARCHAR(50),
    document_src VARCHAR(500)
);

CREATE TABLE IF NOT EXISTS bank (
    id_bank INT AUTO_INCREMENT PRIMARY KEY,
    parent_id VARCHAR(50),
    nama_bank VARCHAR(255),
    norek VARCHAR(100),
    atas_nama VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS medsos (
    id_medsos INT AUTO_INCREMENT PRIMARY KEY,
    parent_id VARCHAR(50),
    name_medsos VARCHAR(255),
    url_medsos VARCHAR(500)
);

-- ============================================================
-- TRANSAKSI
-- ============================================================

CREATE TABLE IF NOT EXISTS bukukas_penerimaan (
    id_bukukas_penerimaan INT AUTO_INCREMENT PRIMARY KEY,
    kode_org_baznas VARCHAR(50),
    id_jalur_akses VARCHAR(50),
    id_jenis_dana INT,
    id_jenis_harta INT,
    id_label_info_dana INT,
    nominal_masuk DECIMAL(15, 2),
    jumlah_donatur INT,
    keterangan TEXT,
    tanggal DATE,
    id_provinsi INT,
    id_kabupaten_kota INT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS bukukas_pengeluaran (
    id_bukukas_pengeluaran INT AUTO_INCREMENT PRIMARY KEY,
    kode_org_baznas VARCHAR(50),
    id_jalur_akses VARCHAR(50),
    id_jenis_dana INT,
    id_jenis_harta INT,
    id_label_info_dana INT,
    nominal_keluar DECIMAL(15, 2),
    jumlah_penerima_manfaat INT,
    keterangan TEXT,
    tanggal DATE,
    id_provinsi INT,
    id_kabupaten_kota INT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- ============================================================
-- CONTENT / CMS
-- ============================================================

CREATE TABLE IF NOT EXISTS informasi (
    id_informasi INT AUTO_INCREMENT PRIMARY KEY,
    judul_informasi VARCHAR(255),
    isi_informasi TEXT,
    foto_informasi VARCHAR(255),
    slug_informasi VARCHAR(255) UNIQUE,
    status_aktif INT DEFAULT 1,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS kajian (
    id_kajian INT AUTO_INCREMENT PRIMARY KEY,
    id_masjid VARCHAR(50),
    judul VARCHAR(255),
    slug_kajian VARCHAR(255) UNIQUE,
    keterangan TEXT,
    foto VARCHAR(255),
    pemateri VARCHAR(255),
    tgl_kajian DATE,
    id_tema INT,
    status_aktif INT DEFAULT 1,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- ============================================================
-- PENGAJUAN MASJID
-- ============================================================

CREATE TABLE IF NOT EXISTS pengajuan_masjid (
    id_pengajuan INT AUTO_INCREMENT PRIMARY KEY,
    nama_masjid VARCHAR(255),
    alamat_masjid TEXT,
    email_masjid VARCHAR(255),
    nohp_masjid VARCHAR(50),
    id_provinsi INT,
    id_kabupaten_kota INT,
    id_kecamatan INT,
    id_kelurahan_desa INT,
    status_pengajuan VARCHAR(50) DEFAULT 'Menunggu',
    kode_org_baznas VARCHAR(50),
    slug_masjid VARCHAR(255),
    nama_pemohon VARCHAR(255),
    email_pemohon VARCHAR(255),
    jk_pemohon VARCHAR(10),
    nohp_pemohon VARCHAR(50),
    alamat_pemohon TEXT,
    id_user INT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS pengajuan_user_masjid (
    id_pengajuan INT AUTO_INCREMENT PRIMARY KEY,
    id_masjid VARCHAR(50),
    nama VARCHAR(255),
    email VARCHAR(255),
    nohp VARCHAR(50),
    status_pengajuan VARCHAR(50) DEFAULT 'Menunggu',
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
