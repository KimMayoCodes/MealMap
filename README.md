# 🍽️ MealMap

MealMap is a Django web application designed for home cooks and busy individuals who want a centralized place to store recipes, organize ingredients, and plan meals for the week.

## 🚀 Features
- Full CRUD functionality for recipes (create, view, update, delete)
- Add and manage ingredients for each recipe
- Create and manage weekly meal plans
- Assign recipes to specific days and meals
- User authentication with private data ownership
- Customized Django admin interface for efficient data management

## 🛠️ Tech Stack
- Python
- Django
- SQLite (development)
- Bootstrap 5

## ⚙️ Installation
1. Clone the repository  
2. Create and activate a virtual environment  
3. Install dependencies:  
   ```bash
   pip install -r requirements.txt
4. Run migrations:
   ```bash
   python manage.py migrate
5. Create a superuser:
   ```bash
   python manage.py createsuperuser
6. Start the development server:
   ```bash
   python manage.py runserver
