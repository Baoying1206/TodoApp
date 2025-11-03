from http.client import responses

from .utils import *
from ..routers.Users import get_current_user, get_db
from fastapi import status

app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user

def test_return_user(test_user):
    response = client.get("/users/user")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["username"] == "testuser1"
    assert response.json()["email"] == "testuser1@test.com"
    assert response.json()["first_name"] == "test1"
    assert response.json()["last_name"] == "user1"
    assert response.json()["role"] == "admin"
    assert response.json()["is_active"] == True
    assert response.json()["phone_number"] == "123456"

def test_user_change_password(test_user):
    response = client.put("/users/user/change_password", json={"password": "testpassword",
                                                          "new_password": "newpassword"})
    assert response.status_code == status.HTTP_204_NO_CONTENT

def test_user_change_password_invalid(test_user):
    response = client.put("/users/user/change_password", json={"password": "wrongpassword",
                                                               "new_password": "newpassword"})
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response.json()["detail"] == "Error on password"

def test_user_change_phone_number_success(test_user):
    response = client.put("/users/user/update-phone-number", params={"new_phone_number": "135123"})
    assert response.status_code == status.HTTP_202_ACCEPTED
    db = TestingSessionLocal()
    model = db.query(User).filter(User.id == test_user.id).first()
    assert model.phone_number == "135123"