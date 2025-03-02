from django.shortcuts import render

# Create your views here.
# searching/views.py

from django.http import HttpResponse

def search_view(request):
    return HttpResponse("Search page is working!")
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = "home.html"
