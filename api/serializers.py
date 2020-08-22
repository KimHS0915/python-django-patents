from rest_framework import serializers
from drf_haystack.serializers import HaystackSerializer

from patents.models import Patent
from patents.search_indexes import PatentIndex


class PatentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patent
        fields = ['publication_number', 'title', 'abstract', 'claims']


class PatentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patent
        fields = '__all__'


class PatentIndexSerializer(HaystackSerializer):
    class Meta:
        index_classes = [PatentIndex]
        fields = ['publication_number', 'text']