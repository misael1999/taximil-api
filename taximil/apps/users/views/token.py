# Django rest framework
from rest_framework_simplejwt.views import TokenObtainPairView
# Serializers
from taximil.apps.users.serializers.token import AdminTokenObtainPairSerializer
import json
# Views


class AdminTokenObtainPairView(TokenObtainPairView):
    serializer_class = AdminTokenObtainPairSerializer

