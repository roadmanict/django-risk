import os
from os.path import isfile
import geodjango
from django.contrib.gis.utils import LayerMapping
from django.contrib.gis.gdal import DataSource
from geo.models import WorldBorder, Municipality


world_mapping = {
    'fips': 'FIPS',
    'iso2': 'ISO2',
    'iso3': 'ISO3',
    'un': 'UN',
    'name': 'NAME',
    'area': 'AREA',
    'pop2005': 'POP2005',
    'region': 'REGION',
    'subregion': 'SUBREGION',
    'lon': 'LON',
    'lat': 'LAT',
    'mpoly': 'MULTIPOLYGON',
}

world_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(
    os.path.dirname(geodjango.__file__))), 'data', 'TM_WORLD_BORDERS-0.3.shp'))


gemeente_mapping = {
    'code': 'code',
    'name': 'gemeentena',
    'mpoly': 'POLYGON'
}

gemeente_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(
    os.path.dirname(geodjango.__file__))), 'data',
    'TopGrenzen-gem-actueel.shp'))

print(gemeente_shp)
print(isfile(gemeente_shp))


def run(verbose=True):
    lm = LayerMapping(WorldBorder, world_shp, world_mapping,
                      transform=False, encoding='iso-8859-1')

    lm.save(strict=True, verbose=verbose)


def gm(verbose=True):
    ds = DataSource(gemeente_shp, encoding='iso-8859-1')
    layer = ds[0]
    print(ds)
    print(layer.fields)
    print(layer.geom_type)
    print(layer.srs)
    lm = LayerMapping(Municipality, gemeente_shp, gemeente_mapping,
                      transform=False, encoding='iso-8859-1')

    lm.save(strict=True, verbose=verbose)
