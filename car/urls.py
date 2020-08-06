from django.urls import path
from . import views
from car.api import views as api_views

urlpatterns = [
    path('', views.index, name='index'),
    path('models/', views.ModelListView.as_view(), name="models"),
    path('model/<int:pk>', views.ModelDetailView.as_view(), name='model-detail'),
    path('mycars/', views.UsedCarsByUserListView.as_view(), name='my-car'),
    path('mycars/', views.UsedCarsByUserListView.as_view(), name='my-car'),
    path('borrowed/', views.UsedCarsAllListView.as_view(), name='all-used'),
    path('api/', api_views.ModelListCreateAPIView.as_view(), name='model_rest_api'),
    path('api/<uuid:uuid>', api_views.ModelListCreateAPIView.as_view(), name='model_rest_api'),
]