# [Task]: T018
# [From]: speckit.plan / Phase 2: Database and ORM Setup
# [Spec]: speckit.specify / TR-004, TR-005

from sqlmodel import Session
from app.core.db import engine, get_session
import pytest
from sqlalchemy import text

# Override get_session dependency for testing
@pytest.fixture(name="session")
def session_fixture():
    # In a real application, you might use a test database or an in-memory database.
    # For now, we'll just yield a session from the main engine.
    # This will connect to the configured DATABASE_URL in .env
    with Session(engine) as session:
        yield session

def test_database_connection(session: Session):
    """
    Test that the database can be connected to and a session can be obtained.
    [Spec]: SC-005
    """
    # Simply trying to get a session and execute a dummy query will confirm connectivity
    # This test will initially fail if DATABASE_URL is misconfigured or DB is unreachable
    try:
        session.exec(text("SELECT 1"))
        assert True
    except Exception as e:
        pytest.fail(f"Could not connect to database or obtain session: {e}")
