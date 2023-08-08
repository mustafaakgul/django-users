from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import *
from django.shortcuts import render, redirect, get_object_or_404, reverse, HttpResponse

# Create your views here.

@login_required(login_url = "user:login")
def addEmployee(request):
    form = EmployeeAddForm(request.POST or None)
    context = {
        "form": form
    }

    if form.is_valid():
        employee = form.save(commit=False)
        employee.user = request.user
        employee.save()
        return redirect("employee:employeeList")
    return render(request, "employee/employeeAdd.html", context)


@login_required(login_url = "user:login")
def employeeList(request):

    employees = Employee.objects.filter(user = request.user)
    context = {
        "employees" : employees
    }
    return render(request, "employee/employeeList.html", context)