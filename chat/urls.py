from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    path('seller-chat/', views.chat_with_seller, name='chat_with_seller'),  # แชทกับผู้ขาย
    path('admin-chat/', views.chat_with_admin, name='chat_with_admin'),  # แชทกับแอดมิน
]
