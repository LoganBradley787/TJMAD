from django.shortcuts import render
from django.views.generic import TemplateView, View


class HomeView(TemplateView):
    template_name = "home.html"


# Create your views here.
