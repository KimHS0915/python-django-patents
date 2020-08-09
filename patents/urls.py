from django.urls import path

from . import views


urlpatterns = [
    path('', views.PatentListView.as_view(), name='patent_list'),
    path('patent/<str:pk>/', views.PatentDetailView.as_view(), name='patent_detail'),
    path('new/', views.PatentCreateView.as_view(), name='patent_new'),
    path('patent/<str:pk>/edit', views.PatentUpdateView.as_view(), name='patent_edit'),
    path('patent/<str:pk>/delete', views.PatentDeleteView.as_view(), name='patent_delete'),
]