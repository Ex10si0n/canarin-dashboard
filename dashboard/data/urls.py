from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('data_upload/', views.data_upload, name='data_upload'),
    path('raw_data/', views.RawDataView.as_view(), name='raw_data'),
]