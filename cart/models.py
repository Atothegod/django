from django.db import models
from users.models import User

class ShoppingCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def addItem(self):
        pass

    def removeItem(self):
        pass

    def viewCart(self):
        pass

class PaymentSystem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def processPayment(self):
        pass

    def generateInvoice(self):
        pass

class OrderSystem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def placeOrder(self):
        pass

    def trackOrder(self):
        pass

    def cancelOrder(self):
        pass
