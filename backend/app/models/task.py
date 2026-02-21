# [Task]: T016
# [From]: speckit.plan / Phase 2: Database and ORM Setup
# [Spec]: speckit.specify / Key Entities, FR-008, FR-009, FR-010, FR-011
# [Source]: spec-kit/specs/database/schema.md

from typing import Optional
from datetime import datetime
from uuid import UUID, uuid4

from sqlmodel import Field, Relationship, SQLModel

class Task(SQLModel, table=True):
    """
    Represents a single to-do item belonging to a User.
    [Spec]: Key Entities / Task
    """
    id: Optional[UUID] = Field(default_factory=uuid4, primary_key=True)
    description: str = Field(nullable=False, max_length=255)
    status: str = Field(default="Pending", nullable=False, max_length=10) # "Pending" or "Complete"
    
    user_id: UUID = Field(foreign_key="users.id", index=True, nullable=False)
    
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    updated_at: datetime = Field(default_factory=datetime.utcnow, nullable=False, sa_column_kwargs={"onupdate": datetime.utcnow})

    owner: Optional["User"] = Relationship(back_populates="tasks")
