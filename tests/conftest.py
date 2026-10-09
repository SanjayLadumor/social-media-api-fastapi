# tests/conftest.py
import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database import Base, get_db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Import your database session setup / engine here

SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://enterprisedb:Daryldixon#22@localhost:5444/FastAPI_test"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

TestingSessionLocal = sessionmaker(autoflush=False,autocommit=False,bind=engine)

@pytest.fixture()
def session():
    print("Session Running")
    # your test database session setup
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

@pytest.fixture()
def client(session):
    def override_get_db():
        try:
            yield session
        finally:
            pass

    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)
    app.dependency_overrides.clear()

# 1. Fixture to create a test user directly in the database
@pytest.fixture
def test_user(client):
    user_data = {"email": "anothertest@gmail.com", "password": "testing"}
    res = client.post("/users/", json=user_data)
    assert res.status_code == 201
    new_user = res.json()
    new_user["password"] = user_data["password"]
    return new_user

# 2. Fixture to log in and get a JWT token
@pytest.fixture
def token(test_user, client):
    res = client.post(
        "/login",
        data={"username": test_user["email"], "password": test_user["password"]}
    )
    return res.json()["access_token"]

# 3. Fixture that returns a client with Authorization header pre-configured
@pytest.fixture
def authorized_client(client, token):
    client.headers = {
        **client.headers,
        "Authorization": f"Bearer {token}"
    }
    return client