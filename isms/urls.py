from isms.api import views as api_views
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter()
router.register(r'image_info', api_views.ImageViewSet, basename="image info")
urlpatterns = [
    path('api/', include(router.urls)),
]