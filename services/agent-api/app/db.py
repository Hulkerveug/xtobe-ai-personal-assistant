import os
from sqlalchemy import create_engine, text

DB_PATH = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'xtobe.db')

def init_db():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    engine = create_engine(f'sqlite:///{DB_PATH}')
    with engine.connect() as conn:
        conn.execute(text('''
        CREATE TABLE IF NOT EXISTS migrations (
            id INTEGER PRIMARY KEY,
            name TEXT,
            applied_at DATETIME DEFAULT CURRENT_TIMESTAMP
        );
        '''))
        conn.commit()
