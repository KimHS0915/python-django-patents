import csv

from django.http import HttpResponse
from django.contrib import admin
from rangefilter.filter import DateRangeFilter

from .models import Patent

# Register your models here.
@admin.register(Patent)
class PatentAdmin(admin.ModelAdmin):
    list_display = [
        'publication_number',
        'title',
        'assignee',
        'filing_date',
    ]
    list_display_links = ['publication_number', 'title']
    list_filter = ('country_code', ('filing_date', DateRangeFilter),)
    search_fields = ['title', 'abstract', 'claims']
    list_per_page = 20
    actions = ['export_as_csv']

    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response
