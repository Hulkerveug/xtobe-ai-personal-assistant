from .workflow_registry import get, load_sample_templates
from .workflow_schema import WorkflowExecution
from .mock_executor import MockExecutor
from .audit_service import AuditService
from .execution_store import ExecutionStore
from .async_executor import AsyncExecutor
from typing import Optional
import asyncio

class AutomationEngine:
    def __init__(self, audit_db_path: Optional[str] = None, store_db_path: Optional[str] = None):
        self.audit = AuditService(db_path=audit_db_path)
        self.store = ExecutionStore(db_path=store_db_path)
        self.executor = MockExecutor(self.audit)
        self.async_executor = AsyncExecutor(self.audit)
        load_sample_templates()

    def start_execution(self, workflow_id: str, trigger: dict) -> WorkflowExecution:
        wf = get(workflow_id)
        if not wf:
            raise ValueError("workflow not found")
        exec_model = WorkflowExecution(workflow_id=workflow_id, trigger=trigger)
        self.audit.log(exec_model.execution_id, "execution.created", {"workflow_id": workflow_id})
        # synchronous mock run for compatibility
        result = self.executor.run(wf, exec_model)
        # persist
        try:
            self.store.save(result)
        except Exception:
            pass
        return result

    async def start_execution_async(self, workflow_id: str, trigger: dict) -> WorkflowExecution:
        wf = get(workflow_id)
        if not wf:
            raise ValueError("workflow not found")
        exec_model = WorkflowExecution(workflow_id=workflow_id, trigger=trigger)
        self.audit.log(exec_model.execution_id, "execution.created", {"workflow_id": workflow_id})
        result = await self.async_executor.run_async(wf, exec_model)
        try:
            self.store.save(result)
        except Exception:
            pass
        return result
