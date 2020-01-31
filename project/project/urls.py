from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from invoice.views import home


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='homepage'),
    path('', include('users.urls')),
    path('invoice/', include('invoice.urls')),
    path('', include('company.urls')),
    path('tax/', include('tax.urls')),
    path('customer/', include('customer.urls')),
    path('payment/', include('payments.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
