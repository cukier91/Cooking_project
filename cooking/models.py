from django.db import models
from django.utils import timezone
from django.utils.timezone import now
from multiselectfield import MultiSelectField


class IngredientsModel(models.Model):
    name = models.CharField(max_length=500, unique=True)

    def __str__(self):
        return self.name


class Unit(models.TextChoices):
    mililiter = "ml", "ml"
    liter = "l", "l"
    gram = "g", "g"
    decagram = "dag", "dag"
    kilogram = "kg", "kg"
    spoon = "łyżka(i)", "łyżka(i)"
    teaspoon = "łyżeczka(i)", "łyżeczka(i)"
    quantity = "szt.", "szt."
    can = "puszka(i)", "puszka(i)"
    fruit = "ząbek(ki)", "ząbek(ki)"
    bar = "kostka(i)", "kostka(i)"
    glass = "szklanka(i)", "szklanka(i)"


MEAL_CHOICE = (
    ('Śniadanie', 'Śniadanie'),
    ('Drugie śniadanie', 'Drugie śniadanie'),
    ('Lunch do pracy', 'Lunch do pracy'),
    ('Obiad', 'Obiad'),
    ('Kolacja', 'Kolacja')
)


class RecipeModel(models.Model):
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=1000)
    preparation = models.TextField(null=True)
    mealtype = MultiSelectField(choices=MEAL_CHOICE, max_choices=2, null=True, max_length=500)
    date = models.DateTimeField(default=now, blank=True)
    ingredients = models.ManyToManyField(IngredientsModel, through='RecipeIngredientsModel')


class RecipeIngredientsModel(models.Model):
    ingredients = models.ForeignKey(IngredientsModel, on_delete=models.CASCADE)
    recipe = models.ForeignKey(RecipeModel, on_delete=models.CASCADE)
    amount = models.DecimalField(null=True, default=0, max_digits=300, decimal_places=1)
    unit = models.CharField(max_length=50, choices=Unit.choices, null=True)
