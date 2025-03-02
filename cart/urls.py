from django.urls import path
from . import views

app_name = 'cart'  # กำหนด app_name ที่นี่

urlpatterns = [
    path('cart_view/', views.view_cart, name='view_cart'),
    path('cart_view/add/', views.add_item, name='add_item'),
    path('cart_view/remove/', views.remove_item, name='remove_item'),
    path('payment/', views.process_payment, name='process_payment'),
    path('invoice/', views.generate_invoice, name='generate_invoice'),
    path('order/place/', views.place_order, name='place_order'),
    path('order/track/', views.track_order, name='track_order'),
    path('order/cancel/', views.cancel_order, name='cancel_order'),
]
