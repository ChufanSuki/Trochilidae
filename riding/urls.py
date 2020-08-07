from riding.api import views as api_views
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter()
router.register(r'current', api_views.RidingViewSet, basename="current riding")
router.register(r'history', api_views.RidingHisViewSet, basename="riding history")
router.register(r'stat', api_views.RidingStatViewSet, basename="riding statistics")
urlpatterns = [
    path('api/', include(router.urls)),
]