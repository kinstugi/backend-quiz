from django.core.management.base import BaseCommand
from unidecode import unidecode
from location.models import Country, City, Airport


class Command(BaseCommand):

    def handle(self, *args, **options):
        for location in Country.objects.all():
            location.search_text = f"{unidecode(location.name)}"
            location.save()

        for city in City.objects.all():
            city.search_text = unidecode(f"{city.name}, {city.country.name}")
            city.save()

        for airport in Airport.objects.all():
            airport.search_text = unidecode(f"{airport.name}, {airport.city.name}, {airport.country.name}")
            airport.save()