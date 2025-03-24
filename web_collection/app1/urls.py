from django.urls import path
from .views import create_collection,home,get_collections,save_bookmark,get_bookmarks,delete_bookmark,delete_collection,rename_collection


urlpatterns = [
    path('',home,name='home'),
    path('create-collection/', create_collection, name='create_collection'),
    path("get-collections/", get_collections, name="get_collections"),
    path('save_bookmark/', save_bookmark, name='save_bookmark'),
    path('get_bookmarks/<int:collection_id>/', get_bookmarks, name='get_bookmarks'),
    path('delete_bookmark/<path:url>/', delete_bookmark, name='delete_bookmark'),
    path('delete_collection/<int:collection_id>/',delete_collection,  name='delete_collection'),
     path('rename_collection/<int:collection_id>/', rename_collection, name='rename_collection'),

]
