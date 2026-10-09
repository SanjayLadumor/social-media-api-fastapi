# from .test_database import client
from app.schemas import *

def test_root(client):
    res = client.get("/")
    assert res.json().get("message") == "Visit : https://social-media-api-fastapi-lc2r.onrender.com/docs"

def test_create_user(client):
    res = client.post("/users/",json={"email":"anothertest@gmail.com","password":"testing"})
    assert res.json().get("email") == "anothertest@gmail.com"
    assert res.status_code == 201

def test_get_user(client):
    res = client.get(f"/users/1")
    print(res.json())

def test_login(client, test_user):
    res = client.post(
        "/login", 
        data={
            "username": test_user["email"], 
            "password": test_user["password"]
        }
    )
    print("Logged In")
    assert res.status_code == 200
    
    # Optional bonus checks for a proper JWT login response:
    login_res = res.json()
    assert "access_token" in login_res
    assert login_res["token_type"] == "bearer"