from rest_framework import serializers
from ..models import UserProfile, MaintainerProfile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'
        read_only_fields = ['uuid', 'created', 'modified']

class MaintainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaintainerProfile
        fields = '__all__'
        read_only_fields = ['uuid', 'created', 'modified']
