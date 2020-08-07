from rest_framework.permissions import IsAuthenticated
from ..models import Riding_Info, Riding_His_Info, Riding_Statistics
from .serializers import RidingSerializer, RidingHisSerializer, RidingStatSerializer
from rest_framework import viewsets
from rest_access_policy import AccessPolicy

class RidingViewSet(viewsets.ModelViewSet):
    queryset = Riding_Info.objects.all()
    permission_classes = (IsAuthenticated, )
    serializer_class = RidingSerializer
    lookup_field = 'uuid'

class RidingHisViewSet(viewsets.ModelViewSet):
    queryset = Riding_His_Info.objects.all()
    permission_classes = (IsAuthenticated, )
    serializer_class = RidingHisSerializer
    lookup_field = 'uuid'

class RidingStatViewSet(viewsets.ModelViewSet):
    queryset = Riding_Statistics.objects.all()
    permission_classes = (IsAuthenticated, )
    serializer_class = RidingStatSerializer
    lookup_field = 'uuid'