Purpose
-------
This file gives concise, actionable guidance for AI coding agents working in this repository so they can be productive immediately.

Quick summary
-------------
- Backend: a small FastAPI app under [backend/app](backend/app#L1).
- Frontend: a top-level `frontend/` folder (no further structure discovered).
- Virtualenv: a `.venv/` directory exists at repository root — prefer using it for commands.

How to run the backend locally
------------------------------
- Activate the repo virtualenv (macOS):

  source .venv/bin/activate

- Run the FastAPI app with hot reload (preferred for development):

  python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000

- Alternate: the `backend/app/main.py` includes a `if __name__ == "__main__"` block that calls `uvicorn.run()`, so `python backend/app/main.py` also starts the server.

Project architecture notes (what matters)
----------------------------------------
- Entry point: [backend/app/main.py](backend/app/main.py#L1) — defines the FastAPI `app` and a simple `/` route.
- Routing: add route modules under [backend/app/api](backend/app/api#L1) and include them on the FastAPI app (look for router `include_router` patterns when adding new endpoints).
- Business logic: place service code under [backend/app/services](backend/app/services#L1). Keep handlers thin and move side-effects into services.
- Data models: keep Pydantic or ORM models under [backend/app/models](backend/app/models#L1).
- Separation guideline: controllers (api) -> services -> models. Follow this layering when adding code.

Conventions and patterns observed
--------------------------------
- Small, explicit modules: prefer small files under `api/`, `services/`, and `models/` rather than large monoliths.
- Use FastAPI decorators for endpoints (example in [backend/app/main.py](backend/app/main.py#L1)).
- Keep side effects (DB, external calls) in `services/` to make unit testing easier.

Tests and CI
------------
- No tests or CI config discovered. If adding tests, mirror the `api/services/models` layout in a `tests/` folder and keep tests small and focused.

Editing guidance for AI agents
-----------------------------
- Make small, focused changes and run the server locally to smoke-test endpoints.
- When adding endpoints, create a router module in `backend/app/api`, export a `router` (FastAPI APIRouter), and import/register it in `backend/app/main.py`.
- When changing interfaces between `api` and `services`, update `models/` if new DTOs are needed.
- Preserve the project's simple style: clear function names, small modules, minimal dependencies.

Integration points to watch for
------------------------------
- Frontend ↔ Backend: frontend likely talks to the backend over HTTP at `http://127.0.0.1:8000/`. Keep CORS and host/port in mind when adding features.
- External dependencies: no lockfile or requirements file was found. If you add packages, also add a `requirements.txt` or `pyproject.toml` and document install steps.

When you can't discover something
-------------------------------
- If an action requires build/test commands or credentials not present in the repo, ask the human for the missing details (DB connection strings, external API keys, test runners).

Files to inspect when starting work
---------------------------------
- [backend/app/main.py](backend/app/main.py#L1)
- [backend/app/api](backend/app/api#L1)
- [backend/app/services](backend/app/services#L1)
- [backend/app/models](backend/app/models#L1)

If something in this file is incorrect or incomplete, tell me what to add or point me to the missing files.
