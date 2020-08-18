  
from django.urls import path, include
from rest_framework import routers

from .views import PatentListViewset, PatentListAPIView, PatentDetailAPIView, PatentCreateAPIView, PatentUpdateAPIView, PatentDeleteAPIView


router = routers.DefaultRouter()
router.register('patents', PatentListViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('list/', PatentListAPIView.as_view(), name='api_list'),
    path('list/<str:pk>/', PatentDetailAPIView.as_view(), name='api_detail'),
    path('new/', PatentCreateAPIView.as_view(), name='api_new'),
    path('list/<str:pk>/edit/', PatentUpdateAPIView.as_view(), name='api_edit'),
    path('list/<str:pk>/delete/', PatentDeleteAPIView.as_view(), name='api_delete')
]