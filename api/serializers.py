from rest_framework import serializers
from patents.models import Patent


class PatentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patent
        fields = ['publication_number', 'title', 'abstract', 'claims']
		