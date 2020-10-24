""" Common URLs module."""
from django.urls import path, include
# Django rest frameworks
from rest_framework.routers import DefaultRouter
# Views
from taximil.apps.common import views as view_set

router = DefaultRouter()
# router.register(r'api/v1/commons', view_set.StatusViewSet, basename='common')
# router.register(r'api/v1/commons/categories', view_set.CategoryMerchantViewSet, basename='common-categories')
# # router.register(r'api/v1/commons/notifications', view_set.StatusViewSet, basename='notifications')
# router.register(r'api/v1/commons/addresses', view_set.RecommendationsAddressesViewSet,
#                 basename='common-addresses')

urlpatterns = [
    # Users
    path('', include(router.urls))
]
