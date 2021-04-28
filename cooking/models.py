from django.db import models
from datetime import datetime


class IngredientsModel(models.Model):
    name = models.CharField(max_length=500, unique=True)

    def __str__(self):
        return self.name


class RecipeModel(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()
    date = models.DateTimeField(default=datetime.now(), blank=True)
    ingredients = models.ManyToManyField(IngredientsModel, through='RecipeIngredientsModel')


class RecipeIngredientsModel(models.Model):
    ingredients = models.ForeignKey(IngredientsModel, on_delete=models.CASCADE)
    recipe = models.ForeignKey(RecipeModel, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()





