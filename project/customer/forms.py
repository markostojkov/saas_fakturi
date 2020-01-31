from django import forms
from .models import Customer


class CreateCustomerForm(forms.ModelForm):

	class Meta:
		model = Customer
		fields = ['name', 'email', 'phone', 'address', 'tax_no']