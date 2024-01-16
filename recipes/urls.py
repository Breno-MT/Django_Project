from django.urls import path, include
from .views import home_url, contact_url, about_url

urlpatterns = [
    path('', home_url),
    path('contact/', contact_url),
    path('about/', about_url),
]
