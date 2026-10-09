from app.schemas import *

def test_get_posts(authorized_client):
    res = authorized_client.get("/posts/")
    print(res.json())
    assert res.status_code == 200

def test_create_post(authorized_client):
    res = authorized_client.post("/posts/", json={"title": "Test Title", "content": "Test Content"})
    print(res.json())
    assert res.status_code == 201

# You can still test unauthorized access using plain client
def test_get_all_posts_unauthorized(client):
    res = client.get("/posts/")
    print(res.json())
    assert res.status_code == 401  # or your route's unauthenticated code