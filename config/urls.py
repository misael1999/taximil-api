"""Main URLs module."""

from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework.routers import DefaultRouter
# Devices FCM
router = DefaultRouter()

urlpatterns = [
    # Django Admin
    path('', include('swagger_ui.urls')),
    path(settings.ADMIN_URL, admin.site.urls),
    # Devices FCM
    path('', include(router.urls)),
    #  Apps Urls
    # Users
    path('', include('taximil.apps.users.urls')),
    # Common
    path('', include('taximil.apps.common.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
