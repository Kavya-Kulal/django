from django.urls import path
from app1.views import home
app_name='app1'
urlpatterns = [path('' , name='design'),]
 


from django.contrib import admin 
from django.urls import path 
from . import views 

app_name = 'app1' 
urlpatterns = [ 
	
	path('', views.home, name='design'), 
   

    
    
     
   
    
   
]
