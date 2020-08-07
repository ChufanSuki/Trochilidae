from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from ..models import Car_Model, Car_Check, Car_User
from .serializers import ModelSerializer, CheckSerializer, CustomerSerializer
from rest_framework import viewsets
from rest_access_policy import AccessPolicy

class ModelAccessPolicy(AccessPolicy):
    statements = [
        {
            "action": ["list", "retrieve"],
            "principal": "*",
            "effect": "allow"
        },
        {
            "action": ["add", "delete"],
            "principal": ["group:"],
            "effect": "allow"            
        }
    ]

class ModelViewSet(viewsets.ModelViewSet):
    queryset = Car_Model.objects.all()
    permission_classes = (IsAuthenticated, )
    serializer_class = ModelSerializer
    lookup_field = 'uuid'

class CheckViewSet(viewsets.ModelViewSet):
    queryset = Car_Check.objects.all()
    permission_classes = (IsAuthenticated, )
    serializer_class = CheckSerializer
    lookup_field = 'uuid'

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Car_User.objects.all()
    permission_classes = (IsAuthenticated, )
    serializer_class = CustomerSerializer
    lookup_field = 'uuid'