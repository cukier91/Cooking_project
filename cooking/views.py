from django.shortcuts import render, redirect
from django.views import View
from .models import *
from .forms import IngredientForm
from django.urls import reverse_lazy
from django.views.generic.edit import FormView


# class IngredientsFormView(View):
#     def get(self,request, *args, **kwargs):
#         form = IngredientForm()
#         context = {
#             'form': form
#         }
#         return render(request, "cooking/ingredients_form.html", context)
#
#     def post(self,request, *args, **kwargs):

class IngredientsFormView(FormView):
    form_class = IngredientForm
    success_url = reverse_lazy("add_ingredient")
    template_name = 'cooking/ingredients_form.html'

    def get(self, request, *args, **kwargs):
        """Handle GET requests: instantiate a blank version of the form."""
        return self.render_to_response(self.get_context_data())

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests: instantiate a form instance with the passed
        POST variables and then check if it's valid.
        """
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

