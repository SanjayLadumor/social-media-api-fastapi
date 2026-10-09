from app.schemas import *

def test_vote(authorized_client):
    res = authorized_client.post("/vote/", json = {"post_id":1,"dir":1})
    print(res.json())