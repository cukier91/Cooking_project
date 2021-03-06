from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.views import View
from .models import *
import random
from faker import Faker
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView, LogoutView
from calories.views import API

from .forms import IngredientForm, RecipeForm, RecipeIngredientForm, MenuPlanForm, CreateUserForm


class IngredientsFormView(PermissionRequiredMixin, FormView):
    permission_required = 'Can add ingredients model'

    def get(self, request, *args, **kwargs):
        ingredients = IngredientsModel.objects.all()
        form = IngredientForm()
        return render(request, 'cooking/ingredients_form.html', {'form': form, 'ingredients': ingredients})

    def post(self, request, *args, **kwargs):
        form = IngredientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/add_i/')


class RecipeFormView(PermissionRequiredMixin, FormView):
    permission_required = 'Can add recipe model'

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


def mainview(request, *args, **kwargs):
    return render(request, 'cooking/home.html')


def delete_ingredient(request, id, recipe_id):
    ingredient = RecipeIngredientsModel.objects.filter(id=id, recipe_id=recipe_id)
    redirect_direct = [ingredient[0].recipe_id]
    if request.method == 'GET':
        ingredient.delete()
        return redirect(f'/detail_r/{redirect_direct[0]}/')


class MenuView(LoginRequiredMixin, View):
    login_url = '/login/'
    #TODO Koniecznie naprawi?? powtarzanie si?? w przepisach w kt??rych wystepuje wi??cej ni?? jedna kategoria

    def get(self, request, *args, **kwargs):
        fake = Faker()
        name = fake.name
        menu = MenuPlanModel.objects.all()
        form = MenuPlanForm(initial={'name': name})
        context = {
            'form': form,
            'menu': menu
        }
        return render(request, 'cooking/random_menu.html', context)

    def breakfast(self):
        recipe_b = RecipeModel.objects.filter(mealtype__contains='??niadanie')
        meal_name = '??niadanie'
        recipe_random_pick = random.sample(list(recipe_b), 7)
        day_name = ['Poniedzia??ek', 'Wtorek', '??roda', 'Czwartek', 'Pi??tek', 'Sobota', 'Niedziela']
        breakfast = {
            'recipe_random_pick': [],
            'day_name': day_name,
            'meal_name': []
        }
        for i in range(0, 7):
            breakfast['recipe_random_pick'].append(recipe_random_pick[i])
            breakfast['meal_name'].append(meal_name)
        return breakfast

    def second_breakfast(self):
        recipe_sb = RecipeModel.objects.filter(mealtype__contains='Drugie ??niadanie')
        meal_name = 'Drugie ??niadanie'
        recipe_random_pick = random.sample(list(recipe_sb), 7)
        day_name = ['Poniedzia??ek', 'Wtorek', '??roda', 'Czwartek', 'Pi??tek', 'Sobota', 'Niedziela']
        sbreakfast = {
            'recipe_random_pick': [],
            'day_name': day_name,
            'meal_name': []
        }
        for i in range(0, 7):
            sbreakfast['recipe_random_pick'].append(recipe_random_pick[i])
            sbreakfast['meal_name'].append(meal_name)
        return sbreakfast

    def lunch(self):
        recipe_l = RecipeModel.objects.filter(mealtype__contains='Lunch do pracy')
        meal_name = 'Lunch do pracy'
        recipe_random_pick = random.sample(list(recipe_l), 7)
        day_name = ['Poniedzia??ek', 'Wtorek', '??roda', 'Czwartek', 'Pi??tek', 'Sobota', 'Niedziela']
        lunch = {
            'recipe_random_pick': [],
            'day_name': day_name,
            'meal_name': []
        }
        for i in range(0, 7):
            lunch['recipe_random_pick'].append(recipe_random_pick[i])
            lunch['meal_name'].append(meal_name)
        return lunch

    def dinner(self):
        recipe_d = RecipeModel.objects.filter(mealtype__contains='Obiad')
        meal_name = 'Obiad'
        recipe_random_pick = random.sample(list(recipe_d), 7)
        day_name = ['Poniedzia??ek', 'Wtorek', '??roda', 'Czwartek', 'Pi??tek', 'Sobota', 'Niedziela']
        dinner = {
            'recipe_random_pick': [],
            'day_name': day_name,
            'meal_name': []
        }
        for i in range(0, 7):
            dinner['recipe_random_pick'].append(recipe_random_pick[i])
            dinner['meal_name'].append(meal_name)
        return dinner

    def supper(self):
        recipe_d = RecipeModel.objects.filter(mealtype__contains='Kolacja')
        meal_name = 'Kolacja'
        recipe_random_pick = random.sample(list(recipe_d), 7)
        day_name = ['Poniedzia??ek', 'Wtorek', '??roda', 'Czwartek', 'Pi??tek', 'Sobota', 'Niedziela']
        supper = {
            'recipe_random_pick': [],
            'day_name': day_name,
            'meal_name': []
        }
        for i in range(0, 7):
            supper['recipe_random_pick'].append(recipe_random_pick[i])
            supper['meal_name'].append(meal_name)
        return supper

    def post(self, request, *args, **kwargs):
        form = MenuPlanForm(request.POST or None)
        if form.is_valid():
            form.save()
            menu_id = MenuPlanModel.objects.all().last().id
            for meal in [
                self.breakfast(),
                self.second_breakfast(),
                self.lunch(),
                self.dinner(),
                self.supper()
            ]:
                for i in range(0, 7):
                    menurecipe = MenuRecipeModel.objects.create(
                        recipe_id=meal['recipe_random_pick'][i].id,
                        menu_id=menu_id,
                        day_name=meal['day_name'][i],
                        meal_name=meal['meal_name'][i]
                    )
            return redirect(reverse('detail_menu', kwargs={'pk': menu_id}))
        else:
            return redirect('main_page')


