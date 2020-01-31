from django.http import Http404, JsonResponse
from django.forms.models import model_to_dict
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from invoice.models import Invoice
from company.models import Company
from .serializers import PaymentSerializer
from .models import Payment
from .forms import CreatePaymentForm2


class PaymentViewSet(viewsets.ModelViewSet):

	serializer_class = PaymentSerializer

	def get_queryset(self):
		company = self.request.user.company
		return Payment.objects.filter(company=company)

	def destroy(self, request, *args, **kwargs):
		invoice_id = request.POST.get('invoice_id')
		try:
			instance = self.get_object()
			self.perform_destroy(instance)
		except Http404:
			pass
		payments = PaymentSerializer(Invoice.objects.get(id=invoice_id).paid_sum.all(), many=True)
		return Response(payments.data)


	def perform_create(self, serializer):
		payment = serializer.save(company=self.request.user.company)
		invoice = Invoice.objects.get(id=self.request.POST.get('invoice_id'))
		invoice.paid_sum.add(payment)
		return Response(model_to_dict(payment))