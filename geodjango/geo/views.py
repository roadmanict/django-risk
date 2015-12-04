from django.contrib.gis.geos import Point, Polygon
from django.http import HttpResponse, Http404, JsonResponse
from random import randrange

from .models import WorldBorder, Marker


def get_country(request, lat, lon):
    pnt = Point(float(lon), float(lat))
    country = WorldBorder.objects.get(mpoly__intersects=pnt)

    if not country:
        raise Http404("No country found.")

    country_json = {
        "name": country.name
    }

    return JsonResponse(country_json)


def get_random_country_name(request):
    count_countries = WorldBorder.objects.count()
    country_id = randrange(count_countries)
    country = WorldBorder.objects.get(pk=country_id)
    return JsonResponse(country)


def get_countries_in_rectangle(request, north, east, south, west):
    bbox = (west, south, east, north)
    geom = Polygon.from_bbox(bbox)
    countries = WorldBorder.objects.filter(mpoly__intersects=geom)

    countries_list = []

    for country in countries:
        countries_list.append(country.name)

    return JsonResponse(countries_list, safe=False)


def get_markers(request):
    markers = Marker.objects.all()
    markers_list = []
    for marker in markers:
        markers_list.append({
            "description": marker.description,
            "lat": marker.point.y,
            "lon": marker.point.x
        })
    return JsonResponse(markers_list, safe=False)
