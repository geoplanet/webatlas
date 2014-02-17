from django.db import models
from filer.fields.image import FilerImageField, FilerFileField
from django.utils.translation import ugettext_lazy as _
from cms.models import CMSPlugin
from decimal import *
from django.contrib.gis.db import models as gismodels
from djgeojson.views import GeoJSONLayerView
import sys


# This is an auto-generated Django model module created by ogrinspect.

class Place(models.Model):
    fkey = models.ForeignKey('self',blank=True, null=True)
    vpoid = models.IntegerField(primary_key=True)
    interviewe = models.CharField(max_length=26)
    date_field = models.CharField(max_length=13,blank=True)
    transcribe = models.CharField(max_length=34,blank=True)
    no_field = models.IntegerField()
    place_type = models.CharField(max_length=73)
    gwich_in_n = models.CharField(max_length=34,blank=True)
    other_name = models.CharField(max_length=40,blank=True)
    meaning = models.CharField(max_length=156,blank=True)
    display = models.CharField(max_length=1)
    category = models.CharField(max_length=3)
    video = FilerFileField(null=True, blank=True, related_name="place_video")
    image = FilerImageField(null=True, blank=True, related_name="place_image")
    has_audio = models.CharField(max_length=1)
    geom = gismodels.PointField(srid=4326)
    objects = gismodels.GeoManager()

    # On Python 3: def __str__(self):
    def __unicode__(self):
        return 'Name: %s' % self.other_name

# Auto-generated `LayerMapping` dictionary for vgg_places_geographic model
place_mapping = {
    'vpoid' : 'ID',
    'interviewe' : 'INTERVIEWE',
    'date_field' : 'DATE_',
    'transcribe' : 'TRANSCRIBE',
    'no_field' : 'NO_',
    'place_type' : 'PLACE_TYPE',
    'gwich_in_n' : 'GWICH_IN_N',
    'other_name' : 'OTHER_NAME',
    'meaning' : 'MEANING',
    'display' : 'DISPLAY',
    'category' : 'CLASS',
    'has_audio' : 'HAS_AUDIO',
    'geom' : 'POINT',
}
     


class Atlas(CMSPlugin):
    title = models.CharField(_("map title"), max_length=100, blank=True, null=True)
    dataurl = models.URLField(_("data url"), max_length=150)
    zoom = models.IntegerField(_("zoom level"), blank=True, null=True)

    content = models.CharField(_("content"), max_length=1500, blank=True, null=True)

    def __unicode__(self):
        return u"%s (%s)" % (self.get_title(), self.dataurl)
    
    def get_title(self):
        return self.title or  _("Map")

    def get_content(self):
        return self.content or ""

    def get_zoom_level(self):
        return  self.zoom or 13    