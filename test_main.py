from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_listing():
    # First, create a user for authentication purposes (if not already created)
    # You may need to adjust this part based on your user creation logic
    with TestClient(app) as test_client:
        token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0YWthbUBnbWFpbC5jb20iLCJleHAiOjE2OTUxOTkxMjV9.77jPhzK9JFBRqs72XU1_W0DRjIPCa1KvagY842ByL5I"
        response = test_client.post("/listing", json={"type": "HOUSE", "avalibalieNow": True, "address":"tabriz meshkinshahr"}, headers={"Authorization": f"Bearer {token}"})
        assert response.status_code == 200

def test_get_listing_by_id():
    # Assuming there is a listing with ID 1 in your database
    response = client.get("/listing/2")
    assert response.status_code == 200
    listing = response.json()
    assert "address" in listing
    assert "avalibalieNow" in listing
    assert "type" in listing





def test_update_listing_by_id():
    # First, authenticate a user and create a listing (similar to the create_listing test)
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0YWthbUBnbWFpbC5jb20iLCJleHAiOjE2OTUxOTkxMjV9.77jPhzK9JFBRqs72XU1_W0DRjIPCa1KvagY842ByL5I"
    updated_data = {"address": "456 Elm St."}
    response = client.put("/listing", json=updated_data, headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    updated_listing = response.json()
    assert updated_listing["address"] == updated_data["address"]



def test_delete_by_id():
    # Assuming there is a listing with ID 1 in your database
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0YWthbUBnbWFpbC5jb20iLCJleHAiOjE2OTUxOTkxMjV9.77jPhzK9JFBRqs72XU1_W0DRjIPCa1KvagY842ByL5I"
    response = client.delete("/listing", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200