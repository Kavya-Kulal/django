from django.shortcuts import render
from app1.forms import inputform
list1=[]
result=[1]
# Create your views here.
def multiply(ip1,ip2):
    for j in range(ip1 ,ip2+1):
        for i in range(1,11):
            s=str(j)+"*"+str(i)+"="+str(j*i)
            list1.append(s)
        list1.append("---------------------------------")
        print()
    return list1    

def home(request):
    if request.method=="POST":
        form1=inputform(request.POST)
        if form1.is_valid():
            data=form1.cleaned_data
            ip1=data.get("input1")
            ip2=data.get("input2")
            result=multiply(ip1,ip2)
            return render(request,"app1/index.html",{'param1':result,'form':form1})
    else:
        form1=inputform()  
    return render(request,"app1/index.html",{ 'form':form1})
    

