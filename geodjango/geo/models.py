from django.contrib.auth.models import User
from django.contrib.gis.db import models as geo_models
from django.db import models
# from rest_framework.authtoken.models import Token

# for user in User.objects.all():
#     Token.objects.get_or_create(user=user)


class WorldBorder(geo_models.Model):
    # Regular Django fields corresponding to the attributes in the
    # world borders shapefile.
    name = models.CharField(max_length=50)
    area = models.IntegerField()
    pop2005 = models.IntegerField('Population 2005')
    fips = models.CharField('FIPS Code', max_length=2)
    iso2 = models.CharField('2 Digit ISO', max_length=2)
    iso3 = models.CharField('3 Digit ISO', max_length=3)
    un = models.IntegerField('United Nations Code')
    region = models.IntegerField('Region Code')
    subregion = models.IntegerField('Sub-Region Code')
    lon = models.FloatField()
    lat = models.FloatField()

    # GeoDjango-specific: a geometry field (MultiPolygonField), and
    # overriding the default manager with a GeoManager instance.
    mpoly = geo_models.MultiPolygonField()
    objects = geo_models.GeoManager()

    # Returns the string representation of the model.
    def __str__(self):              # __unicode__ on Python 2
        return self.name


class Marker(geo_models.Model):
    description = models.CharField(max_length=255, default="")
    point = geo_models.PointField()
    objects = geo_models.GeoManager()

    def __str__(self):
        return self.description


class Game(models.Model):
    name = models.CharField(max_length=255, default='unnamed')


class RiskProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='risk_profile')
    game = models.ForeignKey(Game, related_name='users', null=True)

    def __str__(self):
        return self.user.username


class MunicipalityOwner(models.Model):
    user = models.ForeignKey(User)
    game_id = models.ForeignKey(Game)
    army_count = models.PositiveIntegerField()

    def __str__(self):
        return self.user.username


class Municipality(geo_models.Model):
    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(MunicipalityOwner, related_name='municipality',
                              null=True)
    mpoly = geo_models.MultiPolygonField(srid=28992)

    objects = geo_models.GeoManager()

    @property
    def center(self):
        return self.mpoly.centroid

    def __str__(self):
        return self.name

    def get_adjacent_municipalities(self):
        return Municipality.objects.filter(mpoly__touches=self.mpoly)

    def is_adjacent_to(self, lookup_id):
        adjacent_municipalities = self.get_adjacent_municipalities()
        for municipality in adjacent_municipalities:
            if municipality.pk == lookup_id:
                return True
        return False
