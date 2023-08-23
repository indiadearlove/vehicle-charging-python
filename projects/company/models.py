from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100)
    brand_colour_main = models.CharField(max_length=255, null=True, blank=True)
    brand_colour_secondary = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, default="GB", blank=False)
    currency = models.CharField(max_length=255, default="GBP", blank=False)

    # Other possible fields
    # logo = models.FileField(upload_to="company_logos", null=True, blank=True)

    def __str__(self):
        return self.name
