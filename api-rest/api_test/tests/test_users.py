import requests
from config.settings import BASE_URL

def test_get_users():
    response = requests.get(f"{BASE_URL}/users")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 0

def test_get_user_not_found():
    response = requests.get(f"{BASE_URL}/users/999")
    assert response.status_code == 404
    data = response.json()
    assert data["detail"] == "Usuario no existe"