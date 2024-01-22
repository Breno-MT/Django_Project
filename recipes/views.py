from django.shortcuts import render

def home_url(request):
    return render(request, 'recipes/home.html', context={'name': 'Home'})

