from django.urls import path
from .views import TaxListView, TaxUpdate, TaxCreate

urlpatterns = [
    path('', TaxListView.as_view(), name='taxes'),
    path('view/edit/<int:pk>', TaxUpdate.as_view(), name='edit_tax'),
    path('create', TaxCreate.as_view(), name='create_tax'),
]
