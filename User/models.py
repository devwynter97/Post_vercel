from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# One to One relationship with User table 
# Single profile for single user

class Profile(models.Model):
    # delete profile if user is deleted CASCADE not the other way around
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    image = models.ImageField(default = 'default.jpeg', upload_to = 'profile_pics')
    about = models.TextField(null = True)

    
    def __str__(self):
        return f"{self.user.username} Profile"