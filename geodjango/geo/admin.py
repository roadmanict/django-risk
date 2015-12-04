from django.contrib.gis import admin
from .models import WorldBorder, Marker

admin.site.register(WorldBorder, admin.GeoModelAdmin)
admin.site.register(Marker, admin.GeoModelAdmin)
