from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def Register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save() #creates the user in the system
            username = form.cleaned_data.get("username")
            messages.success(request, f'Acccount Created for {username}')
            return redirect("login") #name given to url path in test_app_ urls
    else:
        form = UserRegistrationForm()
    return render(request, "users/register.html", {"form":form})

@login_required #decorator to ensure that redirected to profile only if already logged in
def Profile(request):
    return render(request, "users/profile.html")