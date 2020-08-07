from rest_framework.permissions import IsAuthenticated
from ..models import UserProfile, MaintainerProfile
from .serializers import UserSerializer, MaintainerSerializer
from rest_framework import viewsets
from rest_access_policy import AccessPolicy

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    permission_classes = (IsAuthenticated, )
    serializer_class = UserSerializer
    lookup_field = 'uuid'

class MaintainerProfileViewSet(viewsets.ModelViewSet):
    queryset = MaintainerProfile.objects.all()
    permission_classes = (IsAuthenticated, )
    serializer_class = MaintainerSerializer
    lookup_field = 'uuid'