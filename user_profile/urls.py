from user_profile.api import views as api_views
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter()
router.register(r'user', api_views.UserProfileViewSet, basename="current riding")
router.register(r'maintainer', api_views.MaintainerProfileViewSet, basename="riding history")
urlpatterns = [
    path('api/', include(router.urls)),
]