from rest_framework import serializers
from ..models import Images_Info

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images_Info
        fields = '__all__'
        read_only_fields = ['uuid', 'created', 'modified']

