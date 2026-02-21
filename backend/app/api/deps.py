# [Task]: T020
# [From]: speckit.plan / Phase 3: Backend Authentication
# [Spec]: speckit.specify / TR-007

from typing import Generator
from sqlmodel import Session
from app.core.db import engine

def get_db() -> Generator[Session, None, None]:
    """
    Dependency to get a database session.
    """
    with Session(engine) as session:
        yield session

# Placeholder for get_current_user dependency
# This will be implemented in T032
async def get_current_user():
    pass
