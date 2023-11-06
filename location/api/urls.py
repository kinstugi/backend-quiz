from django.urls import path

from .views import SearchEndpoint, SelectEndpoint, DeselectEndpoint, CountryMostSearchedCities, CountrySearchRatio

urlpatterns = [
    path('locations/search/', SearchEndpoint.as_view(), name='location-search'),
    path('locations/select/', SelectEndpoint.as_view(), name='location-select'),
    path('locations/deselect/', DeselectEndpoint.as_view(), name='location-deselect'),
    path('locations/country-most-searched-cities/', CountryMostSearchedCities.as_view(), name='country-most-searched-cities'),
    path('locations/country-search-ratio/', CountrySearchRatio.as_view(), name='country-search-ratio'),
]
