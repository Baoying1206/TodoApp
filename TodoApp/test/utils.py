from sqlalchemy import create_engine, text
from sqlalchemy.pool import StaticPool
from sqlalchemy.orm import sessionmaker
from ..database import Base
from ..main import app
from fastapi.testclient import TestClient
import pytest
from ..models import Todos, User
from ..routers.auth import bcrypt_context

SQLALCHEMY_DATABASE_URI = "sqlite:///./testdb.db"
engine = create_engine(SQLALCHEMY_DATABASE_URI,
                       connect_args={"check_same_thread": False},
                       poolclass=StaticPool)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

def override_get_current_user():
    return {'username': 'bao', 'user_id': '1', 'user_role': 'admin'}

client = TestClient(app)

@pytest.fixture
def test_todo():
    todo = Todos(
        title="learing to code",
        description="everyday",
        priority=5,
        completed=False,
        owner_id=1,
    )
    db = TestingSessionLocal()
    db.add(todo)
    db.commit()
    yield todo
    with engine.connect() as connection:
        connection.execute(text("delete from todos"))
        connection.commit()

@pytest.fixture
def test_user():
    user = User(
        email="testuser1@test.com",
        username = "testuser1",
        first_name = "test1",
        last_name = "user1",
        hashed_password = bcrypt_context.hash("testpassword"),
        is_active = True,
        role = "admin",
        phone_number = 123456
    )
    db = TestingSessionLocal()
    db.add(user)
    db.commit()
    yield user
    with engine.connect() as connection:
        connection.execute(text("delete from users"))
        connection.commit()