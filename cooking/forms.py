from django import forms
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
