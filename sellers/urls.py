from django.urls import path
from . import views

app_name = 'sellers'

urlpatterns = [
    path('register/', views.register_seller, name='register_seller'),
    path('profile_seller/', views.manage_profile, name='manage_profile'),
    path('products/', views.manage_products, name='manage_products'),
    path('point/', views.manage_point, name='manage_point'),
]
