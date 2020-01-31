from django.urls import path
from .views import CompanyUpdate

urlpatterns = [
    path('edit-company/<int:pk>', CompanyUpdate.as_view(), name='edit_company'),
]
