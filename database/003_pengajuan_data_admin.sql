-- ============================================================
-- MENARA Database — Migration 003
-- Pengajuan Masjid: kolom data admin pemohon lengkap + slug masjid
-- (flow baru: kode & slug diterbitkan LANGSUNG saat pengajuan dibuat;
--  Admin BAZNAS mengkonfirmasi masjid + admin sekaligus saat approve)
-- Jalankan SEKALI pada database yang sudah ada.
-- ============================================================

ALTER TABLE pengajuan_masjid
    ADD COLUMN slug_masjid VARCHAR(255) NULL AFTER kode_org_baznas,
    ADD COLUMN jk_pemohon VARCHAR(10) NULL AFTER email_pemohon,
    ADD COLUMN nohp_pemohon VARCHAR(50) NULL AFTER jk_pemohon,
    ADD COLUMN alamat_pemohon TEXT NULL AFTER nohp_pemohon;
