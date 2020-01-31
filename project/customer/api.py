from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import CustomerSerializer
from .models import Customer


class CustomerViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]
    queryset = Customer.objects.all()

    def get_queryset(self):
    	return Customer.objects.filter(company=self.request.user.company)