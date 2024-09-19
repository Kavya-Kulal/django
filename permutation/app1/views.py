from django.shortcuts import render
from app1.forms import inputform
def home(request):
    if request.method=="POST":
        form1=inputform(request.POST)
        if form1.is_valid():
            data=form1.cleaned_data
            word4=data.get("name")
            result=perm4(word4)
            return render(request,'app1/index.html',{'param1':result,'form1':form1})
    else:
        form1=inputform()
    return render(request,"app1/index.html",{'form':form1})
            # Create your views here.
def perm3(word3):
    
    s3=word3
    list1=[]
    c1=s3[0:1]
    c2=s3[1:2]
    c3=s3[2:3]
    list1.append(c1+c2+c3)
    list1.append(c1+c3+c2)
    list1.append(c2+c1+c3)
    list1.append(c2+c3+c1)
    list1.append(c3+c1+c2)
    list1.append(c3+c2+c1)
    return list1

def perm4(word4):
    s4=word4
    c1=s4[0:1]
    c2=s4[1:2]
    c3=s4[2:3]
    c4=s4[3:4]
    list4=[]
    part1=c1
    part2=c2+c3+c4
    list1=perm3(part2)
    for i in range(0,6,1):
        list4.append(part1+list1[i])
    part1=c2
    part2=c1+c3+c4
    list1=perm3(part2)
    for i in range(0,6,1):
        list4.append(part1+list1[i])
    part1=c3
    part2=c1+c2+c4
    list1=perm3(part2)
    for i in range(0,6,1):
        list4.append(part1+list1[i])
    part1=c4
    part2=c1+c2+c3
    list1=perm3(part2)
    for i in range(0,6,1):
        list4.append(part1+list1[i])
    return list4