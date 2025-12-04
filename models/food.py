

from sqlalchemy import Column, Integer, String, DateTime, Numeric, func
from sqlalchemy.orm import relationship
from . import Base

class Food(Base):
    __tablename__ = "foods"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    calories = Column(Numeric(8,2), default=0)
    protein = Column(Numeric(8,2), default=0)
    carbs = Column(Numeric(8,2), default=0)
    fat = Column(Numeric(8,2), default=0)
    created_at = Column(DateTime, server_default=func.now())

    
    meal_foods = relationship("UserMealFood", back_populates="food")

    def __repr__(self):
        return f"<Food {self.name}>"
