from django.urls import path
from . import views

app_name = 'analytics'

urlpatterns = [
    path('collect-data/', views.collect_data, name='collect_data'),  # รวบรวมข้อมูล
    path('dashboard/', views.generate_dashboard, name='generate_dashboard'),  # แสดงแดชบอร์ด
]
