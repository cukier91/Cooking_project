"""Cooking_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from cooking import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add_i/', v.IngredientsFormView.as_view(), name="add_ingredient"),
    path('add_r/', v.RecipeFormView.as_view(), name="add_recipe"),
    path('detail_r/<int:pk>/', v.RecipeDetailView.as_view(), name="detail_recipe"),
    path('', v.MainView.as_view(), name='main_page'),
    path('detail_r/delete/<int:ingredients_id>/<int:recipe_id>/', v.delete_ingredient, name='delete_ingredient'),
    path('menu/', v.MenuView.as_view(), name='menu'),
    path('detail_m/<int:pk>/', v.MenuDetailView.as_view(), name="detail_menu"),
    path('basket/<int:pk>/', v.BasketView.as_view(), name="basket"),
    path('shoopinglist/', v.ShoppingListView.as_view(), name="shopping_lists"),
    path('recipe/<int:pk>/', v.RecipeView.as_view(), name="recipe"),
    path('register/', v.register, name="register"),
    path('login/', v.loginview, name="login"),

]
