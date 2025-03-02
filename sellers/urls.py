# sellers/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # ตัวอย่าง URL patterns
    path('', views.some_view, name='some_view'),
]
from django.urls import path
from .views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]
