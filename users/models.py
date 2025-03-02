from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models
class User(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)

    def signUp(self):
        pass

    def login(self):
        pass

    def viewProfile(self):
        pass

    def manageGiftCard(self):
        pass