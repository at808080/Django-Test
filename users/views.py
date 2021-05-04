from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm
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
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        prof_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and prof_form.is_valid():
            user_form.save()
            prof_form.save()
            messages.success(request, f'Profile updated successfully')
            return redirect("profile") 
    
    else:
        user_form = UserUpdateForm(instance=request.user)
        prof_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        "user_form": user_form,
        "prof_form": prof_form
    }
    return render(request, "users/profile.html", context)