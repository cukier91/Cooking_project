from django.db import models
from django.utils import timezone
from django.utils.timezone import now


class IngredientsModel(models.Model):
    name = models.CharField(max_length=500, unique=True)

    def __str__(self):
        return self.name


class RecipeModel(models.Model):
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=1000)
    preparation = models.TextField(null=True)
    date = models.DateTimeField(default=now, blank=True)
    ingredients = models.ManyToManyField(IngredientsModel, through='RecipeIngredientsModel')


class RecipeIngredientsModel(models.Model):
    ingredients = models.ForeignKey(IngredientsModel, on_delete=models.CASCADE)
    recipe = models.ForeignKey(RecipeModel, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
