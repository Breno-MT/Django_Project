from django.urls import path
from .views import home_url

urlpatterns = [
    path('', home_url),
]
