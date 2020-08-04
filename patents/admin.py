from django.contrib import admin

from .models import Patent

@admin.register(Patent)
class PatentAdmin(admin.ModelAdmin):
    list_display = [
        'publication_number',
        'title',
        'assignee',
        'filing_date',
    ]
    list_display_links = ['publication_number', 'title']
    list_filter = ('country_code', 'filing_date')
    search_fields = ['title', 'abstract', 'claims']
    list_per_page = 20