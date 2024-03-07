from django.shortcuts import render

def home_url(request):
    return render(request, 'recipes/pages/home.html', context={'name': 'Home'})

def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={'name': 'Recipe View'})

