from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="test_app_-home"),
    path('about/', views.about, name="test_app_-about")
]