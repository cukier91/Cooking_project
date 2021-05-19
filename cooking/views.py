from django.shortcuts import render, redirect
from django.template.smartif import key
from django.views.generic.edit import FormView
from django.views import View
from .models import *
import random
from faker import Faker
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


from .forms import IngredientForm, RecipeForm, RecipeIngredientForm, MenuPlanForm, CreateUserForm


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


# @login_required(login_url='login')
def mainview(request, *args, **kwargs):
    return render(request, 'cooking/home.html')


def delete_ingredient(request, ingredients_id, recipe_id):
    #TODO przy usuwaniu powtarzającego się składnika usuwa wszystkie wystąpienia, zmienić sposób wyszukiwania po ID modelu
    # RecipeIngredientModel zamiast ID składnika !!
    ingredient = RecipeIngredientsModel.objects.filter(ingredients_id=ingredients_id, recipe_id=recipe_id)
    redirect_direct = [ingredient[0].recipe_id]
    if request.method == 'GET':
        ingredient.delete()
        return redirect(f'/detail_r/{redirect_direct[0]}/')


class MenuView(View):
    #TODO Koniecznie naprawić powtarzanie się w przepisach w których wystepuje więcej niż jedna kategoria
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
        recipe_b = RecipeModel.objects.filter(mealtype__contains='Śniadanie')
        meal_name = 'Śniadanie'
        recipe_random_pick = random.sample(list(recipe_b), 7)
        day_name = ['Poniedziałek', 'Wtorek', 'Środa', 'Czwartek', 'Piątek', 'Sobota', 'Niedziela']
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
        recipe_sb = RecipeModel.objects.filter(mealtype__contains='Drugie śniadanie')
        meal_name = 'Drugie śniadanie'
        recipe_random_pick = random.sample(list(recipe_sb), 7)
        day_name = ['Poniedziałek', 'Wtorek', 'Środa', 'Czwartek', 'Piątek', 'Sobota', 'Niedziela']
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
        day_name = ['Poniedziałek', 'Wtorek', 'Środa', 'Czwartek', 'Piątek', 'Sobota', 'Niedziela']
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
        day_name = ['Poniedziałek', 'Wtorek', 'Środa', 'Czwartek', 'Piątek', 'Sobota', 'Niedziela']
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
        day_name = ['Poniedziałek', 'Wtorek', 'Środa', 'Czwartek', 'Piątek', 'Sobota', 'Niedziela']
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
            # return redirect(f'/detail_m/{menu_id}/')
            return redirect(reverse('detail_menu', kwargs={'pk': menu_id}))
        else:
            return redirect('main_page')


class MenuDetailView(View):
    def get(self, request, pk, *args, **kwargs):
        menu_p = MenuRecipeModel.objects.filter(menu_id=pk, day_name='Poniedziałek')
        menu_w = MenuRecipeModel.objects.filter(menu_id=pk, day_name='Wtorek')
        menu_s = MenuRecipeModel.objects.filter(menu_id=pk, day_name='Środa')
        menu_c = MenuRecipeModel.objects.filter(menu_id=pk, day_name='Czwartek')
        menu_pt = MenuRecipeModel.objects.filter(menu_id=pk, day_name='Piątek')
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
    # TODO Pytanie czy potrzebny jest model do koszyka czy wystarczy wyświetlanie na słowniku
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
            'basket': basket
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


def register(request):
    if request.user.is_authenticated:
        return redirect('main_page')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Konto zostało utworzone poprawnie, Smacznego ! ' + user)
                return redirect('login')

        context = {
            'form': form
        }
        return render(request,'cooking/register.html', context)


def loginview(request):
    if request.user.is_authenticated:
        return redirect('main_page')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('main_page')
            else:
                messages.info(request, 'Nazwa użytkownika lub hasło są niepoprawne ')

        context = {}
        return render(request, 'cooking/login.html', context)


def logoutview(request):
    logout(request)
    return redirect('login')

