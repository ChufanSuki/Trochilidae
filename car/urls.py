from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('models/', views.ModelListView.as_view(), name="models"),
    path('model/<int:pk>', views.ModelDetailView.as_view(), name='model-detail'),
    path('mycars/', views.UsedCarsByUserListView.as_view(), name='my-car'),
    path('mycars/', views.UsedCarsByUserListView.as_view(), name='my-car'),
    path('borrowed/', views.UsedCarsAllListView.as_view(), name='all-used'),
]