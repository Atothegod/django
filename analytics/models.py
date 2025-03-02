from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Analytics(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
