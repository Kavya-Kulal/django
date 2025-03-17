from django.urls import path
from .views import home, insert_collection

urlpatterns = [
    path("", home, name="home"),
    path("insert/", insert_collection, name="insert_collection"),
]
