from django.urls import path

from .views import *

urlpatterns = [
    path('signup/', SignupAPIView.as_view(), name='signupAPI'),
]