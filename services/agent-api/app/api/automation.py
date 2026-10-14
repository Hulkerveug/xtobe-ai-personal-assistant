from fastapi import APIRouter, HTTPException, BackgroundTasks
from pydantic import BaseModel, Field
from typing import Any, Dict
from fastapi.responses import JSONResponse
from functools import lru_cache

from app.automation.factory import get_engine
from app.automation.workflow_registry import list_all, get

router = APIRouter(prefix="/api/automation", tags=["automation"])

# response wrapper helper
def phase_response(payload: Dict[str, Any]):
    base = {
        "phase": "PHASE_A_B_MOCK_ONLY",
        "external_actions_performed": False,
        "live_integrations_enabled": False
    }
    base.update(payload)
    return JSONResponse(content=base)

class TriggerRequest(BaseModel):
    type: str = Field(..., example="MANUAL")
    metadata: Dict[str, Any] = Field(default_factory=dict)

@router.get("/workflows")
async def list_workflows():
    workflows = [
        {"id": wf.id, "name": wf.name, "description": wf.description, "trigger": wf.trigger.dict(), "steps": [s.dict() for s in wf.steps]}
        for wf in list_all()
    ]
    return phase_response({"workflows": workflows})

@router.get("/workflows/{workflow_id}")
async def get_workflow(workflow_id: str):
    wf = get(workflow_id)
    if not wf:
        raise HTTPException(status_code=404, detail="workflow not found")
    return phase_response({"workflow": wf.dict()})

@router.post("/workflows/{workflow_id}/run-mock")
async def run_workflow_mock(workflow_id: str, trigger: TriggerRequest):
    engine = get_engine()
    try:
        result = engine.start_execution(workflow_id, trigger.dict())
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc))
    return phase_response({"execution": result.dict()})

@router.post("/workflows/{workflow_id}/run-mock-async")
async def run_workflow_mock_async(workflow_id: str, trigger: TriggerRequest, background: BackgroundTasks):
    engine = get_engine()
    # Schedule in background (still local-only). We return execution_id immediately with created state.
    async def _run():
        await engine.start_execution_async(workflow_id, trigger.dict())
    background.add_task(_run)
    return phase_response({"status": "queued"})

@router.get("/executions/{execution_id}")
async def get_execution(execution_id: str):
    engine = get_engine()
    rec = engine.store.get(execution_id)
    if not rec:
        raise HTTPException(status_code=404, detail="execution not found")
    return phase_response({"execution": rec})
