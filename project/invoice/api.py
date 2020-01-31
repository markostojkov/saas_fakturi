from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import InvoiceSerializer
from .models import Invoice


class InvoiceViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = InvoiceSerializer
    permission_classes = [IsAuthenticated]
    queryset = Invoice.objects.all()

    def get_queryset(self):
    	return Invoice.objects.filter(company=self.request.user.company)