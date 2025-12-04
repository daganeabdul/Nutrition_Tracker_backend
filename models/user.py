
from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import relationship
from . import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    created_at = Column(DateTime, server_default=func.now())


    meals = relationship("Meal", back_populates="user")
    meal_foods = relationship("UserMealFood", back_populates="user")

    def __repr__(self):
        return f"<User {self.name}>"
