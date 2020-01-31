from django.shortcuts import render
from tax.models import Tax
from customer.models import Customer
from invoice.models import Invoice
from .models import Company


class TaxDifferentCompany:

	def dispatch(self, request, *args, **kwargs):
		pk = kwargs.get('pk')
		if Tax.objects.get(pk=pk).company == request.user.company:
			return super().dispatch(request, *args, **kwargs)
		else:
			return render(request, 'company/403.html')

class DifferentCompany:

	def dispatch(self, request, *args, **kwargs):
		pk = kwargs.get('pk')
		if Company.objects.get(pk=pk) == request.user.company:
			return super().dispatch(request, *args, **kwargs)
		else:
			return render(request, 'company/403.html')


class CustomerDifferentCompany:

	def dispatch(self, request, *args, **kwargs):
		pk = kwargs.get('pk')
		if Customer.objects.get(pk=pk).company == request.user.company:
			return super().dispatch(request, *args, **kwargs)
		else:
			return render(request, 'company/403.html')

class InvoiceDifferentCompany:

	def dispatch(self, request, *args, **kwargs):
		slug = kwargs.get('slug')
		if Invoice.objects.get(slug=slug).company == request.user.company:
			return super().dispatch(request, *args, **kwargs)
		else:
			return render(request, 'company/403.html')


