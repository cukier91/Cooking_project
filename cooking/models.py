from django.db import models
from django.utils import timezone
from django.utils.timezone import now
from multiselectfield import MultiSelectField


class IngredientsModel(models.Model):
    name = models.CharField(max_length=500, unique=True)
    energy = models.FloatField(null=True, blank=True,)
    fat = models.FloatField(null=True, blank=True)
    carbohydrates = models.FloatField(null=True, blank=True)
    fiber = models.FloatField(null=True, blank=True)
    protein = models.FloatField(null=True, blank=True)
    salt = models.FloatField(null=True, blank=True)
    sugar = models.FloatField(null=True, blank=True)

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
    ('Lunch', 'Lunch'),
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


class MenuPlanModel(models.Model):
    name = models.CharField(max_length=300, null=False)
    date = models.DateTimeField(default=now, blank=False)
    recipe = models.ManyToManyField(RecipeModel, through='MenuRecipeModel')


class Meal(models.TextChoices):
    breakfast = 'Śniadanie', 'Śniadanie'
    second_breakfast = 'Drugie śniadanie', 'Drugie śniadanie'
    lunch = 'Lunch do pracy', 'Lunch do pracy'
    dinner = 'Obiad', 'Obiad'
    supper = 'Kolacja', 'Kolacja'


class Day(models.TextChoices):
    monday = 'Poniedziałek', 'Poniedziałek'
    tuesday = 'Wtorek', 'Wtorek'
    wednesday = 'Środa', 'Środa'
    thursday = 'Czwartek', 'Czwartek'
    friday = 'Piątek', 'Piątek'
    saturday = 'Sobota', 'Sobota'
    sunday = 'Niedziela', 'Niedziela'


class MenuRecipeModel(models.Model):
    recipe = models.ForeignKey(RecipeModel, on_delete=models.CASCADE)
    menu = models.ForeignKey(MenuPlanModel, on_delete=models.CASCADE)
    day_name = models.CharField(max_length=50, choices=Day.choices, null=False)
    meal_name = models.CharField(max_length=50, choices=Meal.choices, null=False)


