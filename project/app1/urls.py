# app1/urls.py
from django.urls import path, include, re_path ,path
from . import views
from app1.views import home
from app1.views import process_spoken_text

urlpatterns = [
    # Other URL patterns...
    re_path(r'^process_spoken_text/$', views.process_spoken_text, name='process_spoken_text'),
    re_path(r'analyze_sentiment/$',views.analyze_sentiment,name='analyze_sentiment'),
    
    path('', home),
]
