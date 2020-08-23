from django.urls import path, include
from rest_framework import routers

from .views import PatentListViewSet, PatentListAPIView, \
    PatentDetailAPIView, PatentCreateAPIView, PatentUpdateAPIView, \
    PatentDeleteAPIView, PatentSearchViewSet, PatentListFilterAPIView, \
    AutocompleteSearchViewSet


router = routers.DefaultRouter()
router.register('patents', PatentListViewset)
router.register('search', PatentSearchViewSet, base_name='patent-search')
router.register('autocomplete', AutocompleteSearchViewSet, base_name='patent-auto')

urlpatterns = [
    path('', include(router.urls)),
    path('list/', PatentListAPIView.as_view(), name='api_list'),
    path('list/<str:pk>/', PatentDetailAPIView.as_view(), name='api_detail'),
    path('new/', PatentCreateAPIView.as_view(), name='api_new'),
    path('list/<str:pk>/edit/', PatentUpdateAPIView.as_view(), name='api_edit'),
    path('list/<str:pk>/delete/', PatentDeleteAPIView.as_view(), name='api_delete'),
     path('filter/', PatentListFilterAPIView.as_view(), name='api_filter'),
]