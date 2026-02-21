# [Task]: T023, T025
# [From]: speckit.plan / Phase 3: Backend Authentication
# [Spec]: spec-kit/specs/features/authentication.md

from app.core.security import verify_password, get_password_hash, create_access_token, decode_access_token
from app.schemas.user import TokenPayload
from datetime import timedelta
from app.core.config import settings
import pytest
from jose import jwt

def test_password_hashing_and_verification():
    """
    Test that a password can be hashed and then verified correctly.
    [Spec]: Functional Requirements / Password hashing MUST be used
    """
    plain_password = "mysecretpassword"
    hashed_password = get_password_hash(plain_password)
    
    assert verify_password(plain_password, hashed_password)
    assert not verify_password("wrongpassword", hashed_password)

def test_jwt_token_creation_and_decoding():
    """
    Test that a JWT token can be created and then decoded correctly.
    [Spec]: FR-001
    """
    user_id = "a1b2c3d4-e5f6-7890-1234-567890abcdef"
    token = create_access_token(subject=user_id, expires_delta=timedelta(minutes=1))
    
    payload = decode_access_token(token)
    
    assert payload is not None
    assert str(payload.sub) == user_id
    assert "exp" in payload.model_dump()
    
def test_jwt_token_expiration():
    """
    Test that an expired JWT token cannot be decoded.
    """
    user_id = "a1b2c3d4-e5f6-7890-1234-567890abcdef"
    token = create_access_token(subject=user_id, expires_delta=timedelta(minutes=-1)) # Create an expired token
    
    payload = decode_access_token(token)
    
    assert payload is None
