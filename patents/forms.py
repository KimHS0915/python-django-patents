from django import forms

from .models import Patent


class PatentCreateForm(forms.ModelForm):

    class Meta:
        model = Patent
        fields = ('publication_number', 'title', 'abstract', 'claims')

class PatentUpdateForm(forms.ModelForm):

    class Meta:
        model = Patent
        fields = ('title', 'abstract', 'claims')
