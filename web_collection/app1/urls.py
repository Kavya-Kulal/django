from django.urls import path
from .views import create_collection,home,get_collections,save_bookmark,get_bookmarks

urlpatterns = [
    path('',home,name='home'),
    path('create-collection/', create_collection, name='create_collection'),
    path("get-collections/", get_collections, name="get_collections"),
    path('save_bookmark/', save_bookmark, name='save_bookmark'),
    path('get_bookmarks/<int:collection_id>/', get_bookmarks, name='get_bookmarks'),
]
