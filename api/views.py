from rest_framework import viewsets, permissions

from patents.models import Patent
from .serializers import PatentSerializer


class PatentListViewset(viewsets.ModelViewSet):
    queryset = Patent.objects.all().order_by('publication_number')
    serializer_class = PatentSerializer
    permission_classes = [permissions.IsAuthenticated]
	