from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
)

from .models import Recipe, Ingredient, MealPlan, MealPlanEntry


class HomePageView(TemplateView):
    template_name = "home.html"


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")


class RecipeListView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = "MealMap/recipe_list.html"
    context_object_name = "recipes"

    def get_queryset(self):
        return Recipe.objects.filter(owner=self.request.user)


class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = "MealMap/recipe_detail.html"
    context_object_name = "recipe"

    def get_queryset(self):
        return Recipe.objects.filter(owner=self.request.user)


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    template_name = "MealMap/recipe_form.html"
    fields = ["title", "description", "cook_time", "instructions"]
    success_url = reverse_lazy("recipe_list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class RecipeUpdateView(LoginRequiredMixin, UpdateView):
    model = Recipe
    template_name = "MealMap/recipe_form.html"
    fields = ["title", "description", "cook_time", "instructions"]
    success_url = reverse_lazy("recipe_list")

    def get_queryset(self):
        return Recipe.objects.filter(owner=self.request.user)


class RecipeDeleteView(LoginRequiredMixin, DeleteView):
    model = Recipe
    template_name = "MealMap/recipe_confirm_delete.html"
    success_url = reverse_lazy("recipe_list")

    def get_queryset(self):
        return Recipe.objects.filter(owner=self.request.user)
    
class RecipeListView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = "MealMap/recipe_list.html"
    context_object_name = "recipes"

    def get_queryset(self):
        return Recipe.objects.filter(owner=self.request.user)
    
class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = "MealMap/recipe_detail.html"
    context_object_name = "recipe"

    def get_queryset(self):
        return Recipe.objects.filter(owner=self.request.user)
    
class IngredientCreateView(LoginRequiredMixin, CreateView):
    model = Ingredient
    template_name = "MealMap/ingredient_form.html"
    fields = ["name", "quantity", "notes"]

    def dispatch(self, request, *args, **kwargs):
        self.recipe = get_object_or_404(Recipe, pk=self.kwargs["recipe_pk"], owner=request.user)
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.recipe = self.recipe
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["recipe"] = self.recipe
        return context

    def get_success_url(self):
        return reverse_lazy("recipe_detail", kwargs={"pk": self.recipe.pk})


class IngredientUpdateView(LoginRequiredMixin, UpdateView):
    model = Ingredient
    template_name = "MealMap/ingredient_form.html"
    fields = ["name", "quantity", "notes"]

    def get_queryset(self):
        return Ingredient.objects.filter(recipe__owner=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["recipe"] = self.object.recipe
        return context

    def get_success_url(self):
        return reverse_lazy("recipe_detail", kwargs={"pk": self.object.recipe.pk})


class IngredientDeleteView(LoginRequiredMixin, DeleteView):
    model = Ingredient
    template_name = "MealMap/ingredient_confirm_delete.html"

    def get_queryset(self):
        return Ingredient.objects.filter(recipe__owner=self.request.user)

    def get_success_url(self):
        return reverse_lazy("recipe_detail", kwargs={"pk": self.object.recipe.pk})
    
class MealPlanListView(LoginRequiredMixin, ListView):
    model = MealPlan
    template_name = "MealMap/mealplan_list.html"
    context_object_name = "mealplans"

    def get_queryset(self):
        return MealPlan.objects.filter(owner=self.request.user)


class MealPlanDetailView(LoginRequiredMixin, DetailView):
    model = MealPlan
    template_name = "MealMap/mealplan_detail.html"
    context_object_name = "mealplan"

    def get_queryset(self):
        return MealPlan.objects.filter(owner=self.request.user)


class MealPlanCreateView(LoginRequiredMixin, CreateView):
    model = MealPlan
    template_name = "MealMap/mealplan_form.html"
    fields = ["title", "week_start"]
    success_url = reverse_lazy("mealplan_list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class MealPlanUpdateView(LoginRequiredMixin, UpdateView):
    model = MealPlan
    template_name = "MealMap/mealplan_form.html"
    fields = ["title", "week_start"]
    success_url = reverse_lazy("mealplan_list")

    def get_queryset(self):
        return MealPlan.objects.filter(owner=self.request.user)


class MealPlanDeleteView(LoginRequiredMixin, DeleteView):
    model = MealPlan
    template_name = "MealMap/mealplan_confirm_delete.html"
    success_url = reverse_lazy("mealplan_list")

    def get_queryset(self):
        return MealPlan.objects.filter(owner=self.request.user)
    
class MealPlanEntryCreateView(LoginRequiredMixin, CreateView):
    model = MealPlanEntry
    template_name = "MealMap/mealplanentry_form.html"
    fields = ["recipe", "day_of_week", "meal_type"]

    def dispatch(self, request, *args, **kwargs):
        self.mealplan = get_object_or_404(
            MealPlan,
            pk=self.kwargs["mealplan_pk"],
            owner=request.user,
        )
        return super().dispatch(request, *args, **kwargs)

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["recipe"].queryset = Recipe.objects.filter(owner=self.request.user)
        return form

    def form_valid(self, form):
        form.instance.meal_plan = self.mealplan
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["mealplan"] = self.mealplan
        return context

    def get_success_url(self):
        return reverse_lazy("mealplan_detail", kwargs={"pk": self.mealplan.pk})


class MealPlanEntryUpdateView(LoginRequiredMixin, UpdateView):
    model = MealPlanEntry
    template_name = "MealMap/mealplanentry_form.html"
    fields = ["recipe", "day_of_week", "meal_type"]

    def get_queryset(self):
        return MealPlanEntry.objects.filter(meal_plan__owner=self.request.user)

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["recipe"].queryset = Recipe.objects.filter(owner=self.request.user)
        return form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["mealplan"] = self.object.meal_plan
        return context

    def get_success_url(self):
        return reverse_lazy("mealplan_detail", kwargs={"pk": self.object.meal_plan.pk})


class MealPlanEntryDeleteView(LoginRequiredMixin, DeleteView):
    model = MealPlanEntry
    template_name = "MealMap/mealplanentry_confirm_delete.html"

    def get_queryset(self):
        return MealPlanEntry.objects.filter(meal_plan__owner=self.request.user)

    def get_success_url(self):
        return reverse_lazy("mealplan_detail", kwargs={"pk": self.object.meal_plan.pk})
    
