from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Player

# Create your views here.

players = [
    {
        "name": "Hoops",
        "position": "Flanker", 
        "country": "Aus"
    },
    {
        "name": "Hamish",
        "position": "Flanker", 
        "country": "Scotland"
    },
    {
        "name": "Paolo",
        "position": "Flyhalf", 
        "country": "ITALIA"
    }
]

def home(request):
    """
    context = {
        "title": "HOME PAGE TEST APP",
        "things": players
    }
    return render(request, "test_app_/home.html", context)
    """
    context = {
        "title": "HOME PAGE TEST APP",
        "things": Player.objects.all()
    }
    return render(request, "test_app_/home.html", context)

def about(request):
    return render(request, "test_app_/about.html", {"title": "ABOUT PAGE TEST APP"})