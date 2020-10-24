""" Custom token serializers """
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from taximil.apps.users.models import User


class AdminTokenObtainPairSerializer(TokenObtainPairSerializer):
    default_error_messages = {'no_active_account': 'Télefono o contraseña incorrectos'}

    def validate(self, attrs):
        # Delivery man can validate their account
        data = super().validate(attrs)
        try:
            user = self.user
        except User.DoesNotExist:
            raise serializers.ValidationError({'detail': 'No tienes permisos para iniciar sesión'})

        if user.status.slug_name == 'inactive':
            raise serializers.ValidationError({'detail': 'Te han dado de baja en tu central'})

        # Add extra responses here
        # data['user'] = UserModelSerializer(self.user).data
        return data
