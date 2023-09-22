from fastapi.testclient import TestClient
from main import app
from fastapi import FastAPI
from sqlalchemy.orm import Session
from .router import listing_app  # Replace with your FastAPI app instance
from databse.connection import get_db
from databse.models import User
from .schema.request import ListingIn, ListingCh

client = TestClient(listing_app)


def test_get_listing_by_id():
    response = client.get("/listing/")
    assert response.status_code == 200


def test_update_listing_by_id():
    # First, authenticate a user and create a listing (similar to the create_listing test)
    # ...
    # Update the listing
    updated_data = {"type": "House", "availableNow": False, "address": "456 Elm St."}
    response = client.put("/listing", json=updated_data, headers={"Authorization": f"Bearer {access_token}"})
    assert response.status_code == 200
    updated_listing = response.json()

    # Check if the updated listing matches the new data
    assert updated_listing["type"] == updated_data["type"]
    assert updated_listing["availableNow"] == updated_data["availableNow"]
    assert updated_listing["address"] == updated_data["address"]