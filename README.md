# MealMap

MealMap is a Django web application designed for home cooks and busy individuals who want one place to store favorite recipes, organize ingredients, and plan meals for the week.

## Features
- Create, view, update, and delete recipes
- Add ingredients to recipes
- Create weekly meal plans
- Assign recipes to specific days/meals
- User authentication and private data ownership
- Django admin customization for data management

## Tech Stack
- Python
- Django
- SQLite (development)
- Bootstrap 5

## Installation
1. Clone the repository
2. Create and activate a virtual environment
3. Install dependencies:
   pip install -r requirements.txt
4. Run migrations:
   python manage.py migrate
5. Create superuser:
   python manage.py createsuperuser
6. Start server:
   python manage.py runserver

## Project Purpose
Many people enjoy cooking at home but struggle to keep recipes organized and turn them into a realistic weekly meal plan. MealMap helps users reduce last-minute decision-making and keep meal planning simple and practical.

## Future Enhancements
- Pantry tracking
- Ingredient-based recipe suggestions
- Grocery list generation