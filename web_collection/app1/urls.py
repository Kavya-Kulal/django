from django.urls import path
from .views import create_collection,home,get_collections

urlpatterns = [
    path('',home,name='home'),
    path('create-collection/', create_collection, name='create_collection'),
    path("get-collections/", get_collections, name="get_collections"),
]
