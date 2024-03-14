from django.shortcuts import render
from utils.recipes.faker_info import make_recipe

def home_url(request):
    return render(request, 'recipes/pages/home.html', context={
        'name': 'Home',
        'recipes': [make_recipe() for _ in range(10)]
    })

def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'name': 'Recipe View',
        'recipe': make_recipe(),
        'is_viewing_recipe': True,
    })

