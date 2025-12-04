Developed : Abdirahman Dagane
# Nutrition Tracker Backend

A simple **Python CLI application** to track users’ meals, foods, and daily nutrition. Built with **SQLAlchemy ORM** and **SQLite**, this project allows you to add users, foods, meals, associate foods with meals, and view daily nutrition summaries.



## Features

* Add users with name and email.
* Add foods with nutritional information: calories, protein, carbs, and fat.
* Create meals for users with a specific date.
* Add foods to meals with quantity and unit (e.g., serving, grams).
* View a daily summary of calories, protein, carbs, and fat for each user.
* Fully interactive command-line interface (CLI).



## Technologies Used

* Python 3.x
* SQLAlchemy ORM
* SQLite (local database)
* Pipenv (virtual environment & dependency management)


## Project Structure

```
Nutrition_Tracker_backend/
│
├── app.py                 # Main CLI application
├── models/                # SQLAlchemy models
│   ├── __init__.py
│   ├── user.py
│   ├── food.py
│   ├── meal.py
│   └── user_meal_food.py
├── db/                    # Database folder (ignored in git)
│   └── nutrition.db
├── .venv/                 # Virtual environment (ignored in git)
├── Pipfile
├── Pipfile.lock
└── README.md
```

---

## Installation

1. **Clone the repository**

```bash
git clone git@github.com:daganeabdul/Nutrition_Tracker_backend.git
cd Nutrition_Tracker_backend
```

2. **Activate the virtual environment**

```bash
pipenv shell
```

3. **Install dependencies**

```bash
pipenv install
```

4. **Run the application**

```bash
python app.py
```

---

## Usage

When you run the app, you'll see a menu like this:

```
=== Nutrition Tracker ===
1. Add User
2. Add Food
3. Add Meal
4. Add Food to Meal
5. View Daily Summary
6. Exit
Choose:
```

* **Add User:** Enter user’s name and email.
* **Add Food:** Enter food name and nutritional values.
* **Add Meal:** Choose a user, name the meal, and set a date.
* **Add Food to Meal:** Select a meal, select a food, and specify quantity and unit.
* **View Daily Summary:** Enter a user and date to view their total nutrition for that day.

**Example Unit Input:** `"serving"`, `"grams"`, `"pieces"`.



## Database

* SQLite database is stored in `db/nutrition.db`.
* Tables:

  * `users`
  * `foods`
  * `meals`
  * `user_meal_foods`
  * `daily_summaries` (optional for future reporting)

> The database file is ignored in `.gitignore` to avoid committing sensitive data.



## Contributing

1. Fork the repository
2. Create a new branch: `git checkout -b feature-name`
3. Make your changes
4. Commit your changes: `git commit -m "Add feature"`
5. Push to your branch: `git push origin feature-name`
6. Open a pull request




MIT License

Copyright (c) 2025 daganeabdul

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


