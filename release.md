# Release Notes — MENARA API

## Version 2.0.0 (2024)

### Architecture Change
- Restructured from monolithic `app/` to service-oriented architecture under `src/`
- Layered pattern: Routes → Services → Queries (SQL) → Models
- Centralized Dependency Injection via `src/container.py`

### New Structure
```
src/
├── main.py              # Entry point
├── container.py         # DI container + app factory
├── config/              # Environment, database, constants
├── routes/              # Thin HTTP handlers
├── services/            # Business logic
├── queries/             # SQLAlchemy queries
├── models/              # SQLAlchemy ORM models
├── middlewares/         # Auth, RBAC, validation, error, logging
└── utils/               # Helpers: JWT, response, errors, route wrapper
```

### Deployment
- Docker support with multi-stage build
- Docker Compose with MySQL 8
- Google Cloud Build & Cloud Run scripts
- Environment template: `env_example`

### Migration from v1
1. Copy `.env` from `env_example` and configure
2. Run database migrations from `database/` folder
3. Start server: `uvicorn src.main:app --reload`
