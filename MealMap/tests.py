from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Recipe, Ingredient, MealPlan, PantryItem


User = get_user_model()


class MealMapTestCase(TestCase):

    def setUp(self):
        # Create users
        self.user1 = User.objects.create_user(username="user1", password="pass1234")
        self.user2 = User.objects.create_user(username="user2", password="pass1234")

        # Create recipe for user1
        self.recipe = Recipe.objects.create(
            owner=self.user1,
            title="Test Recipe",
            description="Test description",
            cook_time=30,
            instructions="Test instructions"
        )

        # Add ingredient
        self.ingredient = Ingredient.objects.create(
            recipe=self.recipe,
            name="Eggs",
            quantity="2"
        )

        # Create pantry item
        self.pantry_item = PantryItem.objects.create(
            owner=self.user1,
            name="Eggs",
            quantity="6"
        )

    # -------------------------
    # AUTH TEST
    # -------------------------
    def test_login_required_redirect(self):
        response = self.client.get(reverse("recipe_list"))
        self.assertEqual(response.status_code, 302)  # redirect to login

    # -------------------------
    # RECIPE TESTS
    # -------------------------
    def test_recipe_list_user_only(self):
        self.client.login(username="user1", password="pass1234")
        response = self.client.get(reverse("recipe_list"))
        self.assertContains(response, "Test Recipe")

    def test_recipe_not_visible_to_other_user(self):
        self.client.login(username="user2", password="pass1234")
        response = self.client.get(reverse("recipe_list"))
        self.assertNotContains(response, "Test Recipe")

    # -------------------------
    # PANTRY TESTS
    # -------------------------
    def test_pantry_item_created(self):
        self.assertEqual(PantryItem.objects.count(), 1)
        self.assertEqual(self.pantry_item.name, "Eggs")

    def test_pantry_list_view(self):
        self.client.login(username="user1", password="pass1234")
        response = self.client.get(reverse("pantry_list"))
        self.assertContains(response, "Eggs")

    # -------------------------
    # MEAL PLAN TESTS
    # -------------------------
    def test_mealplan_create(self):
        self.client.login(username="user1", password="pass1234")
        response = self.client.post(reverse("mealplan_create"), {
            "title": "Weekly Plan",
            "week_start": "2026-04-13"
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(MealPlan.objects.count(), 1)

    # -------------------------
    # SUGGESTION LOGIC TEST
    # -------------------------
    def test_recipe_suggestion_basic_match(self):
        self.client.login(username="user1", password="pass1234")
        response = self.client.get(reverse("suggested_recipes"))
        self.assertContains(response, "Test Recipe")

    def test_recipe_suggestion_no_match(self):
        # remove pantry item so nothing matches
        PantryItem.objects.all().delete()

        self.client.login(username="user1", password="pass1234")
        response = self.client.get(reverse("suggested_recipes"))

        self.assertContains(response, "Your pantry is empty")

    # -------------------------
    # SECURITY TEST
    # -------------------------
    def test_user_cannot_access_other_recipe(self):
        self.client.login(username="user2", password="pass1234")
        response = self.client.get(reverse("recipe_detail", args=[self.recipe.pk]))
        self.assertEqual(response.status_code, 404)