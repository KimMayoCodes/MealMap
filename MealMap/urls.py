from django.urls import path
from .views import (
    HomePageView,
    RecipeCreateView,
    RecipeDeleteView,
    RecipeDetailView,
    RecipeListView,
    RecipeUpdateView,
    SignUpView,
)

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("recipes/", RecipeListView.as_view(), name="recipe_list"),
    path("recipes/new/", RecipeCreateView.as_view(), name="recipe_create"),
    path("recipes/<int:pk>/", RecipeDetailView.as_view(), name="recipe_detail"),
    path("recipes/<int:pk>/edit/", RecipeUpdateView.as_view(), name="recipe_update"),
    path("recipes/<int:pk>/delete/", RecipeDeleteView.as_view(), name="recipe_delete"),
]