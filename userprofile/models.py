from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Userprofile(models.Model):
    user=models.OneToOneField(User, related_name="userprofile", on_delete=models.CASCADE)

    def __str__(self):
        return self.user
    
class Username(models.Model):
    username=models.TextField(max_length=20)
    password=models.TextField(max_length=20)
    created=models.DateTimeField(auto_now_add=True)