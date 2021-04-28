from django import forms
from .models import *


class IngredientForm(forms.ModelForm):
    class Meta:
        model = IngredientsModel
        fields = [
            'name',
        ]

