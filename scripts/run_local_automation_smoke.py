import os
from app.automation.factory import get_engine

if __name__ == '__main__':
    # quick smoke script to run a mock workflow
    engine = get_engine()
    wf_list = [w.id for w in __import__('app.automation.workflow_registry', fromlist=['']).list_all()]
    print('Available workflows:', wf_list)
    res = engine.start_execution('daily-expo-watch', {'type':'MANUAL'})
    print('Execution', res.execution_id, res.state)
