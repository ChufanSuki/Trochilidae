from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('models/', views.ModelListView.as_view(), name="models"),
    path('model/<int:pk>', views.ModelDetailView.as_view(), name='model-detail'),
]