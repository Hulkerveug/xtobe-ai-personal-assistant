# XTOBE AI Personal Assistant — Phase A scaffold

This repository contains the Phase A scaffold for XTOBE AI COMMAND — desktop assistant.

What this commit includes (phase-a-ui-backend branch):

- apps/desktop: React + TypeScript starter files, Guardian activation UI and voice mock components
- services/agent-api: FastAPI health endpoint and SQLite initialization
- docs/: Guardian UI design and implementation plan files

Next steps (local):
- From apps/desktop: npm install && npm run dev (or yarn)
- From services/agent-api: python -m venv .venv && .venv\Scripts\activate (Windows) && pip install -r requirements.txt && uvicorn app.main:app --reload

DO NOT PUSH or publish without authorization beyond this branch.
