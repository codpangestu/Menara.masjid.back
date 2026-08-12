from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from services.auth_service.queries.auth_queries import get_user_by_email, get_user_by_id, create_user, update_last_login
from shared.utils.jwt_helper import verify_password, get_password_hash, create_access_token
from shared.config.constants import DEFAULT_PASSWORD, DEFAULT_AVATAR, DEFAULT_USER_LEVEL, JALUR_MASJID
from shared.models.users import Users
from shared.models.masjid import Masjid


class AuthService:
    def login(self, db: Session, email: str, password: str):
        user = get_user_by_email(db, email)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Email tidak terdaftar",
            )
        if not verify_password(password, user.password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Password salah",
            )
        if user.status_aktif != 1:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Status akun tidak aktif",
            )

        update_last_login(db, user)
        token = create_access_token(data={"sub": str(user.id_user)})
        return {
            "access_token": token,
            "user": {
                "id_user": user.id_user,
                "nama": user.nama,
                "email": user.email,
                "jalur_akses": user.jalur_akses,
                "id_jalur_akses": user.id_jalur_akses,
                "avatar": user.avatar,
                "id_level": user.id_level,
                "id_labels": user.id_labels,
                "nohp": user.nohp,
            }
        }

    def login_admin_masjid(self, db: Session, email: str, password: str):
        user = get_user_by_email(db, email)
        if not user or not verify_password(password, user.password):
            raise HTTPException(status_code=401, detail="Email atau password salah")
        if user.jalur_akses != JALUR_MASJID:
            raise HTTPException(status_code=403, detail="Akses ditolak. Bukan akun Masjid")
        if user.status_aktif != 1:
            raise HTTPException(status_code=403, detail="Akun tidak aktif")

        update_last_login(db, user)
        token = create_access_token(data={"sub": str(user.id_user)})
        return {
            "access_token": token,
            "user": {
                "id_user": user.id_user,
                "nama": user.nama,
                "email": user.email,
                "jalur_akses": user.jalur_akses,
                "id_jalur_akses": user.id_jalur_akses,
                "avatar": user.avatar,
                "id_level": user.id_level,
            }
        }

    def login_admin_pusat(self, db: Session, email: str, password: str):
        user = get_user_by_email(db, email)
        if not user or not verify_password(password, user.password):
            raise HTTPException(status_code=401, detail="Email atau password salah")
        if user.jalur_akses != "Pusat":
            raise HTTPException(status_code=403, detail="Akses ditolak")
        if user.status_aktif != 1:
            raise HTTPException(status_code=403, detail="Akun tidak aktif")

        token = create_access_token(data={"sub": str(user.id_user)})
        return {
            "access_token": token,
            "user": {
                "id_user": user.id_user,
                "nama": user.nama,
                "email": user.email,
                "jalur_akses": user.jalur_akses,
                "avatar": user.avatar,
            }
        }

    def register_user(self, db: Session, data: dict):
        """
        Register Admin Masjid (flow baru).
        Wajib mengisi kode_org_baznas (kode masjid) yang diterbitkan Admin BAZNAS
        setelah pengajuan masjid disetujui. Kode divalidasi terhadap tabel masjid:
        - kode tidak ditemukan / masjid belum disetujui → ditolak (register gagal)
        - valid → user dibuat sebagai Admin Masjid (id_level=2, jalur_akses=Masjid,
          id_jalur_akses=id_masjid) dan langsung bisa login via tab Admin Masjid.
        """
        existing = get_user_by_email(db, data["email"])
        if existing:
            return {"status_code": "403", "status": "Email sudah terdaftar"}

        kode = (data.get("kode_org_baznas") or "").strip()
        if not kode:
            return {"status_code": "400", "status": "Kode masjid wajib diisi"}

        # Validasi: masjid dengan kode tsb harus sudah terdaftar (berarti pengajuannya sudah disetujui)
        masjid = db.query(Masjid).filter(Masjid.kode_org_baznas == kode).first()
        if not masjid or masjid.status_aktif != 1:
            return {
                "status_code": "404",
                "status": "Kode masjid tidak valid. Pastikan pengajuan masjid Anda sudah disetujui Admin BAZNAS.",
            }

        create_user(
            db,
            jalur_akses=JALUR_MASJID,
            id_jalur_akses=masjid.id_masjid,
            nama=data.get("nama"),
            jk=data.get("jk"),
            alamat=data.get("alamat"),
            email=data.get("email"),
            nohp=data.get("nohp", ""),
            kode_org_baznas=kode,
            password=get_password_hash(DEFAULT_PASSWORD),
            id_level=2,  # Admin Masjid
            id_labels=1 if data.get("id_labels") is None else data.get("id_labels"),  # 1 = Admin
            avatar=DEFAULT_AVATAR,
            status_aktif=1,
            catatan=data.get("catatan", ""),
        )
        return {"status_code": "000", "status": "Sukses"}

    def get_me(self, current_user: Users):
        return {
            "id_user": current_user.id_user,
            "nama": current_user.nama,
            "email": current_user.email,
            "jalur_akses": current_user.jalur_akses,
            "id_jalur_akses": current_user.id_jalur_akses,
            "avatar": current_user.avatar,
            "id_level": current_user.id_level,
            "id_labels": current_user.id_labels,
            "nohp": current_user.nohp,
            "jk": current_user.jk,
            "alamat": current_user.alamat,
            "status_aktif": current_user.status_aktif,
        }

    def logout(self):
        return {"status_code": "000", "status": "Berhasil logout"}
