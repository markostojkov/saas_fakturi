from django import forms
from .models import Tax


class CreateTaxForm(forms.ModelForm):

	class Meta:
		model = Tax
		fields = ['name', 'value']