import pytest
from fastapi.testclient import TestClient
from app.main import app
client = TestClient(app)
def test_healthz():
    res = client.get("/healthz")
    assert res.status_code == 200
    assert "status" in res.json()
