from rest_framework.permissions import IsAuthenticated
from ..models import Images_Info
from .serializers import ImageSerializer
from rest_framework import viewsets
from rest_access_policy import AccessPolicy

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Images_Info.objects.all()
    permission_classes = (IsAuthenticated, )
    serializer_class = ImageSerializer
    lookup_field = 'uuid'