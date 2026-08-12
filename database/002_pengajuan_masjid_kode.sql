-- ============================================================
-- MENARA Database — Migration 002
-- Pengajuan Masjid: tambah kolom untuk flow daftar masjid → kode masjid → daftar admin masjid
-- Jalankan SEKALI pada database yang sudah ada (fresh install sudah tercakup di 001).
-- ============================================================

ALTER TABLE pengajuan_masjid
    ADD COLUMN kode_org_baznas VARCHAR(50) NULL AFTER status_pengajuan,
    ADD COLUMN nama_pemohon VARCHAR(255) NULL AFTER kode_org_baznas,
    ADD COLUMN email_pemohon VARCHAR(255) NULL AFTER nama_pemohon;
