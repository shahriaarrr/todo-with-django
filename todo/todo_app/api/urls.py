from django.urls import path

from .views import addTaskView

urlpatterns = [
    path('add/', addTaskView.as_view()),
]
