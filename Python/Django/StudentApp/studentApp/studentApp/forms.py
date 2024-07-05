# studentApp/forms.py

from django import forms
from django.core import validators

def start_with_d(value):
    if value[0].lower() != 'd':
        raise forms.ValidationError("Name should start with d")

class MyForm(forms.Form):
    # name = forms.CharField(label='Name', max_length=100, validators=[validators.MinLengthValidator(4), validators.MaxLengthValidator(10)])
    name = forms.CharField(validators = [start_with_d])
    email = forms.EmailField(label='Email')
    age = forms.IntegerField(label='Age')
