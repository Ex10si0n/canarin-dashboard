from django.urls import path
from . import views

urlpatterns = [
    path('node/<str:node>/', views.home, name='home'),
    path('node/<str:node>/<str:start>/<str:end>/', views.hometime, name='hometime'),
    path('', views.HomePageView.as_view(), name='homepage'),
    path('data_upload/', views.data_upload, name='data_upload'),
    path('map/', views.MapView.as_view(), name='map'),
    path('raw_data/', views.RawDataView.as_view(), name='raw_data'),
]