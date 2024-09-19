from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"app1/index.html",{'param1':"Helloworld"})
def square(n):
    return n*n;