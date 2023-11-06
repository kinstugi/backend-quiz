from django.db import models
from django.db.models import Q
from unidecode import unidecode

class SearchManager(models.Manager):
    def search(self, query):
        normalized_query = unidecode(query)
        
        queryset = self.get_queryset().filter(
            Q(name__icontains=normalized_query) |
            Q(search_text__icontains=normalized_query)
        )
        return queryset