from rest_framework import serializers
from .models import Invoice


class InvoiceSerializer(serializers.ModelSerializer):

	customer_name = serializers.CharField(source='customer.name')

	class Meta:
		model = Invoice
		fields = ['id', 'customer', 'customer_name', 'slug', 'id_number', 'date_created', 'payment_due', 'place', 'items', 'invoice_sum', 'tax_sum', 'full_sum', 'paid_sum', 'currency']