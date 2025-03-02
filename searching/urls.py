# searching/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # ตัวอย่าง URL patterns
    path('', views.search_view, name='search_view'),
]
from django.urls import path
from .views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]
