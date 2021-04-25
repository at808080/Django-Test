from django.db import models
from django.utils import timezone

# Create your models here.

class Player(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    history = models.TextField()

class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Player, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)
    content = models.TextField()