from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import *

urlpatterns = [
    path('signup/', SignupAPIView.as_view(), name='signupAPI'),
    path('login/', view=obtain_auth_token, name='LoginAPIview'),
    path('logout/', LogoutAPIView.as_view(), name='LogoutAPIview'),
]