from rest_framework import routers
from .api import PaymentViewSet

router = routers.DefaultRouter()
router.register('get-payment', PaymentViewSet, 'payment')

urlpatterns = router.urls