# [Task]: T014
# [From]: speckit.plan / Phase 2: Database and ORM Setup
# [Spec]: speckit.specify / TR-004, TR-005

from sqlmodel import create_engine, Session
from app.core.config import settings

# Ensure DATABASE_URL is set in .env or environment variables
# For Neon, it typically looks like:
# postgresql+psycopg2://[user]:[password]@[endpoint_hostname]/[db_name]?sslmode=require
engine = create_engine(str(settings.DATABASE_URL))

def get_session():
    """
    Dependency to get a database session.
    """
    with Session(engine) as session:
        yield session
