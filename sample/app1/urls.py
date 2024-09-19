# urls.py
from django.urls import path
from .views import process_audio

urlpatterns = [
    # Other URL patterns...
    path('process_audio/', process_audio, name='process_audio'),
]
