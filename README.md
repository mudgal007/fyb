# Find Your Balance

Find Your Balance is a futuristic productivity and wellness platform that blends long-term goal design, daily planning, mindful tracking, and community momentum. The project is split into a **FastAPI** backend and a **React + Tailwind + Framer Motion** frontend.

## Monorepo structure

```
backend/   # FastAPI application with modular routers, PostgreSQL-ready models, and JWT auth
frontend/  # Vite-powered React interface with Tailwind styling and motion-enhanced UI
```

## Backend

* Framework: FastAPI (async)
* Database: SQLAlchemy models targeting PostgreSQL (asyncpg driver)
* Auth: OAuth2 password flow with JWT, role-based guards
* Realtime: WebSocket broadcast channel for live activity feed
* Personalization services for mood nudges and goal reminders

### Setup

```bash
cd backend
poetry install
poetry run uvicorn app.main:app --reload
```

Set environment variables (or `.env`) such as `FYB_DATABASE_URL` to point to your PostgreSQL instance.

### Tests

```bash
cd backend
poetry run pytest
```

## Frontend

* React 18 with Vite, Tailwind CSS, and Framer Motion
* Drag-and-drop dashboard modules, responsive cards, and animated journal canvas
* Service worker for offline-first support
* WebSocket client to stream live community activity from the backend

### Setup

```bash
cd frontend
npm install
npm run dev
```

The dev server listens on `http://localhost:5173` and expects the API at `http://localhost:8000`.

### Build

```bash
npm run build
```

## Admin & analytics

The backend exposes an admin dashboard endpoint (`/api/v1/auth/admin/dashboard`) guarded by role checks. This is a foundation for deeper analytics dashboards.

## License

MIT
