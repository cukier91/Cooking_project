from django import forms
from .models import Person, Movie

class PeopleForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = [
            'first_name',
            'last_name'
        ]


