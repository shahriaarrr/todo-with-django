from django.urls import path

from .views import *

urlpatterns = [
    path('', home, name="main page"),
    path('add-task/', addTask, name="addTask"),
]