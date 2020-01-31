from django.urls import path
from .views import InvoiceListView, InvoiceDetailView, InvoiceUpdate, InvoiceCreate, InvoicePrintView
from .api import InvoiceViewSet
from rest_framework import routers

urlpatterns = [
    path('', InvoiceListView.as_view(), name='invoices'),
    path('view/<str:slug>', InvoiceDetailView.as_view(), name='detail_invoice'),
    path('view/<str:slug>/edit', InvoiceUpdate.as_view(), name='edit_invoice'),
    path('view/<str:slug>/print', InvoicePrintView.as_view(), name='print_invoice'),
    path('create', InvoiceCreate.as_view(), name='create_invoice'),
]

router = routers.SimpleRouter()
router.register(r'get-invoice', InvoiceViewSet)

urlpatterns += router.urls
