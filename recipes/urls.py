from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_url),
    path('recipes/<int:id>/', views.recipe),
]
