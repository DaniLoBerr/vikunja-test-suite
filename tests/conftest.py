import httpx
import pytest


base_url = "http://localhost:8080/api/v1"


@pytest.fixture
def client():
    with httpx.Client(base_url=base_url) as client:
        yield client


@pytest.fixture
def token(client):
    data = {"username": "testuser", "password": "testpassword123"}
    response = client.post("/login", json=data)
    return response.json()["token"]
