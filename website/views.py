from django.shortcuts import render
from django.http import HttpResponse
from .forms import RegistrationForm


def home(request):

    return render(request, "website/index.html")

def dashboard(request):

    return render(request, "website/header.html")
