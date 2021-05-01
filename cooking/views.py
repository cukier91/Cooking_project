from django.shortcuts import render, redirect
from django.views.generic.edit import FormView, CreateView
from django.views import View
from .models import *

from .forms import IngredientForm, RecipeForm


class IngredientsFormView(FormView):

    def get(self, request, *args, **kwargs):
        form = IngredientForm()
        return render(request, 'cooking/ingredients_form.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = IngredientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/add_i/')


class RecipeFormView(FormView):

    def get(self, request, *args, **kwargs):
        form = RecipeForm()
        recipe = RecipeModel.objects.all()
        return render(request, 'cooking/recipe_form.html', {'form': form, 'recipe': recipe})

    def post(self, request, *args, **kwargs):
        form = RecipeForm(request.POST)
        recipe = RecipeModel.objects.last()
        if form.is_valid():
            form.save()
            return redirect(f'/detail_r/{recipe.id}/')


class RecipeDetailView(View):

    def get(self, request, pk, *args, **kwargs):
        recipe = RecipeModel.objects.get(id=pk)
        return render(request, 'cooking/recipe_detail.html', {'recipe': recipe, 'pk': pk})

class MainView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'cooking/base.html')

