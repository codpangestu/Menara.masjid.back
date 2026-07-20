# MENARA API — Microservice Backend

**M**anajemen **E**konomi, **N**azhir, **A**mal, **R**umah **A**mal

Backend API microservice untuk platform MENARA, dibangun dengan FastAPI.

## Tech Stack

- **Runtime:** Python 3.12
- **Framework:** FastAPI
- **ORM:** SQLAlchemy 2.0
- **Database:** MySQL 8.0 (shared database)
- **Auth:** JWT + API Key
- **Container:** Docker + Docker Compose
- **Cloud:** Google Cloud Run

## Arsitektur Microservice

```
backend/
├── shared/                     # Shared library (config, models, utils)
│   ├── config/                 # environment.py, database.py, constants.py
│   ├── models/                 # SQLAlchemy ORM models
│   ├── middlewares/            # Auth, RBAC, Validation, Error, Logging
│   ├── schemas/                # Request/response schemas
│   └── utils/                  # response_helper, jwt_helper, app_error
│
├── services/                   # 5 Microservices
│   ├── auth_service/           # Port 8001 — Auth + Users
│   ├── masjid_service/         # Port 8002 — Masjid + Wilayah + Rekap
│   ├── content_service/        # Port 8003 — Content + Home + Public
│   ├── transaction_service/    # Port 8004 — BukuKas + Sync
│   └── admin_service/          # Port 8005 — Admin CRUD + Master Data
│
├── database/                   # SQL migrations
├── docker-compose.yml          # 5 services + MySQL
└── Dockerfile                  # Build image (multi-service)
```

## Quick Start

### 1. Clone & Setup

```bash
git clone <repo-url>
cd menara-api

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt
```

### 2. Configure Environment

```bash
cp env_example .env
# Edit .env with your database credentials
```

### 3. Run Database Migrations

Execute SQL files in `database/` folder against your MySQL instance.

### 4. Start All Services (Development)

Each service runs on its own port. Start them in separate terminals:

```bash
# Terminal 1 - Auth Service (port 8001)
uvicorn services.auth_service.main:app --reload --port 8001

# Terminal 2 - Masjid Service (port 8002)
uvicorn services.masjid_service.main:app --reload --port 8002

# Terminal 3 - Content Service (port 8003)
uvicorn services.content_service.main:app --reload --port 8003

# Terminal 4 - Transaction Service (port 8004)
uvicorn services.transaction_service.main:app --reload --port 8004

# Terminal 5 - Admin Service (port 8005)
uvicorn services.admin_service.main:app --reload --port 8005
```

### 5. Access API Docs

Each service has its own Swagger UI:
- Auth: http://localhost:8001/docs
- Masjid: http://localhost:8002/docs
- Content: http://localhost:8003/docs
- Transaction: http://localhost:8004/docs
- Admin: http://localhost:8005/docs

## Docker Deployment

```bash
# Build and run ALL 5 services + MySQL
docker-compose up --build -d

# Or run a single service manually:
docker build -t menara-auth .
docker run -p 8001:8001 --env-file .env menara-auth uvicorn services.auth_service.main:app --host 0.0.0.0 --port 8001
```

## Microservices Overview

| Service | Port | Routes | Endpoints |
|---------|------|--------|-----------|
| **Auth** | 8001 | 16 | Login, Register, Users CRUD |
| **Masjid** | 8002 | 16 | Masjid, Wilayah, Rekap |
| **Content** | 8003 | 48 | Home, Informasi, Kajian, Acara, dll |
| **Transaction** | 8004 | 11 | BukuKas, Sync Push/Pull |
| **Admin** | 8005 | 38 | Admin CRUD, Master Data |

## Environment Variables

See `env_example` for all configuration options.

## License

Internal project — BAZNAS
