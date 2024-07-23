from django.shortcuts import render
from utils.recipes.faker_info import make_recipe
from recipes.models import Recipe

def home(request):
    recipes = Recipe.objects.all().order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'name': 'Home',
        'recipes': recipes,
        # 'recipes': [make_recipe() for _ in range(10)] # In case i need to use in the future.
    })

def category(request, category_id):
    category = Recipe.objects.filter(category__id=category_id).order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'name': 'Home',
        'recipes': category,
        # 'recipes': [make_recipe() for _ in range(10)] # In case i need to use in the future.
    })

def recipe(request, id):
    recipes = Recipe.objects.filter(id=id).first()
    return render(request, 'recipes/pages/recipe-view.html', context={
        'name': 'Recipe View',
        'recipe': recipes,
        'is_viewing_recipe': True,
    })

