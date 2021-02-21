from django.contrib import admin
from .models import Reports, District
from leaflet.admin import LeafletGeoAdmin


class ReportsAdmin(LeafletGeoAdmin):
    list_display =('name', 'point')


class DistrictAdmin(LeafletGeoAdmin):
    list_display = ('district', 'dist_id')

admin.site.register(Reports, ReportsAdmin)
admin.site.register(District, DistrictAdmin)