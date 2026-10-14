import sqlite3
import os
from typing import Optional, Dict, Any
from .workflow_schema import WorkflowExecution

DB_PATH = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'workflow_executions.db')

class ExecutionStore:
    def __init__(self, db_path: Optional[str] = None):
        self.db_path = db_path or DB_PATH
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        self._init()

    def _init(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute('''CREATE TABLE IF NOT EXISTS executions (
                execution_id TEXT PRIMARY KEY,
                workflow_id TEXT,
                state TEXT,
                started_at TEXT,
                finished_at TEXT,
                steps TEXT,
                error TEXT
            )''')
            conn.commit()

    def save(self, execution: WorkflowExecution):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute('''INSERT OR REPLACE INTO executions (execution_id, workflow_id, state, started_at, finished_at, steps, error)
                             VALUES (?, ?, ?, ?, ?, ?, ?)''', (
                execution.execution_id,
                execution.workflow_id,
                execution.state,
                execution.started_at.isoformat() if execution.started_at else None,
                execution.finished_at.isoformat() if execution.finished_at else None,
                str(execution.step_results),
                execution.error
            ))
            conn.commit()

    def get(self, execution_id: str) -> Optional[Dict[str, Any]]:
        with sqlite3.connect(self.db_path) as conn:
            cur = conn.execute('SELECT execution_id,workflow_id,state,started_at,finished_at,steps,error FROM executions WHERE execution_id=?', (execution_id,))
            row = cur.fetchone()
            if not row:
                return None
            return {
                'execution_id': row[0], 'workflow_id': row[1], 'state': row[2], 'started_at': row[3], 'finished_at': row[4], 'steps': row[5], 'error': row[6]
            }
