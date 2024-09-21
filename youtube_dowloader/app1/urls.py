from django.contrib import admin 
from django.urls import path 
from . import views 

app_name = 'app1' 
urlpatterns = [ 
	
	path('', views.design, name='design'), 
    path('youtube/',views.youtube,name='youtube'),
    path('youtube_page/',views.youtube_page,name='youtube_page'),
     path('facebook_page/', views.facebook_page, name='facebook_page'),
     path('facebook',views.facebook,name='facebook'),

    
    
     
   
    
   
]
