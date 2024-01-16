from django.shortcuts import render
from django.http import HttpResponse

def home_url(request):
    return HttpResponse("HOME")


def contact_url(request):
    return HttpResponse("CONTACT")


def about_url(request):
    return HttpResponse("ABOUT")
