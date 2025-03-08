from django.shortcuts import render,HttpResponse
from .models import Employee 
# Create your views here.
def index(request):
    return render(request,'index.html')

def all_emp(request):
    emps=Employee.objects.all()
    context={
        'emps':emps

    }
    print(context)
    return render(request,'view_all_emp.html',context)

def add_emp(request):
    if request.method=='POST':
       First_name=request.POST['First_name']
       Last_name=request.POST['Last_name']
       Dept=request.POST['Dept']
       newemp=Employee(First_name=First_name,Last_name=Last_name,Dept=Dept)
       newemp.save()
       return HttpResponse("Added successfully")
    else:
        print("hey")
        return render(request,'add_emp.html')

def remove_emp(request):
    return render(request,'remove_emp.html')

def filter_emp(request):
    return render(request,'filter_emp.html')



