from django.db import models
from django.contrib.auth.models import User 
from PIL import Image

# Create your models here.

class Profile(models.Model): #inherit from models.Model
    user = models.OneToOneField(User, on_delete=models.CASCADE) #assign a 1:1 realtionship with user model
                                                                # assign on delete function, cascade means delete profile if user is deleted
    #imagesrc = models.StringField()
    image = models.ImageField(default="default.jpg", upload_to="profile_pics")

    def __str__(self): #basically a tostring method for the profile object
        return f'{self.user.username} Profile'

    def save(self):
        super().save()
        img = Image.open(self.image.path)
        if img.height > 240 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
