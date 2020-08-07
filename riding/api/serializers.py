from rest_framework import serializers
from ..models import Riding_Info, Riding_His_Info, Riding_Statistics

class RidingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Riding_Info
        fields = '__all__'
        read_only_fields = ['uuid', 'created', 'modified']

class RidingHisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Riding_His_Info
        fields = '__all__'
        read_only_fields = ['uuid', 'created', 'modified']

class RidingStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Riding_Statistics
        fields = '__all__'
        read_only_fields = ['uuid', 'created', 'modified']
