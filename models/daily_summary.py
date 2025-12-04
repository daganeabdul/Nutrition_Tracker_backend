

from sqlalchemy import Column, Integer, Numeric, Date, DateTime, func, ForeignKey
from sqlalchemy.orm import relationship
from . import Base

class DailySummary(Base):
    __tablename__ = "daily_summaries"

    id = Column(Integer, primary_key=True)
    mealfood_id = Column(Integer, ForeignKey("user_meal_foods.id"), nullable=False)
    date = Column(Date, nullable=False)
    total_calories = Column(Numeric(10,2), default=0)
    total_protein = Column(Numeric(10,2), default=0)
    total_carbs = Column(Numeric(10,2), default=0)
    total_fat = Column(Numeric(10,2), default=0)
    created_at = Column(DateTime, server_default=func.now())

    mealfood = relationship("UserMealFood", back_populates="summary")

    def __repr__(self):
        return f"<DailySummary {self.date}>"
