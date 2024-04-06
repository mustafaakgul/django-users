from django.contrib import admin
from django.urls import path
from . import views


app_name = "employee"


urlpatterns = [
    path("yeni/", views.addEmployee, name = "addEmployee"),

    path("", views.employeeList, name="employeeList"),



]