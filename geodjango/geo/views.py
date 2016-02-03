from django.contrib.auth.models import User
from django.contrib.gis.geos import Point, Polygon
from django.http import Http404, JsonResponse
from geo import models, serializers
# from geo.permissions import UserInGamePermission
from random import randrange
from rest_framework import generics, permissions
from rest_framework.response import Response


class MunicipalityList(generics.ListCreateAPIView):
    queryset = models.Municipality.objects.all()
    serializer_class = serializers.MunicipalitySerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class MunicipalityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Municipality.objects.all()
    serializer_class = serializers.MunicipalitySerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class MunicipalityOwnerList(generics.ListCreateAPIView):
    queryset = models.MunicipalityOwner.objects.all()
    serializer_class = serializers.MunicipalityOwnerSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class MunicipalityOwnerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.MunicipalityOwner.objects.all()
    serializer_class = serializers.MunicipalityOwnerSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class GameList(generics.ListCreateAPIView):
    queryset = models.Game.objects.all()
    serializer_class = serializers.GameSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,
    #                       UserInGamePermission)


class GameDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Game.objects.all()
    serializer_class = serializers.GameSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class UserDetail(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class AdjacentList(generics.ListAPIView):
    serializer_class = serializers.MunicipalitySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        municipality = serializers.Municipality.objects.get(
            pk=self.kwargs[self.lookup_field])
        queryset = municipality.get_adjacent_municipalities()
        return queryset


class IsAdjacent(generics.RetrieveAPIView):
    queryset = models.Municipality.objects.all()
    serializer_class = serializers.MunicipalitySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get(self, request, *args, **kwargs):
        municipality = self.get_object()
        is_adjacent = municipality.is_adjacent_to(int(kwargs.pop('to')))
        return Response(is_adjacent)


def get_country(request, lat, lon):
    pnt = Point(float(lon), float(lat))
    country = models.WorldBorder.objects.get(mpoly__intersects=pnt)

    if not country:
        raise Http404("No country found.")

    country_json = {
        "name": country.name
    }

    return JsonResponse(country_json)


def get_random_country_name(request):
    count_countries = models.WorldBorder.objects.count()
    country_id = randrange(count_countries)
    country = models.WorldBorder.objects.get(pk=country_id)
    return JsonResponse(country)


def get_countries_in_rectangle(request, north, east, south, west):
    bbox = (west, south, east, north)
    geom = Polygon.from_bbox(bbox)
    countries = models.WorldBorder.objects.filter(mpoly__intersects=geom)

    countries_list = []

    for country in countries:
        countries_list.append(country.name)

    return JsonResponse(countries_list, safe=False)


def get_markers(request):
    markers = models.Marker.objects.all()
    markers_list = []
    for marker in markers:
        markers_list.append({
            "description": marker.description,
            "lat": marker.point.y,
            "lon": marker.point.x
        })
    return JsonResponse(markers_list, safe=False)
