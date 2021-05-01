from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.views import View
from .models import *

from .forms import IngredientForm, RecipeForm, RecipeIngredientForm


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
        ingredients = IngredientsModel.objects.all().first()
        form = RecipeForm(initial={'ingredients': ingredients})
        recipe = RecipeModel.objects.all()
        return render(request, 'cooking/recipe_form.html', {'form': form, 'recipe': recipe, 'ingredients': ingredients})

    def post(self, request, *args, **kwargs):
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            recipe = RecipeModel.objects.last()
            return redirect(f'/detail_r/{recipe.id}/')


class RecipeDetailView(View):

    def get(self, request, pk, *args, **kwargs):
        recipe = RecipeModel.objects.get(id=pk)
        form = RecipeIngredientForm(initial={'recipe': recipe})
        return render(request, 'cooking/recipe_detail.html', {'recipe': recipe, 'pk': pk, 'form': form})

    def post(self, request, *args, **kwargs):
        form = RecipeIngredientForm(request.POST or None)
        recipe_id = RecipeModel.objects.all().last().id
        if form.is_valid():
            form.save()
            return redirect(f'/detail_r/{recipe_id}/')


class MainView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'cooking/base.html')

