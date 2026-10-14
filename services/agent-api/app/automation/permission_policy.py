from typing import Set

ROLE_PERMISSIONS = {
    "user": {"READ_LOCAL","COMMUNICATE"},
    "admin": {"READ_LOCAL","COMMUNICATE","WRITE_LOCAL","WRITE_EXTERNAL","PUBLISH","EXECUTE_BROWSER","USE_SECRET"}
}

def allow_action(role: str, permission: str) -> bool:
    return permission in ROLE_PERMISSIONS.get(role, set())
