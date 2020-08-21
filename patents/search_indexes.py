import datetime

from haystack import indexes

from patents.models import Patent


class PatentIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(
        document=True, use_template=True, template_name='search/patent_text.txt')
    publication_number = indexes.CharField(model_attr='publication_number')
    filing_date = indexes.DateTimeField(model_attr='filing_date')

    def get_model(self):
        return Patent

    def index_queryset(self, using=None):
        return self.get_model().objects.all() 