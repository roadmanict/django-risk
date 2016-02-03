from django.contrib.gis import admin
from geo import models


class WorldBorderAdmin(admin.GeoModelAdmin):
    list_display = ('name', 'pop2005', 'fips', 'iso2', 'iso3', 'lon', 'lat')


admin.site.register(models.WorldBorder, WorldBorderAdmin)
admin.site.register(models.Marker, admin.GeoModelAdmin)
admin.site.register(models.Municipality, admin.GeoModelAdmin)
admin.site.register(models.MunicipalityOwner, admin.GeoModelAdmin)
admin.site.register(models.Game, admin.GeoModelAdmin)
admin.site.register(models.RiskProfile, admin.GeoModelAdmin)
