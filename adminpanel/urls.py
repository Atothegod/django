from django.urls import path
from . import views

app_name = 'adminpanel'

urlpatterns = [
    path('users_manage/', views.manage_users, name='manage_users'),
    path('sellers_manage/', views.manage_sellers, name='manage_sellers'),
    path('reports_view/', views.view_reports, name='view_reports'),
]
