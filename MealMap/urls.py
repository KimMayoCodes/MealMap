from django.urls import path
from .views import (
    HomePageView,
    IngredientCreateView,
    IngredientDeleteView,
    IngredientUpdateView,
    MealPlanCreateView,
    MealPlanDeleteView,
    MealPlanDetailView,
    MealPlanListView,
    MealPlanUpdateView,
    MealPlanEntryCreateView,
    MealPlanEntryDeleteView,
    MealPlanEntryUpdateView,
    RecipeCreateView,
    RecipeDeleteView,
    RecipeDetailView,
    RecipeListView,
    RecipeUpdateView,
    SignUpView,
    PantryItemCreateView,
    PantryItemDeleteView,
    PantryItemListView,
    PantryItemUpdateView,
    SuggestedRecipeListView
)

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("signup/", SignUpView.as_view(), name="signup"),

    path("recipes/", RecipeListView.as_view(), name="recipe_list"),
    path("recipes/new/", RecipeCreateView.as_view(), name="recipe_create"),
    path("recipes/<int:pk>/", RecipeDetailView.as_view(), name="recipe_detail"),
    path("recipes/<int:pk>/edit/", RecipeUpdateView.as_view(), name="recipe_update"),
    path("recipes/<int:pk>/delete/", RecipeDeleteView.as_view(), name="recipe_delete"),

    path("recipes/<int:recipe_pk>/ingredients/new/", IngredientCreateView.as_view(), name="ingredient_create"),
    path("ingredients/<int:pk>/edit/", IngredientUpdateView.as_view(), name="ingredient_update"),
    path("ingredients/<int:pk>/delete/", IngredientDeleteView.as_view(), name="ingredient_delete"),

    path("mealplans/", MealPlanListView.as_view(), name="mealplan_list"),
    path("mealplans/new/", MealPlanCreateView.as_view(), name="mealplan_create"),
    path("mealplans/<int:pk>/", MealPlanDetailView.as_view(), name="mealplan_detail"),
    path("mealplans/<int:pk>/edit/", MealPlanUpdateView.as_view(), name="mealplan_update"),
    path("mealplans/<int:pk>/delete/", MealPlanDeleteView.as_view(), name="mealplan_delete"),

    path(
        "mealplans/<int:mealplan_pk>/entries/new/",
        MealPlanEntryCreateView.as_view(),
        name="mealplanentry_create",
    ),
    path(
        "entries/<int:pk>/edit/",
        MealPlanEntryUpdateView.as_view(),
        name="mealplanentry_update",
    ),
    path(
        "entries/<int:pk>/delete/",
        MealPlanEntryDeleteView.as_view(),
        name="mealplanentry_delete",
    ),
    path("pantry/", PantryItemListView.as_view(), name="pantry_list"),
    path("pantry/new/", PantryItemCreateView.as_view(), name="pantry_create"),
    path("pantry/<int:pk>/edit/", PantryItemUpdateView.as_view(), name="pantry_update"),
    path("pantry/<int:pk>/delete/", PantryItemDeleteView.as_view(), name="pantry_delete"),
    path("suggestions/", SuggestedRecipeListView.as_view(), name="suggested_recipes"),
]