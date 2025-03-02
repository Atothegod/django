from django.db import models
from users.models import User

class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def manageUsers(self):
        pass

    def manageSellers(self):
        pass

    def viewReports(self):
        pass
