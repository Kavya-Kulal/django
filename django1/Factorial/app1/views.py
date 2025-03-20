
from app1.forms import inputform


# Create your views here.

    
def home(request):

    
    result=1
    n1=1
    if request.method=="POST":
        form1=inputform(request.POST)
        if form1.is_valid():
            data=form1.cleaned_data
            n1=data.get("input")
            result=fact(n1)
            return render(request,"app1/index.html",{'param1':result, 'param2':n1, 'form':form1})
    else:
        form1=inputform()  
    return render(request,"app1/index.html",{'param1':result, 'param2':n1, 'form':form1})
    
def fact(n1):  
    result=1
    for i in range(1,n1+1,1):
        result=result*i
    return result
    
    