from django import forms

from .models import Patent


class PatentForm(forms.ModelForm):

    class Meta:
        model = Patent
        fields = ('publication_number', 'title', 'abstract', 'claims')
        