from rest_framework import generics, viewsets, permissions

from patents.models import Patent
from .serializers import PatentSerializer, PatentDetailSerializer


class PatentListViewset(viewsets.ModelViewSet):
    queryset = Patent.objects.all().order_by('publication_number')
    serializer_class = PatentSerializer
    permission_classes = [permissions.IsAuthenticated]


class PatentListAPIView(generics.ListAPIView):
    queryset = Patent.objects.all()
    serializer_class = PatentSerializer
    permission_classes = [permissions.IsAuthenticated]


class PatentDetailAPIView(generics.RetrieveAPIView):
    queryset = Patent.objects.all()
    serializer_class = PatentDetailSerializer
    permission_classes = [permissions.IsAuthenticated]


class PatentCreateAPIView(generics.CreateAPIView):
    queryset = Patent.objects.all()
    serializer_class = PatentDetailSerializer
    permission_classes = [permissions.IsAuthenticated]


class PatentUpdateAPIView(generics.UpdateAPIView):
    queryset = Patent.objects.all()
    serializer_class = PatentDetailSerializer
    permission_classes = [permissions.IsAuthenticated]


class PatentDeleteAPIView(generics.DestroyAPIView):
    queryset = Patent.objects.all()
    serializer_class = PatentSerializer
    permission_classes = [permissions.IsAuthenticated]