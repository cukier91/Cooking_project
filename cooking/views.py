from django.shortcuts import render, redirect
from django.views import View
from .models import *
from .forms import IngredientForm
from django.views.generic.edit import FormView


class IngredientsFormView(FormView):

    def get(self, request, *args, **kwargs):
        form = IngredientForm()
        return render(request, 'cooking/ingredients_form.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = IngredientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/add_i/')


