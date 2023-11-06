from django.core.management.base import BaseCommand

from location.models import Country, City, Airport
import json

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--model', type=str, help='Model type (ulke for Country, sehir for City')
        parser.add_argument('--json-file', type=str, help='Path to the JSON file to import')

    def handle(self, *args, **options):
        model_type = options['model']
        file_path = options['json_file']

        try:
            with open(file_path, 'r', encoding='utf-8') as json_file:
                data = json.load(json_file)
                if model_type == "ulke":
                    for country_data in data:
                        # Create a new Country object with the data from the JSON
                        Country.objects.create(
                            name=country_data['name'],
                            code=country_data['code'],
                            phone_code=country_data['phone_code'],
                            search_text='',
                            search_count=0
                        )
                    self.stdout.write(self.style.SUCCESS('Countries data imported successfully.'))
                elif model_type == "sehir":
                    for city in data:
                        db_country = Country.objects.get(code = city['country_code'])
                        db_city = City.objects.create(name=city['name'], country=db_country, search_text='', search_count=0)
                        for airport in city['airports']:
                            Airport.objects.create(name=airport['name'], code=airport['code'], search_text='', search_count=0, city=db_city, country=db_country)
                    self.stdout.write(self.style.SUCCESS('Cities data imported successfully.'))
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR('JSON file not found.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'An error occurred: {str(e)}'))