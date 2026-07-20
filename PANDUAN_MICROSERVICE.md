# Panduan Menjalankan MENARA API (Microservice) Secara Lokal

## 🏗️ Arsitektur

Sekarang backend terdiri dari **5 microservice** yang berjalan independen:

| Service | Port | URL | Fungsinya |
|---------|------|-----|-----------|
| **Auth Service** | 8001 | http://localhost:8001 | Login, Register, Users |
| **Masjid Service** | 8002 | http://localhost:8002 | Masjid, Wilayah, Rekap |
| **Content Service** | 8003 | http://localhost:8003 | Home, Informasi, Kajian, Acara, dll |
| **Transaction Service** | 8004 | http://localhost:8004 | BukuKas, Sync Push/Pull |
| **Admin Service** | 8005 | http://localhost:8005 | Admin CRUD, Master Data |

> **⚠️ Penting!** Masing-masing service **HARUS dijalankan bersamaan** agar semua fitur berfungsi.

---

## 📋 Prasyarat

- Python 3.12+
- MySQL 8.0 (database sudah berisi data clone)
- `pip install -r requirements.txt`

---

## 🚀 Cara 1: Jalankan Semua Service Sekaligus (Docker)

**Paling mudah — cukup 1 perintah:**

```bash
cd C:\Users\User\Downloads\BAZNAS\ci4\backend
docker-compose up --build -d
```

Ini akan menjalankan:
- 1 container MySQL (port 3307)
- 5 container service (port 8001-8005)

Cek status:
```bash
docker-compose ps
```

Lihat log:
```bash
docker-compose logs -f
```

---

## 🚀 Cara 2: Jalankan Manual (5 Terminal Terpisah)

**Untuk development/debugging — lihat output setiap service:**

### Terminal 1 — Auth Service (port 8001)
```bash
cd C:\Users\User\Downloads\BAZNAS\ci4\backend
uvicorn services.auth_service.main:app --reload --port 8001
```

### Terminal 2 — Masjid Service (port 8002)
```bash
cd C:\Users\User\Downloads\BAZNAS\ci4\backend
uvicorn services.masjid_service.main:app --reload --port 8002
```

### Terminal 3 — Content Service (port 8003)
```bash
cd C:\Users\User\Downloads\BAZNAS\ci4\backend
uvicorn services.content_service.main:app --reload --port 8003
```

### Terminal 4 — Transaction Service (port 8004)
```bash
cd C:\Users\User\Downloads\BAZNAS\ci4\backend
uvicorn services.transaction_service.main:app --reload --port 8004
```

### Terminal 5 — Admin Service (port 8005)
```bash
cd C:\Users\User\Downloads\BAZNAS\ci4\backend
uvicorn services.admin_service.main:app --reload --port 8005
```

---

## 🚀 Cara 3: Satu Terminal dengan & (Background)

**Untuk development cepat — semua jalan di 1 terminal:**

```bash
cd C:\Users\User\Downloads\BAZNAS\ci4\backend

uvicorn services.auth_service.main:app --reload --port 8001 &
uvicorn services.masjid_service.main:app --reload --port 8002 &
uvicorn services.content_service.main:app --reload --port 8003 &
uvicorn services.transaction_service.main:app --reload --port 8004 &
uvicorn services.admin_service.main:app --reload --port 8005 &

echo "Semua service berjalan!"
```

---

## ✅ Verifikasi Service Berjalan

Cek health endpoint masing-masing service:

```bash
# Cek semua service
curl http://localhost:8001/health
curl http://localhost:8002/health
curl http://localhost:8003/health
curl http://localhost:8004/health
curl http://localhost:8005/health
```

Response sukses:
```json
{"service":"auth","status":"ok"}
{"service":"masjid","status":"ok"}
{"service":"content","status":"ok"}
{"service":"transaction","status":"ok"}
{"service":"admin","status":"ok"}
```

---

## 📖 Swagger UI per Service

Setiap service punya dokumentasi Swagger sendiri:

| Service | Swagger UI |
|---------|-----------|
| Auth | http://localhost:8001/docs |
| Masjid | http://localhost:8002/docs |
| Content | http://localhost:8003/docs |
| Transaction | http://localhost:8004/docs |
| Admin | http://localhost:8005/docs |

---

## 🛑 Menghentikan Service

Jika pakai Docker:
```bash
docker-compose down
```

Jika manual (Ctrl+C di setiap terminal, atau):
```bash
# Windows
taskkill /F /IM python.exe

# Linux/Mac
pkill -f uvicorn
```
