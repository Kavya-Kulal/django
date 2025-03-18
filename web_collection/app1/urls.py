from django.urls import path
from .views import create_collection,home

urlpatterns = [
    path('',home,name='home'),
    path('create-collection/', create_collection, name='create_collection'),
]
