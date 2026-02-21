# [Task]: T022
# [From]: speckit.plan / Phase 3: Backend Authentication
# [Spec]: speckit.specify / FR-001, FR-002

from datetime import datetime, timedelta
from typing import Any, Optional, Union
from jose import jwt, JWTError
from passlib.context import CryptContext

from app.core.config import settings
from app.schemas.user import TokenPayload

pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verifies if a plain password matches a hashed password.
    [Spec]: Functional Requirements / Password hashing MUST be used
    """
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    """
    Hashes a plain password.
    [Spec]: Functional Requirements / Password hashing MUST be used
    """
    return pwd_context.hash(password)

def create_access_token(subject: Union[str, Any], expires_delta: Optional[timedelta] = None) -> str:
    """
    Creates a JWT access token.
    """
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    
    to_encode = {"exp": expire, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt

def decode_access_token(token: str) -> Optional[TokenPayload]:
    """
    Decodes a JWT access token and returns its payload.
    """
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        return TokenPayload(**payload)
    except JWTError:
        return None
