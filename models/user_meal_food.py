
from sqlalchemy import Column, Integer, Numeric, String, DateTime, func, ForeignKey
from sqlalchemy.orm import relationship
from . import Base

class UserMealFood(Base):
    __tablename__ = "user_meal_foods"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    meal_id = Column(Integer, ForeignKey("meals.id"), nullable=False)
    food_id = Column(Integer, ForeignKey("foods.id"), nullable=False)
    quantity = Column(Numeric(10,2), default=1)
    unit = Column(String(50), default="serving")
    created_at = Column(DateTime, server_default=func.now())

   
    user = relationship("User", back_populates="meal_foods")
    meal = relationship("Meal", back_populates="meal_foods")
    food = relationship("Food", back_populates="meal_foods")
    summary = relationship("DailySummary", back_populates="mealfood", uselist=False)

    def __repr__(self):
        return f"<UserMealFood user={self.user_id}, food={self.food_id}>"
