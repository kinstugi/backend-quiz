from django.db import models
from .search_utils import SearchManager

class Details(models.Model):
    name = models.CharField(max_length=280, null=False, blank=False)
    search_text = models.CharField(max_length=280, null=False, blank=False)
    search_count = models.IntegerField(null=False, blank=False)

    class Meta:
        abstract =True

    
# Create your models here.
class Country(Details):
    code = models.CharField(max_length=10)
    phone_code = models.CharField(max_length=280)
    objects = SearchManager()  # Add the custom manager

    def __str__(self) -> str:
        return f"country: {self.name}/{self.code}"
    
    def increate_search_count(self):
        self.search_count += 1
        self.save()

class City(Details):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='cities')
    objects = SearchManager()  # Add the custom manager

    def __str__(self) -> str:
        return f"city: {self.name}"
    
    def increate_search_count(self):
        self.country.increate_search_count()
        self.search_count += 1
        self.save()

class Airport(Details):
    code = models.CharField(max_length=20)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='airports')
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='airports')
    objects = SearchManager()  # Add the custom manager

    def __str__(self) -> str:
        return f"airport: {self.name}"
    
    def increate_search_count(self):
        self.city.increate_search_count()
        self.search_count += 1
        self.save()