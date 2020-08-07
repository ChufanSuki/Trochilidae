from rest_framework import serializers
from ..models import Startup_Img, Sms_Codes, System_Config

class StartImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = Startup_Img
        fields = '__all__'
        read_only_fields = ['uuid', 'created', 'modified']

class SmsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sms_Codes
        fields = '__all__'
        read_only_fields = ['uuid', 'created', 'modified']

class ConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = System_Config
        fields = '__all__'
        read_only_fields = ['uuid', 'created', 'modified']