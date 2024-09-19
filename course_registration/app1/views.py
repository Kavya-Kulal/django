from django.shortcuts import render
# Create your views here.
from django.shortcuts import render
from app1.forms import inputform

def home(request):
    ip1=""
    ip2=""
    ip3=""
    if request.method=="POST":
        form1=inputform(request.POST)
        if form1.is_valid():
            data=form1.cleaned_data
            ip1=data.get("name")
            ip2=data.get("college")
            ip3=data.get("course")

            
            return render(request,"app1/index.html",{'param1':ip1, 'param2':ip2,'param3':ip3, 'form':form1})
    else:
        form1=inputform()  
    return render(request,"app1/index.html",{'param1':ip1, 'param2':ip2,'param3':ip3, 'form':form1})
