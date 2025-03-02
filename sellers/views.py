from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = "home.html"


def some_view(request):
    return HttpResponse("Hello, this is the some_view!")