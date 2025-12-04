
from sqlalchemy import Column, Integer, String, Date, DateTime, func, ForeignKey
from sqlalchemy.orm import relationship
from . import Base

class Meal(Base):
    __tablename__ = "meals"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    name = Column(String(100), nullable=False)
    date = Column(Date, nullable=False)
    created_at = Column(DateTime, server_default=func.now())

   
    user = relationship("User", back_populates="meals")
    meal_foods = relationship("UserMealFood", back_populates="meal")

    def __repr__(self):
        return f"<Meal {self.name} - {self.date}>"
