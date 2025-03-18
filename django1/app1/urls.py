from django.urls import path
from .views import submit_url, success

urlpatterns = [
    path('', submit_url, name='submit_url'),
    path('success/', success, name='success'),
]
