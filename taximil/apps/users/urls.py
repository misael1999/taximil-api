"""User URLs module."""
from django.urls import path, include
# Django rest frameworks
from rest_framework.routers import DefaultRouter
# JWT
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView
# Views
from taximil.apps.users.views import users as user_view

router = DefaultRouter()
router.register(r'api/v1/users', user_view.UserViewSet, basename='users')
# router.register(r'api/v1/customers/login/facebook', CustomerFacebookAuthViewSet, basename='customers_facebook')
# router.register(r'api/v1/customers/login/apple', CustomerAppleAuthViewSet, basename='customers_apple')

urlpatterns = [
    # JWT
    # path('api/v1/customers/login/', CustomerTokenObtainPairView.as_view(), name='token_obtain_pair_customer'),
    # path('api/v1/marketing/login/', MarketingTokenObtainPairView.as_view(), name='token_obtain_pair_marketing'),
    # path('api/v1/stations/login/', StationTokenObtainPairView.as_view(), name='token_obtain_pair_stations'),
    # path('api/v1/merchants/login/', MerchantManTokenObtainPairView.as_view(), name='token_obtain_pair_merchants'),
    path('api/v1/users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/users/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # Views
    path('', include(router.urls))
]
