import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_sheep_by_id():
    response = client.get("/sheep/1")
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "name": "Spice",
        "breed": "Gotland",
        "sex": "Female"
    }

def test_add_sheep():
    # TODO: Prepare the new sheep data in a dictionary format.
    sheep_data = {
        "id": 2,
        "name": "Fluffy",
        "breed": "Suffolk",
        "sex": "Female"
    }
    
    # TODO: Send a POST request to the endpoint "/sheep" with the new sheep data.
    # Arguments should be your endpoint and new sheep data.
    response = client.post("/sheep", json=sheep_data)
    
    # TODO: Assert that the response status code is 201 (Created)
    assert response.status_code == 201
    
    # TODO: Assert that the response JSON matches the new sheep data
    assert response.json() == sheep_data
    
    # TODO: Verify that the sheep was actually added to the database by retrieving the new sheep by ID.
    # include an assert statement to see if the new sheep data can be retrieved.
    get_response = client.get("/sheep/2")
    assert get_response.status_code == 200
    assert get_response.json() == sheep_data

def test_update_sheep():
    sheep_data = {
        "id": 2,
        "name": "Daisy Updated",
        "breed": "Suffolk",
        "sex": "Female"
    }
    response = client.put("/sheep/2", json=sheep_data)
    assert response.status_code == 200
    assert response.json() == sheep_data

def test_delete_sheep():
    response = client.delete("/sheep/2")
    assert response.status_code == 204
    # Confirm deletion
    response = client.get("/sheep/2")
    assert response.status_code == 404

def test_get_all_sheep():
    # Add another sheep for testing
    sheep_data = {
        "id": 3,
        "name": "Bubbles",
        "breed": "Babydoll",
        "sex": "Male"
    }
    client.post("/sheep", json=sheep_data)
    response = client.get("/sheep")
    assert response.status_code == 200
    sheep_list = response.json()
    assert any(sheep["id"] == 1 for sheep in sheep_list)
    assert any(sheep["id"] == 3 for sheep in sheep_list) 