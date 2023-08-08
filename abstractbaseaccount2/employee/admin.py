from django.contrib import admin
from . models import *

# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["employee_name",
                    "employee_email",
                    "employee_iban",
                    "created_date"]
    list_display_links = ["employee_name"]
    search_fields = ["employee_name"]
    list_filter = ["created_date"]

    class Meta:
        model = Employee