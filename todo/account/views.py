from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .forms import *
# Create your views here.
@csrf_exempt
def signup(request):
    if request.method == "GET":
        form = Signup()
        return render(request, 'signup.html', {'form' : form})
    if request.method == "POST":
        form = Signup(request.POST)
        if form.is_valid():
            user = form.save()
            return render(request, 'seccess.html', {'username' : user.username})