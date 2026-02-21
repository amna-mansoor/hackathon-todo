# [Task]: T009, T017
# [From]: speckit.plan / Phase 1: Project Setup & Monorepo Configuration, Phase 2: Database and ORM Setup
# [Spec]: speckit.specify

from fastapi import FastAPI
from sqlmodel import SQLModel
from app.core.db import engine # Import the engine

# Import all models so SQLModel can find them
from app.models.user import User
from app.models.task import Task


def create_db_and_tables():
    """
    Creates all database tables defined by SQLModel.
    """
    SQLModel.update_forward_refs() # Ensure all relationships are resolved
    SQLModel.metadata.create_all(engine)


app = FastAPI(
    title="Full-Stack Todo API",
    description="FastAPI backend for the Full-Stack Todo application.",
    version="0.1.0",
)

@app.on_event("startup")
def on_startup():
    """
    Event handler that runs when the FastAPI application starts up.
    """
    create_db_and_tables()

@app.get("/")
async def root():
    return {"message": "Welcome to the Full-Stack Todo API!"}
