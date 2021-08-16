from django import forms
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *

class Signup(UserCreationForm):
    pass


class Login(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')