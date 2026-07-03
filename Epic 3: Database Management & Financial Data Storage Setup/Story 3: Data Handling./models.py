from sqlalchemy import Column, Integer, String, Float
from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    email = Column(String, unique=True)
    password = Column(String)

    monthly_income = Column(Float)
    monthly_expenses = Column(Float)
