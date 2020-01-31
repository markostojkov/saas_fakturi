from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from invoice.models import Invoice
from .models import Payment


@login_required
@csrf_exempt
def delete_payment(request, **kwargs):

	payment_id = kwargs.get('pk')
	if request.method == 'POST':
		invoice_id = request.POST.get('invoice_id')
		Payment.objects.get(id=payment_id).delete()
		qs = Invoice.objects.get(id=invoice_id).paid_sum.all()
		data = list(qs.values())
		return JsonResponse(data, safe=False)
