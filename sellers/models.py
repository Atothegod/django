from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # เพิ่มฟิลด์อื่น ๆ ตามต้องการ
class Seller(models.Model):
    name = models.CharField(max_length=100)
    products = models.ManyToManyField('Product', related_name='sellers')
