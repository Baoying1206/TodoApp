from fastapi import APIRouter, Depends, HTTPException, status, Path
from sqlalchemy.orm import Session
from typing import Annotated
from ..models import Todos, User
from ..database import SessionLocal
from pydantic import BaseModel, Field
from .auth import get_current_user
from passlib.context import CryptContext
router = APIRouter(prefix="/users", tags=["user"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]
bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserVerification(BaseModel):
    password: str
    new_password: str = Field(min_length=6)

@router.get("/user", status_code=status.HTTP_200_OK)
async def get_user(user: user_dependency, db: db_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication failed")
    user_info = db.query(User).filter(User.id == user.get("user_id")).first()
    if user_info is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user_info

@router.put("/user/change_password", status_code=status.HTTP_204_NO_CONTENT)
async def change_password(user_verification: UserVerification, user: user_dependency, db: db_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication failed")
    user_model = db.query(User).filter(User.id == user.get("user_id")).first()
    if not bcrypt_context.verify(user_verification.password, user_model.hashed_password):
        raise HTTPException(status_code=401, detail="Error on password")
    user_model.hashed_password = bcrypt_context.hash(user_verification.new_password)
    db.add(user_model)
    db.commit()

@router.put("/user/update-phone-number", status_code=status.HTTP_202_ACCEPTED)
async def update_phone_number(user: user_dependency, db: db_dependency, new_phone_number: str):
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication failed")
    user_model = db.query(User).filter(User.id == user.get("user_id")).first()
    if user_model is None:
        raise HTTPException(status_code=401, detail="Authentication failed")
    user_model.phone_number = new_phone_number
    db.commit()




