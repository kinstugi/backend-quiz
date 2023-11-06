from django.http import JsonResponse
from rest_framework import views
from django.db.models import Sum
from location.models import Country, City, Airport
from .serializers import CountrySerializer, CitySerializer, AirportSerializer
from unidecode import unidecode

class SearchEndpoint(views.APIView):
    def get(self, request):
        query = request.query_params.get('query')

        if query is None:
            return JsonResponse({'error': 'Query parameter is required.'}, status=400)

        country_results = Country.objects.search(query=query).all()[:20]
        city_results = City.objects.search(query=query).all()[:20]
        airport_results = Airport.objects.search(query=query).all()[:20]
        
        results = []
        results += CountrySerializer(country_results, many=True).data
        results += CitySerializer(city_results, many=True).data
        results += AirportSerializer(airport_results, many=True).data

        return JsonResponse({'results': results})

class SelectEndpoint(views.APIView):
    def post(self, request):
        model = request.data.get('model')
        id = request.data.get('id')
        
        if model is None:
            return JsonResponse({'error': 'Model field is required.'}, status=400)
        model = model.lower()

        if id is None:
            return JsonResponse({'error': 'ID field is required.'}, status=400)
        models_map = {"city": City, "country": Country, "airport": Airport}
        try:
            location = models_map[model].objects.get(id=id)
        except :
            return JsonResponse({'error': 'Location does not exist.'}, status=404)
        location.increate_search_count()
        
        response = JsonResponse({'success': True}, json_dumps_params={'ensure_ascii': False}, content_type='application/json; charset=utf-8')
        response.set_cookie('selected_location', unidecode(f'{location.name}:{id}'))
        return response

class DeselectEndpoint(views.APIView):
    def get(self, request):
        response = JsonResponse({'success': True})
        response.delete_cookie('selected_location')
        return response


class CountryMostSearchedCities(views.APIView):
    def get(self, request):
        country_codes = request.query_params.get('country_codes')

        if country_codes is None:
            return JsonResponse({'error': 'Country codes parameter is required.'}, status=400)

        country_codes = country_codes.split(',')

        cities = []
        for country_code in country_codes:
            country = Country.objects.get(code=country_code)
            city_results = City.objects.filter(country_id=country.id).order_by('-search_count')[:5]
            cities.append({
                'country_code': country_code,
                'cities': CitySerializer(city_results, many=True).data
            })

        return JsonResponse({'cities': cities})


class CountrySearchRatio(views.APIView):
    def get(self, request):
        country_codes = request.query_params.get('country_codes')

        if country_codes is None:
            return JsonResponse({'error': 'Country codes parameter is required.'}, status=400)

        country_codes = country_codes.split(',')
        countries = []

        for country_code in country_codes:
            try:
                country = Country.objects.get(code=country_code)
                city_search_count = City.objects.filter(country_id=country.id).aggregate(search_count=Sum('search_count'))['search_count']
                airport_search_count = Airport.objects.filter(country_id=country.id).aggregate(search_count=Sum('search_count'))['search_count']
                ratio = city_search_count / airport_search_count if airport_search_count else 0

                countries.append({
                    'country_code': country_code,
                    'name': country.name,
                    'ratio': ratio
                })
            except Country.DoesNotExist:
                return JsonResponse({'error': f'Country with code {country_code} does not exist.'}, status=404)

        return JsonResponse({'countries': countries})