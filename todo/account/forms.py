from django import forms
from django import forms
from .models import *

class Signup(forms.ModelForm):
    class Meta:
        models = User
        fields = ('username', 'first name', 'last name', 'email', 'age', 'gender')


class Login(forms.ModelForm):
    class Meta:
        models = User
        fields = ('username', 'password')