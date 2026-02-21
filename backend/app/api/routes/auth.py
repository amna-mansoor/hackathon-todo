# [Task]: T027
# [From]: speckit.plan / Phase 3: Backend Authentication
# [Spec]: spec-kit/specs/features/authentication.md

from datetime import timedelta
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session, select

from app.core.config import settings
from app.core.security import create_access_token, get_password_hash, verify_password
from app.core.db import get_session
from app.models.user import User
from app.schemas.user import Token, UserCreate, UserRead

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register", response_model=UserRead)
def register_user(user_in: UserCreate, session: Annotated[Session, Depends(get_session)]):
    """
    Register a new user.
    [Spec]: User Story: User Authentication / Acceptance Criteria 6
    """
    user = session.exec(select(User).where(User.email == user_in.email)).first()
    if user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email already exists",
        )
    
    hashed_password = get_password_hash(user_in.password)
    user_db = User(email=user_in.email, password_hash=hashed_password)
    session.add(user_db)
    session.commit()
    session.refresh(user_db)
    return user_db

@router.post("/login", response_model=Token)
def login_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    session: Annotated[Session, Depends(get_session)]
):
    """
    OAuth2 compatible token login, get an access token for future requests.
    [Spec]: User Story: User Authentication / Acceptance Criteria 1
    """
    user = session.exec(select(User).where(User.email == form_data.username)).first()
    if not user or not verify_password(form_data.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        subject=str(user.id), expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
