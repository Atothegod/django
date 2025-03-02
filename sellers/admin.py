from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Seller, Product

admin.site.register(Seller)   # ทำให้ Seller ปรากฏใน Admin Panel
admin.site.register(Product)  # ทำให้ Product ปรากฏใน Admin Panel
