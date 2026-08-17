from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_drug_not_found():
    response = client.get("/drugs/asdfghjklxyz123")

    assert response.status_code == 404
    assert response.json() == {"detail": "Drug not found"}

def test_drug_found():
    response = client.get("/drugs/Tylenol")

    assert response.status_code == 200

    data = response.json()

    assert data["drug_name"] == "TYLENOL Extra Strength"