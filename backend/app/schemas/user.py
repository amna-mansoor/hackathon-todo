# [Task]: T021
# [From]: speckit.plan / Phase 3: Backend Authentication
# [Spec]: speckit.specify / Key Entities, FR-001, FR-002

from typing import Optional
from uuid import UUID
from sqlmodel import Field, SQLModel
from datetime import datetime

# Shared properties for a user
class UserBase(SQLModel):
    email: str = Field(index=True)

# Properties to receive via API on creation
class UserCreate(UserBase):
    password: str

# Properties to receive via API on update
class UserUpdate(UserBase):
    password: Optional[str] = None

# Properties to return via API
class UserRead(UserBase):
    id: UUID
    # No password_hash here, as it's sensitive

# Token schema for JWT
class Token(SQLModel):
    access_token: str
    token_type: str = "bearer"

class TokenPayload(SQLModel):
    sub: Optional[UUID] = None
    exp: Optional[datetime] = None
