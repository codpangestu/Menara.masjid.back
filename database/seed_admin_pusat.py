"""
Seeder: Admin Pusat account for MENARA Masjid
Jalankan: python -m database.seed_admin_pusat
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from shared.config.database import SessionLocal, engine
from shared.config.constants import DEFAULT_PASSWORD
from shared.utils.jwt_helper import get_password_hash
from sqlalchemy import text


LEVELS = [
    (1, "Admin Pusat"),
    (2, "Admin Masjid"),
    (3, "Petugas"),
]

LABELS = [
    (1, "Admin", ""),
    (2, "Petugas", ""),
    (3, "Jamaah", ""),
]

ADMIN_PUSAT = {
    "kode_org_baznas": "BAZNAS",
    "jalur_akses": "Pusat",
    "nama": "Admin Pusat BAZNAS",
    "jk": "Laki-laki",
    "nohp": "081234567890",
    "email": "admin_pusat@baznas.go.id",
    "password": DEFAULT_PASSWORD,
    "alamat": "Jl. Lapangan Banteng Timur 3-4, Jakarta Pusat",
    "id_level": 1,
    "id_labels": 1,
    "status_aktif": 1,
}


def seed_levels(db):
    print("Seeding levels...")
    for id_level, nama_level in LEVELS:
        exists = db.execute(
            text("SELECT id_level FROM levels WHERE id_level = :id"),
            {"id": id_level},
        ).fetchone()
        if not exists:
            db.execute(
                text("INSERT INTO levels (id_level, nama_level) VALUES (:id, :nama)"),
                {"id": id_level, "nama": nama_level},
            )
            print(f"  + Level: {nama_level} (id={id_level})")
        else:
            print(f"  = Level '{nama_level}' sudah ada (id={id_level})")
    db.commit()


def seed_labels(db):
    print("Seeding labels...")
    for id_labels, nama_labels, parent_id in LABELS:
        exists = db.execute(
            text("SELECT id_labels FROM labels WHERE id_labels = :id"),
            {"id": id_labels},
        ).fetchone()
        if not exists:
            db.execute(
                text("INSERT INTO labels (id_labels, nama_labels, parent_id) VALUES (:id, :nama, :pid)"),
                {"id": id_labels, "nama": nama_labels, "pid": parent_id},
            )
            print(f"  + Label: {nama_labels} (id={id_labels})")
        else:
            print(f"  = Label '{nama_labels}' sudah ada (id={id_labels})")
    db.commit()


def seed_admin_pusat(db):
    print("Seeding admin pusat...")
    email = ADMIN_PUSAT["email"]
    exists = db.execute(
        text("SELECT id_user FROM users WHERE email = :email"),
        {"email": email},
    ).fetchone()
    if exists:
        print(f"  = User '{email}' sudah ada (id={exists[0]})")
        return

    hashed = get_password_hash(ADMIN_PUSAT["password"])

    db.execute(
        text(
            """
            INSERT INTO users
                (kode_org_baznas, jalur_akses, nama, jk, nohp, email, password,
                 alamat, id_level, id_labels, status_aktif)
            VALUES
                (:kode_org_baznas, :jalur_akses, :nama, :jk, :nohp, :email, :password,
                 :alamat, :id_level, :id_labels, :status_aktif)
            """
        ),
        {
            "kode_org_baznas": ADMIN_PUSAT["kode_org_baznas"],
            "jalur_akses": ADMIN_PUSAT["jalur_akses"],
            "nama": ADMIN_PUSAT["nama"],
            "jk": ADMIN_PUSAT["jk"],
            "nohp": ADMIN_PUSAT["nohp"],
            "email": ADMIN_PUSAT["email"],
            "password": hashed,
            "alamat": ADMIN_PUSAT["alamat"],
            "id_level": ADMIN_PUSAT["id_level"],
            "id_labels": ADMIN_PUSAT["id_labels"],
            "status_aktif": ADMIN_PUSAT["status_aktif"],
        },
    )
    db.commit()
    print(f"  + Admin pusat '{email}' berhasil dibuat!")


def main():
    print("=" * 50)
    print("  MENARA Masjid - Seed Admin Pusat")
    print("=" * 50)
    print()

    db = SessionLocal()
    try:
        seed_levels(db)
        print()
        seed_labels(db)
        print()
        seed_admin_pusat(db)

        print()
        print("=" * 50)
        print("  Credential untuk login:")
        print(f"  Email    : {ADMIN_PUSAT['email']}")
        print(f"  Password : {ADMIN_PUSAT['password']}")
        print("=" * 50)
    except Exception as e:
        db.rollback()
        print(f"\nERROR: {e}")
        sys.exit(1)
    finally:
        db.close()


if __name__ == "__main__":
    main()
