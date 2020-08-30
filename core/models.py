from django.db import models


class Job(models.Model):
    type = models.CharField(max_length=50)
    url = models.CharField(max_length=100)
    created_at = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    company_url = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description = models.TextField()
    how_to_apply = models.TextField()
    company_logo = models.ImageField()

