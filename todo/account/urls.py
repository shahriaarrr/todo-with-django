from django.urls import path, include

from .views import *

urlpatterns = [
    path('signup/', signup, name='signup'),
]