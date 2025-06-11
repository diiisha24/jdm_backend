from django.db import models
from uuid import uuid4

# Create your models here.
class Sector(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class SectorLogo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    sector = models.ForeignKey(Sector, related_name='logos', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='customer_logo/sector_wise/')
    alt_text = models.CharField(max_length=255, default="alt text")

class Country(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class SubCountry(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    country = models.ForeignKey(Country, related_name='subcountries', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.country.name} - {self.name}"

class CountryLogo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    subcountry = models.ForeignKey(SubCountry, related_name='logos', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='customer_logo/country_wise/', default="alt text")
    alt_text = models.CharField(max_length=255)