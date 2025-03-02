from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # แก้ไขการชนกันของ related_name
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',  # เปลี่ยนชื่อ
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions_set',  # เปลี่ยนชื่อ
        blank=True
    )