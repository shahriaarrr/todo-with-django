from django.urls import path

from .views import *

urlpatterns = [
    path('add-task', addTaskView.as_view()),
    path('delete-task', DeleteTaskAPIView.as_view()),
]
