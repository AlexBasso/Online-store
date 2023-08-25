from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("__debug__/", include("debug_toolbar.urls")),
    path("api/", include("tag.urls")),
    path("api/", include("basket.urls")),
    path("api/", include("auth_user.urls")),
    path("api/", include("product.urls")),
    path("api/", include("catalog.urls")),
    path("api/", include("order.urls")),
    path("", include("frontend.urls")),
    path("api/", include("api.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
