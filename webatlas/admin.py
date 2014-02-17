
from django.contrib.gis import admin
from filer.admin.fileadmin import FileAdmin
from webatlas.models import Place
from olwidget.admin import GeoModelAdmin

class MyGeoAdmin(GeoModelAdmin):
    options = {
        'layers': ['google.physical'],
        'default_lat': 64,
        'default_lon': -135,
	'zoom_to_data_extent': True,
	'default_zoom': 11,
    }

admin.site.register(Place, MyGeoAdmin)

