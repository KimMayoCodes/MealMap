from django.contrib import admin
from .models import (
    Recipe,
    Ingredient,
    MealPlan,
    MealPlanEntry, 
    PantryItem
    )


class IngredientInline(admin.TabularInline):
    model = Ingredient
    extra = 1


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", "cook_time", "created_at")
    search_fields = ("title", "description", "owner__username")
    list_filter = ("created_at",)
    ordering = ("title",)
    inlines = [IngredientInline]


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ("name", "recipe", "quantity")
    search_fields = ("name", "recipe__title")
    list_filter = ("recipe",)
    ordering = ("name",)


@admin.register(MealPlan)
class MealPlanAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", "week_start", "created_at")
    search_fields = ("title", "owner__username")
    list_filter = ("week_start", "created_at")
    ordering = ("-week_start",)


@admin.register(MealPlanEntry)
class MealPlanEntryAdmin(admin.ModelAdmin):
    list_display = ("meal_plan", "recipe", "day_of_week", "meal_type")
    search_fields = ("meal_plan__title", "recipe__title")
    list_filter = ("day_of_week", "meal_type")
    ordering = ("day_of_week", "meal_type")

@admin.register(PantryItem)
class PantryItemAdmin(admin.ModelAdmin):
    list_display = ("name", "owner", "quantity", "created_at")
    search_fields = ("name", "owner__username")
    list_filter = ("created_at",)
    ordering = ("name",)
