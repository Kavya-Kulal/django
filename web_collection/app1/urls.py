from django.urls import path
from . import views  # Ensure this import is correct

urlpatterns = [
    path('', views.home, name='home'),  # Example URL pattern
]
