from django.urls import path

from . import views


urlpatterns = [
    path('', views.patent_list, name='patent_list'),
    path('patent/<str:pk>/', views.patent_detail, name='patent_detail'),
    path('new/', views.patent_new, name='patent_new'),
]