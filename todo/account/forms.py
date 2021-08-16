from django import forms
from django import forms
from .models import *

class Signup(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'


class Login(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')