from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('signup/', views.sign_up, name='sign_up'),  # URL สำหรับการสมัครสมาชิก
    path('login/', views.login, name='login'),  # URL สำหรับการเข้าสู่ระบบ
    path('profile_user/', views.view_profile, name='view_profile'),  # URL สำหรับการดูโปรไฟล์
    path('giftcard/', views.manage_gift_card, name='manage_gift_card'),  # URL สำหรับการจัดการบัตรของขวัญ
]