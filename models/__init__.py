from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()

from .user import User
from .food import Food
from .meal import Meal
from .user_meal_food import UserMealFood
from .daily_summary import DailySummary



engine = create_engine("sqlite:///./db/nutrition.db")
Session = sessionmaker(bind=engine)
session = Session()



