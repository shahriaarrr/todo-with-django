from django.shortcuts import render
from django.http import HttpResponse

from .forms import TaskForm
# Create your views here.
def home(request):
    return HttpResponse("<h1>Welcom to Todo website</h1>")

def addTask(request):
    if request.method == "GET":
        form = TaskForm()
        return render(request, 'signup.html', {'form' : form})
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            return HttpResponse(f"<h1>your task({task.title}) seccessfuly add</h1>")