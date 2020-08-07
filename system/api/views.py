from rest_framework.permissions import IsAuthenticated
from ..models import Startup_Img, Sms_Codes, System_Config
from .serializers import StartImgSerializer, SmsSerializer, ConfigSerializer
from rest_framework import viewsets
from rest_access_policy import AccessPolicy

class StartImgViewSet(viewsets.ModelViewSet):
    queryset = Startup_Img.objects.all()
    permission_classes = (IsAuthenticated, )
    serializer_class = StartImgSerializer
    lookup_field = 'uuid'

class SmsViewSet(viewsets.ModelViewSet):
    queryset = Sms_Codes.objects.all()
    permission_classes = (IsAuthenticated, )
    serializer_class = SmsSerializer
    lookup_field = 'uuid'

class ConfigViewSet(viewsets.ModelViewSet):
    queryset = System_Config.objects.all()
    permission_classes = (IsAuthenticated, )
    serializer_class = ConfigSerializer
    lookup_field = 'uuid'
