from fastapi.testclient import TestClient
from app.main import app
import pytest
from app.schemas import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app.database import get_db
from app.database import Base

# client = TestClient(app)

SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://enterprisedb:Daryldixon#22@localhost:5444/FastAPI_test"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

TestingSessionLocal = sessionmaker(autoflush=False,autocommit=False,bind=engine)

@pytest.fixture
def session():
    # Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

@pytest.fixture
def client(session):
    def override_get_db():
        try:
            yield session
        finally:
            session.close()
    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)