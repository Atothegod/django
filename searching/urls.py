# searching/urls.py
from django.urls import path
from . import views

app_name = 'searching'

urlpatterns = [
    path('search/', views.search_view, name='search_view'),
    path('filter/', views.filter_view, name='filter_view'),
]
