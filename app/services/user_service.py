from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate
from passlib.hash import bcrypt

def create_user(db: Session, user: UserCreate):
    hashed_password = bcrypt.hash(user.password)
    db_user = User(**user.model_dump())
    # db_user = User(user.username, user.email, hashed_password) # hashing pswds
    db.add(db_user)
    db.commit()
    return db_user