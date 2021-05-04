from django.db import models
from django.utils import timezone
from django.utils.timezone import now
from multiselectfield import MultiSelectField


class IngredientsModel(models.Model):
    name = models.CharField(max_length=500, unique=True)

    def __str__(self):
        return self.name


class Unit(models.TextChoices):
    mililiter = "ML", "ml"
    liter = "L", "l"
    gram = "G", "g"
    decagram = "KO", "dag"
    kilogram = "KG", "kg"
    spoon = "Ł", "łyżka"
    spoons = "ŁY", "łyżki"
    teaspoon = "ł", "łyżeczka"
    teaspoons = "ły", "łyżeczki"
    quantity = "SZT", "szt"


MEAL_CHOICE = (
    (1, 'Śniadanie'),
    (2, 'Drugie śniadanie'),
    (3, 'Lunch do pracy'),
    (4, 'Obiad'),
    (5, 'Kolacja')
)


class RecipeModel(models.Model):
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=1000)
    preparation = models.TextField(null=True)
    mealtype = MultiSelectField(choices=MEAL_CHOICE, max_choices=2, null=True)
    date = models.DateTimeField(default=now, blank=True)
    ingredients = models.ManyToManyField(IngredientsModel, through='RecipeIngredientsModel')


class RecipeIngredientsModel(models.Model):
    ingredients = models.ForeignKey(IngredientsModel, on_delete=models.CASCADE)
    recipe = models.ForeignKey(RecipeModel, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(null=True, default=0)
    unit = models.CharField(max_length=50, choices=Unit.choices, null=True)
