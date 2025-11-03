from ..main import app
from fastapi import status
from fastapi.testclient import TestClient

client = TestClient(app)
def test_healthy():
    response = client.get("/healthy")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"status": "ok"}
