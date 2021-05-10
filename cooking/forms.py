from django import forms
from django.views.generic import FormView

from .models import *


class IngredientForm(forms.ModelForm):
    class Meta:
        model = IngredientsModel
        fields = [
            'name',
        ]


class RecipeForm(forms.ModelForm):
    class Meta:
        model = RecipeModel
        fields = '__all__'
        exclude = ['date', 'ingredients']
        widgets = {
            'mealtype': forms.CheckboxSelectMultiple
        }


class RecipeIngredientForm(forms.ModelForm):
    class Meta:
        model = RecipeIngredientsModel
        fields = [
            'ingredients',
            'recipe',
            'amount',
            'unit'
        ]
        widgets = {
            'recipe': forms.HiddenInput,
        }


class MenuPlanForm(forms.ModelForm):
    class Meta:
        model = MenuPlanModel
        fields = [
            'name',
        ]
