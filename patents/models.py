from django.db import models

class Patent(models.Model):
    publication_number = models.CharField(max_length=20, primary_key=True)
    application_number = models.CharField(max_length=20)
    country_code = models.CharField(max_length=5)
    filing_date = models.DateField(null=True)
    assignee = models.CharField(max_length=500, null=True)
    title = models.CharField(max_length=500, null=True)
    abstract = models.TextField(null=True)
    claims = models.TextField(null=True)

    class Meta:
        db_table = 'patents1000'

    def __str__(self):
        return self.publication_number
