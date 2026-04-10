from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
)

from .models import Recipe


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