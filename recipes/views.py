from django.shortcuts import render
from django.http import HttpResponse

def home_url(request):
    return render(request, 'recipes/home.html')


def contact_url(request):
    return render(request, 'recipes/contact.html')


def about_url(request):
    return render(request, 'recipes/about.html')
