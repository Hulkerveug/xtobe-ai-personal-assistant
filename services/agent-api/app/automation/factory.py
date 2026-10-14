from functools import lru_cache
from .engine import AutomationEngine

@lru_cache(maxsize=1)
def get_engine():
    # returns a singleton mock engine for local-only Phase A/B
    return AutomationEngine()
