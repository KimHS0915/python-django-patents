from django.urls import path, include
from rest_framework import routers

from .views import PatentListViewset


router = routers.DefaultRouter()
router.register('patents', PatentListViewset)

urlpatterns = [
    path('', include(router.urls)),
]