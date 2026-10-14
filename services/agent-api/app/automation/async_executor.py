import asyncio
from typing import Optional
from .workflow_schema import WorkflowExecution
from .mock_executor import MockExecutor
from .audit_service import AuditService

class AsyncExecutor:
    def __init__(self, audit: Optional[AuditService] = None):
        self.audit = audit or AuditService()
        self._executor = MockExecutor(self.audit)

    async def run_async(self, workflow, execution: WorkflowExecution):
        # Run mock executor in thread to simulate async behavior without network
        loop = asyncio.get_running_loop()
        result = await loop.run_in_executor(None, self._executor.run, workflow, execution)
        return result
