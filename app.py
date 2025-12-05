from models import Base, engine, Session, User, Food, Meal, UserMealFood
from datetime import datetime


# print("Creating database tables...")
# Base.metadata.create_all(engine)
# print("Database ready!")


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def get_date(prompt):
    while True:
        date_str = input(prompt)
        try:
            return datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            print("Date must be in YYYY-MM-DD format.")


def menu():
    while True:
        print("\n Nutrition Tracker ")
        print("1. Add User")
        print("2. Add Food")
        print("3. Add Meal")
        print("4. Add Food to Meal")
        print("5. View Daily Summary")
        print("6. Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_user()
        elif choice == "2":
            add_food()
        elif choice == "3":
            add_meal()
        elif choice == "4":
            add_food_to_meal()
        elif choice == "5":
            view_daily_summary()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


def add_user():
    with Session() as session:
        name = input("Name: ")
        email = input("Email: ")
        user = User(name=name, email=email)
        session.add(user)
        session.commit()
        print(f"User {name} added!")

def add_food():
    with Session() as session:
        name = input("Food Name: ")
        calories = get_float("Calories: ")
        protein = get_float("Protein: ")
        carbs = get_float("Carbs: ")
        fat = get_float("Fat: ")
        food = Food(name=name, calories=calories, protein=protein, carbs=carbs, fat=fat)
        session.add(food)
        session.commit()
        print(f"Food {name} added!")

def add_meal():
    with Session() as session:
        users = session.query(User).all()
        if not users:
            print("No users found. Please add a user first.")
            return
        for u in users:
            print(f"{u.id}. {u.name}")
        user_id = get_int("Select user by ID: ")
        name = input("Meal name: ")
        date = get_date("Date (YYYY-MM-DD): ")
        meal = Meal(name=name, date=date, user_id=user_id)
        session.add(meal)
        session.commit()
        print(f"Meal {name} added for user {user_id}!")

def add_food_to_meal():
    with Session() as session:
        meals = session.query(Meal).all()
        if not meals:
            print("No meals found. Please add a meal first.")
            return
        for m in meals:
            print(f"{m.id}. {m.name} ({m.date})")
        meal_id = get_int("Select meal by ID: ")

        foods = session.query(Food).all()
        if not foods:
            print("No foods found. Please add food first.")
            return
        for f in foods:
            print(f"{f.id}. {f.name}")
        food_id = get_int("Select food by ID: ")

        quantity = get_float("Quantity: ")
        unit = input("Unit (default 'serving'): ") or "serving"

        
        meal = session.query(Meal).get(meal_id)

        meal_food = UserMealFood(
            meal_id=meal_id,
            food_id=food_id,
            quantity=quantity,
            unit=unit,
            user_id=meal.user_id  
        )
        session.add(meal_food)
        session.commit()
        print("Food added to meal!")


def view_daily_summary():
    with Session() as session:
        user_id = get_int("Enter user ID to view summary: ")
        date = get_date("Enter date (YYYY-MM-DD) to view summary: ")
        
        meals = session.query(Meal).filter_by(user_id=user_id, date=date).all()
        if not meals:
            print("No meals found for this user on this date.")
            return

        print(f"\nDaily Summary for User {user_id} on {date}:")
        total_calories = total_protein = total_carbs = total_fat = 0

        for meal in meals:
            print(f"\nMeal: {meal.name}")
            meal_foods = session.query(UserMealFood).filter_by(meal_id=meal.id).all()
            for mf in meal_foods:
                food = session.query(Food).get(mf.food_id)
                cals = food.calories * mf.quantity
                prot = food.protein * mf.quantity
                carbs = food.carbs * mf.quantity
                fat = food.fat * mf.quantity
                total_calories += cals
                total_protein += prot
                total_carbs += carbs
                total_fat += fat
                print(f"  {food.name}: {mf.quantity} {mf.unit} | Calories: {cals}, Protein: {prot}, Carbs: {carbs}, Fat: {fat}")

        print("\n Total Nutrients ")
        print(f"Calories: {total_calories}")
        print(f"Protein: {total_protein}")
        print(f"Carbs: {total_carbs}")
        print(f"Fat: {total_fat}")


if __name__ == "__main__":
    menu()
