# [Task]: T015
# [From]: speckit.plan / Phase 2: Database and ORM Setup
# [Spec]: speckit.specify / Key Entities, FR-008, FR-009
# [Source]: spec-kit/specs/database/schema.md

from typing import List, Optional
from datetime import datetime
from uuid import UUID, uuid4

from sqlmodel import Field, Relationship, SQLModel

# Import Task to resolve forward reference
from .task import Task

class User(SQLModel, table=True):
    """
    Represents a registered user of the application.
    [Spec]: Key Entities / User
    """
    id: Optional[UUID] = Field(default_factory=uuid4, primary_key=True)
    email: str = Field(index=True, unique=True, nullable=False)
    password_hash: str = Field(nullable=False, max_length=256)
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    updated_at: datetime = Field(default_factory=datetime.utcnow, nullable=False, sa_column_kwargs={"onupdate": datetime.utcnow})

    tasks: List["Task"] = Relationship(back_populates="owner")
