from django.db import models
from django.conf import settings


class Employee(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    employee_name = models.CharField(max_length=50)
    employee_email = models.CharField(max_length=50)
    employee_tckn = models.CharField(max_length=50)
    employee_iban = models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    total_balance = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)


    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.employee_name