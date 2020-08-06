from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from ..models import Car_Model
from .serializers import ModelSerializer

class ModelListCreateAPIView(ListCreateAPIView):
    queryset = Car_Model.objects.all()
    permission_classes = (IsAuthenticated, )
    serializer_class = ModelSerializer
    lookup_field = 'uuid'

class ModelRetrieveUpdateDestoryAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Car_Model.objects.all()
    permission_classes = (IsAuthenticated, )
    serializer_class = ModelSerializer
    lookup_field = 'uuid'
