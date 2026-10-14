from fastapi import FastAPI
from .db import init_db

app = FastAPI(title="XTOBE Agent API (Phase A)")

@app.on_event("startup")
async def startup_event():
    init_db()

@app.get("/healthz")
async def healthz():
    return {"status": "ok", "phase": "phase-a-ui-backend"}
