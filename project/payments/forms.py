from django import forms
from .models import Payment


class CreatePaymentForm(forms.ModelForm):

	class Meta:
		model = Payment
		fields = ['amount']


class CreatePaymentForm2(forms.ModelForm):

	class Meta:
		model = Payment
		fields = ['company', 'amount']