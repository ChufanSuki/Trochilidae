from django.urls import path, include
from . import views
from car.api import views as api_views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

router = DefaultRouter()
router.register(r'customer', api_views.CustomerViewSet, basename="customer")
router.register(r'model', api_views.ModelViewSet, basename="model")
router.register(r'check', api_views.CheckViewSet, basename="check")

urlpatterns = [
    path('', views.index, name='index'),
    path('models/', views.ModelListView.as_view(), name="models"),
    path('model/<int:pk>', views.ModelDetailView.as_view(), name='model-detail'),
    path('mycars/', views.UsedCarsByUserListView.as_view(), name='my-car'),
    path('mycars/', views.UsedCarsByUserListView.as_view(), name='my-car'),
    path('borrowed/', views.UsedCarsAllListView.as_view(), name='all-used'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/', include(router.urls)),
]