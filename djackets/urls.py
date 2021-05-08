
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

import debug_toolbar
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken')),
    path('api/v1/', include('product.urls')),
    path('api/v1/', include('order.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


