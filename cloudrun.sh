#!/bin/bash
# ============================================================
# cloudrun.sh — Deploy MENARA API to Google Cloud Run
# ============================================================
# Prerequisites:
#   1. gcloud CLI installed and authenticated
#   2. Docker installed
#   3. Google Cloud Artifact Registry repo created
# ============================================================

set -euo pipefail

# === CONFIGURATION ===
PROJECT_ID="${PROJECT_ID:-your-gcp-project-id}"
REGION="${REGION:-asia-southeast2}"
REPO_NAME="${REPO_NAME:-menara-api}"
SERVICE_NAME="${SERVICE_NAME:-menara-api}"
IMAGE_TAG="$(date +%Y%m%d-%H%M%S)"

# === BUILD & PUSH ===
echo "=== Building Docker image ==="
docker build -t "${REGION}-docker.pkg.dev/${PROJECT_ID}/${REPO_NAME}/service:${IMAGE_TAG}" .
docker tag "${REGION}-docker.pkg.dev/${PROJECT_ID}/${REPO_NAME}/service:${IMAGE_TAG}" "${REGION}-docker.pkg.dev/${PROJECT_ID}/${REPO_NAME}/service:latest"

echo "=== Pushing to Artifact Registry ==="
docker push "${REGION}-docker.pkg.dev/${PROJECT_ID}/${REPO_NAME}/service:${IMAGE_TAG}"
docker push "${REGION}-docker.pkg.dev/${PROJECT_ID}/${REPO_NAME}/service:latest"

# === DEPLOY TO CLOUD RUN ===
echo "=== Deploying to Cloud Run ==="
gcloud run deploy "${SERVICE_NAME}" \
  --image="${REGION}-docker.pkg.dev/${PROJECT_ID}/${REPO_NAME}/service:${IMAGE_TAG}" \
  --region="${REGION}" \
  --platform=managed \
  --allow-unauthenticated \
  --set-env-vars="DB_HOST=${DB_HOST:-127.0.0.1},DB_PORT=${DB_PORT:-3306},DB_DATABASE=${DB_DATABASE:-menara_masjid_revamp},DB_USERNAME=${DB_USERNAME:-root},DB_PASSWORD=${DB_PASSWORD:-cauburuk123},SECRET_KEY=${SECRET_KEY:-menara-secret-key-change-in-production},API_KEY=${API_KEY:-menara23apikey},APP_NAME=MENARA API,APP_VERSION=2.0.0,DEBUG=false"

echo "=== Deploy Success! ==="
