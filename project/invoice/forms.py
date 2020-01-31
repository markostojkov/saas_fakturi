from django import forms
from .models import Invoice


class CreateInvoiceForm(forms.ModelForm):

	class Meta:
		model = Invoice
		fields = ['company', 'customer', 'id_number','slug', 'date_created', 'payment_due', 'place', 
		'notes', 'items', 'invoice_sum', 'tax_sum', 'full_sum', 'currency']