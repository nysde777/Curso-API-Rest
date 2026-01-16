import requests

import response

base_url = "http://localhost:8000/users"

def test_get_users():
    response = requests.get(base_url)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 0