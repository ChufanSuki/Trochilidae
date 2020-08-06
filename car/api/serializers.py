from rest_framework import serializers
from ..models import Car_Model
class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car_Model
        fields = ['name', 'img', 'code', 'state', 'uuid']