# [Task]: T010
# [From]: speckit.plan / Phase 1: Project Setup & Monorepo Configuration
# [Spec]: speckit.specify

from fastapi.testclient import TestClient
from app.main import app

# Create a TestClient for your FastAPI application
client = TestClient(app)

def test_read_root():
    """
    Test the root endpoint to ensure the API is running.
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Full-Stack Todo API!"}