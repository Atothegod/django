from django.db import models
from users.models import User
from sellers.models import Seller

class ChatSupport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, null=True, blank=True)
    admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name="admin_chat", null=True, blank=True)

    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def chatWithSeller(self):
        # ฟังก์ชันแชทกับผู้ขาย
        pass

    def chatWithAdmin(self):
        # ฟังก์ชันแชทกับแอดมิน
        pass
