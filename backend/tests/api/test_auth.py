# [Task]: T028, T030
# [From]: speckit.plan / Phase 3: Backend Authentication
# [Spec]: spec-kit/specs/features/authentication.md

from fastapi.testclient import TestClient
from sqlmodel import Session, SQLModel, create_engine
from app.main import app
from app.core.config import settings
from app.models.user import User
from app.models.task import Task
import pytest

# Use a test database for tests
DATABASE_URL = "sqlite:///./test.db" # In-memory SQLite for tests
engine = create_engine(DATABASE_URL)

def create_db_and_tables():
    SQLModel.metadata.clear() # Clear metadata for a clean test state
    # Ensure models are imported so SQLModel discovers them
    from app.models.user import User # Local import for test metadata
    from app.models.task import Task # Local import for test metadata
    SQLModel.update_forward_refs() # Resolve relationships
    SQLModel.metadata.create_all(engine)

def get_session_override():
    with Session(engine) as session:
        yield session

@pytest.fixture(name="client")
def client_fixture():
    # Create the test database
    create_db_and_tables()
    # Override the get_session dependency
    app.dependency_overrides[Session] = get_session_override
    with TestClient(app) as client:
        yield client
    # Clean up the test database
    SQLModel.metadata.drop_all(engine)
    app.dependency_overrides = {} # Clear overrides

def test_register_user_success(client: TestClient):
    """
    Test successful user registration.
    [Spec]: User Story: User Authentication / Acceptance Criteria 6
    """
    response = client.post(
        "/auth/register",
        json={"email": "test@example.com", "password": "securepassword"}
    )
    assert response.status_code == 200
    assert response.json()["email"] == "test@example.com"
    assert "id" in response.json()

def test_register_user_duplicate_email(client: TestClient):
    """
    Test registration with a duplicate email.
    [Spec]: User Story: User Authentication / Acceptance Criteria 7
    """
    client.post(
        "/auth/register",
        json={"email": "duplicate@example.com", "password": "password123"}
    )
    response = client.post(
        "/auth/register",
        json={"email": "duplicate@example.com", "password": "password123"}
    )
    assert response.status_code == 400
    assert response.json()["detail"] == "User with this email already exists"

def test_login_user_success(client: TestClient):
    """
    Test successful user login.
    [Spec]: User Story: User Authentication / Acceptance Criteria 1
    """
    client.post(
        "/auth/register",
        json={"email": "login@example.com", "password": "loginpassword"}
    )
    response = client.post(
        "/auth/login",
        data={"username": "login@example.com", "password": "loginpassword"}
    )
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert response.json()["token_type"] == "bearer"

def test_login_user_incorrect_password(client: TestClient):
    """
    Test login with incorrect password.
    [Spec]: User Story: User Authentication / Acceptance Criteria 2
    """
    client.post(
        "/auth/register",
        json={"email": "wrongpass@example.com", "password": "correctpassword"}
    )
    response = client.post(
        "/auth/login",
        data={"username": "wrongpass@example.com", "password": "incorrectpassword"}
    )
    assert response.status_code == 401
    assert response.json()["detail"] == "Incorrect username or password"

def test_login_user_non_existent(client: TestClient):
    """
    Test login for a non-existent user.
    [Spec]: User Story: User Authentication / Acceptance Criteria 2
    """
    response = client.post(
        "/auth/login",
        data={"username": "nonexistent@example.com", "password": "anypassword"}
    )
    assert response.status_code == 401
    assert response.json()["detail"] == "Incorrect username or password"
