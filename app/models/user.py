from sqlalchemy import Column, String, Integer
from app.database.connection import Base
from passlib.hash import bcrypt

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    email = Column(String, index=True)
    password = Column(String, index=True)
    # hashed_password = Column(String)

    # verify for user auth
    def hash_password(self, pswd):
        return bcrypt.verify(pswd, self.hashed_password)