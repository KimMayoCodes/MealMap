from django.conf import settings
from django.db import models


class Recipe(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="recipes",
    )
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    cook_time = models.PositiveIntegerField(help_text="Cook time in minutes")
    instructions = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title
    
class Ingredient(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name="ingredients",
    )
    name = models.CharField(max_length=100)
    quantity = models.CharField(max_length=50)
    notes = models.CharField(max_length=200, blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.quantity} {self.name}"