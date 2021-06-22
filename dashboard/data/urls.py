from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('data_upload/', views.data_upload, name='data_upload'),
]