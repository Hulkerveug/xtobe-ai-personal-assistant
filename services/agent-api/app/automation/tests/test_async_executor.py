import pytest
import asyncio
from ..workflow_registry import load_sample_templates, get
from ..engine import AutomationEngine

def test_async_executor_runs(tmp_path):
    load_sample_templates()
    engine = AutomationEngine(audit_db_path=str(tmp_path/'audit.db'), store_db_path=str(tmp_path/'store.db'))
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    result = loop.run_until_complete(engine.start_execution_async('daily-expo-watch', {'type':'SCHEDULED'}))
    assert result.state == 'COMPLETED'
