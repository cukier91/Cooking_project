from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.views import View
from .models import *

from .forms import IngredientForm, RecipeForm, RecipeIngredientForm


class IngredientsFormView(FormView):

    def get(self, request, *args, **kwargs):
        ingredients = IngredientsModel.objects.all()
        form = IngredientForm()
        return render(request, 'cooking/ingredients_form.html', {'form': form, 'ingredients': ingredients})

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
        delete = RecipeIngredientsModel.objects.filter(amount__exact=0).delete()
        recipe = RecipeModel.objects.get(id=pk)
        ingredients = RecipeIngredientsModel.objects.filter(recipe_id=pk)

        form = RecipeIngredientForm(initial={'recipe': recipe})
        context = {
            'recipe': recipe,
            'pk': pk,
            'form': form,
            'ingredients': ingredients,

        }
        return render(request, 'cooking/recipe_detail.html', context)

    def post(self, request, *args, **kwargs):
        form = RecipeIngredientForm(request.POST or None)
        if form.is_valid():
            form.save()
            recipe_id = RecipeIngredientsModel.objects.all().last().recipe_id
            return redirect(f'/detail_r/{recipe_id}/')


class MainView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'cooking/home.html')


def delete_ingredient(request, ingredients_id, recipe_id):
    ingredient = RecipeIngredientsModel.objects.filter(ingredients_id=ingredients_id, recipe_id=recipe_id)
    redirect_direct = [ingredient[0].recipe_id]
    if request.method == 'GET':
        ingredient.delete()
        return redirect(f'/detail_r/{redirect_direct[0]}/')


class MenuView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'cooking/random_menu.html')