# Dockerfile — Service Beasiswa
# Build stage
FROM python:3.12-slim AS builder

WORKDIR /app

# Install build dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc default-libmysqlclient-dev && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# Runtime stage
FROM python:3.12-slim

WORKDIR /app

# Install runtime deps for mysqlclient
RUN apt-get update && \
    apt-get install -y --no-install-recommends default-libmysqlclient-dev && \
    rm -rf /var/lib/apt/lists/*

COPY --from=builder /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH

COPY . .

# Default port (override via SERVICE_PORT env or docker-compose)
EXPOSE 8000

# Default service (use docker-compose to run specific services)
# Available services:
#   services.auth_service.main:app      — port 8001
#   services.masjid_service.main:app    — port 8002
#   services.content_service.main:app   — port 8003
#   services.transaction_service.main:app — port 8004
#   services.admin_service.main:app     — port 8005
CMD ["uvicorn", "services.auth_service.main:app", "--host", "0.0.0.0", "--port", "8001"]
