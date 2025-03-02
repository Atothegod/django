from django.contrib import admin
from .models import Seller

# Register Seller model to admin panel
class SellerAdmin(admin.ModelAdmin):
    list_display = ('user', 'shop_name')  # แสดง user และ shop_name ในหน้าแสดงผล
    search_fields = ('shop_name',)  # ค้นหาจาก shop_name
    list_filter = ('user',)  # ฟิลเตอร์จาก user

admin.site.register(Seller, SellerAdmin)
