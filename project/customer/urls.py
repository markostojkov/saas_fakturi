from django.urls import path
from .views import CustomerListView, CustomerUpdate, CustomerCreate, CustomerDetailView
from .api import CustomerViewSet
from rest_framework import routers


urlpatterns = [
    path('', CustomerListView.as_view(), name='customers'),
    path('view/<int:pk>', CustomerDetailView.as_view(), name='detail_customer'),
    path('view/<int:pk>/edit', CustomerUpdate.as_view(), name='edit_customer'),
    path('create', CustomerCreate.as_view(), name='create_customer'),
]

router = routers.SimpleRouter()
router.register(r'get-customer', CustomerViewSet)

urlpatterns += router.urls

