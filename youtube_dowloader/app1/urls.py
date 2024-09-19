from django.contrib import admin 
from django.urls import path 
from . import views 

app_name = 'app1' 
urlpatterns = [ 
	
	path('', views.design, name='design'), 
    path('/youtube',views.youtube,name='youtube'),

    
    
     
   
    
   
]
