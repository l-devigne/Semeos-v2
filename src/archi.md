# Project architecture — Developer overview

## Overview
A simple multi-service app composed of a Python backend, a Vite-based frontend, and a PostgreSQL data volume, orchestrated with Docker Compose for local development.

## Services
- **Backend:** Python service in `src/backend` providing HTTP APIs and business logic. Built from `requirements.txt` and containerized via the backend `Dockerfile`.
- **Frontend:** Vite-powered single-page app in `src/frontend` serving the UI and calling backend APIs.
- **Database:** PostgreSQL persists data under the `data/` folder and is run as a Docker-managed volume.

## How they interact
- Frontend calls backend HTTP endpoints (CORS enabled) to read/write data.
- Backend connects to Postgres over Docker Compose networking using standard credentials.
- Docker Compose wires networking and volumes so services run together locally.

## Local development
- Bring up the full stack:

```bash
docker compose up --build
```

- Frontend dev (hot reload):

```bash
cd frontend && npm install && npm run dev
```

- Backend dev: run inside the container via Compose or run locally using a virtualenv and `src/backend/requirements.txt`.

## Code layout (dev-focused)
- `src/backend/`: Python source, API routes, `requirements.txt`, backend `Dockerfile`.
- `src/frontend/` or `frontend/`: Vite app, `package.json`, dev scripts.
- `data/`: Postgres data files and config persisted between restarts.

## Notes for contributors
- Use Docker Compose for reproducible local environments and CI parity.
- Keep API changes backward-compatible; update frontend calls when responses change.
- For DB schema changes, include migration steps or scripts and persist backups from `data/` when needed.