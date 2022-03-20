from django.shortcuts import render,HttpResponseRedirect
from . models import *

def home(request):
    Data = Employee.objects.all()
    return render(request,'index.html',{'data':Data})


def add(request):
    if request.method == "POST":
        e = Employee()
        e.name = request.POST.get('Name')
        e.email = request.POST.get('Email')
        e.salary = request.POST.get('Salary')
        e.dsg = request.POST.get('Designation')
        e.city = request.POST.get('City')
        e.state = request.POST.get('State')
        # print(e.name)
        e.save()
        return HttpResponseRedirect('/')
    return render(request,'add.html')


def update(request,id):
    e = Employee.objects.get(id = id)
    if request.method == "POST":
        # e = Employee.objects.get(id = id)
        e.name = request.POST.get('Name')
        e.email = request.POST.get('Email')
        e.salary = request.POST.get('Salary')
        e.dsg = request.POST.get('Designation')
        e.city = request.POST.get('City')
        e.state = request.POST.get('State')
        # print(e.name)
        e.save()
        return HttpResponseRedirect('/')
    return render(request,'update.html',{'data':e})


def delete(request,id):
    record = Employee.objects.get(id = id)
    record.delete()
    return HttpResponseRedirect('/')
