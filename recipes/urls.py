from django.urls import path
from .views import home_url

urlpatterns = [
    path('', home_url),
    path('contact/', contact_url),
    path('about/', about_url),
]
