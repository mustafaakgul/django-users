from django.forms import ModelForm
from .models import *
class EmployeeAddForm(ModelForm):
	class Meta:
		model = Employee

		exclude = [
			'user'
		]

