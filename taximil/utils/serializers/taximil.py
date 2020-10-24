from rest_framework.serializers import ModelSerializer
# Serializers
from taximil.apps.common.serializers.status import StatusModelSerializer


# Serializer with status object
class TaximilModelSerializer(ModelSerializer):
    status = StatusModelSerializer(read_only=True)