class MenuDetailView(View):
    def get(self, request, pk, *args, **kwargs):
        menu_p = MenuRecipeModel.objects.filter(menu_id=pk, day_name='Poniedzia??ek')
        menu_w = MenuRecipeModel.objects.filter(menu_id=pk, day_name='Wtorek')
        menu_s = MenuRecipeModel.objects.filter(menu_id=pk, day_name='??roda')
        menu_c = MenuRecipeModel.objects.filter(menu_id=pk, day_name='Czwartek')
        menu_pt = MenuRecipeModel.objects.filter(menu_id=pk, day_name='Pi??tek')
        menu_so = MenuRecipeModel.objects.filter(menu_id=pk, day_name='Sobota')
        menu_n = MenuRecipeModel.objects.filter(menu_id=pk, day_name='Niedziela')
        context = {
            'menu_p': menu_p,
            'menu_w': menu_w,
            'menu_s': menu_s,
            'menu_c': menu_c,
            'menu_pt': menu_pt,
            'menu_so': menu_so,
            'menu_n': menu_n,
            'pk': pk
        }
        return render(request, 'cooking/menu_detail.html', context)


class BasketView(View):
    # TODO Pytanie czy potrzebny jest model do koszyka czy wystarczy wy??wietlanie na s??owniku
    def get(self, request, pk, *args, **kwargs):

        menu = MenuRecipeModel.objects.filter(menu_id=pk)
        basket = {}
        recipes = []
        ingredients = []
        for m in menu:
            recipes.append(m.recipe_id)
        for r in recipes:
            query = RecipeIngredientsModel.objects.filter(recipe_id=r).all()
            for q in query:
                i = IngredientsModel.objects.filter(id=q.ingredients_id)
                if f'{i[0]}' in basket:
                    basket[f'{i[0]}'][0] = basket[f'{i[0]}'][0] + q.amount
                else:
                    basket[f'{i[0]}'] = [q.amount, q.unit]
        ctx = {
            'recipes': recipes,
            'menu': menu,
            'ingredients': ingredients,
            'basket': basket,
        }
        return render(request, 'cooking/basket.html', ctx)


class ShoppingListView(View):

    def get(self,request, *args, **kwargs):
        menu = MenuPlanModel.objects.all()
        ctx = {
            'menu': menu
        }
        return render(request, 'cooking/shopping_lists.html', ctx)


class RecipeView(View):
    def get(self, request, pk, *args, **kwargs):
        recipe = RecipeModel.objects.filter(id=pk)
        ingredients = RecipeIngredientsModel.objects.filter(recipe_id=pk).all()
        ctx = {
            'recipe': recipe,
            'ingredients': ingredients
        }
        return render(request, 'cooking/recipe.html', ctx)


class LoginTest(UserPassesTestMixin):

    def test_func(self):
        if self.request.user.id is None:
            return True


class Register(LoginTest, View):

    def get(self, request, *args, **kwargs):
        form = CreateUserForm()
        context = {
            'form': form
        }
        return render(request, 'cooking/register.html', context)

    def post(self, request, *args, **kwargs):
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            return redirect('login')


class LogoutView(LogoutView):
    next_page = '/login/'


class LoginClassView(LoginTest, LoginView):
    # Todo zmieni?? na form
    template_name = 'cooking/login.html'

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('main_page')
        else:
            messages_f = ['Nieprawid??owa nazwa u??ytkownika lub has??o']
        return render(request, 'cooking/login.html', {'messages_f': messages_f})


