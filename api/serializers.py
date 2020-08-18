from rest_framework import serializers
from patents.models import Patent


class PatentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patent
        fields = ['publication_number', 'title', 'abstract', 'claims']


class PatentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patent
        fields = [
            'publication_number',
            'application_number',
            'country_code',
            'filing_date',
            'assignee',
            'title',
            'abstract',
            'claims',
        ]