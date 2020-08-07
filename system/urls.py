from system.api import views as api_views
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter()
router.register(r'config', api_views.ConfigViewSet, basename="system config")
router.register(r'start_img', api_views.StartImgViewSet, basename="startup image")
router.register(r'sms', api_views.SmsViewSet, basename="Sms code")
urlpatterns = [
    path('api/', include(router.urls)),
]