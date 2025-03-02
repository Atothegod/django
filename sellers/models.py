# from django.db import models
# from users.models import User

# class Seller(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     shop_name = models.CharField(max_length=255)

#     def registerAsSeller(self):
#         pass

#     def manageProfile(self):
#         pass

#     def manageProduct(self):
#         pass

#     def managePoint(self):
#         pass

# class Product(models.Model):
#     seller = models.ForeignKey(Seller, related_name="products", on_delete=models.CASCADE)
#     name = models.CharField(max_length=255)
#     description = models.TextField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     stock_quantity = models.PositiveIntegerField()
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.name
# seller/models.py
from django.db import models
from users.models import User

class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    shop_name = models.CharField(max_length=255)

    def registerAsSeller(self):
        # ฟังก์ชันนี้ยังไม่ทำอะไร เพราะมันง่ายมาก ๆ ตอนนี้
        pass

    def manageProfile(self):
        # ฟังก์ชันนี้ยังไม่ทำอะไร
        pass

    def manageProduct(self):
        # ฟังก์ชันนี้ยังไม่ทำอะไร
        pass

    def managePoint(self):
        # ฟังก์ชันนี้ยังไม่ทำอะไร
        pass
