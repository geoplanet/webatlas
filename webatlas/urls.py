from django.conf.urls import *
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.conf import settings
from django.views.generic import TemplateView
from djgeojson.views import GeoJSONLayerView
from webatlas.models import Place

admin.autodiscover()

urlpatterns = i18n_patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^test$', TemplateView.as_view(template_name='map_cluster.html'), name='home'),
    url(r'^google$', TemplateView.as_view(template_name='google_cluster.html'), name='google'),
    url(r'^data.geojson$', GeoJSONLayerView.as_view(model=Place, properties=('other_name','gwich_in_n','place_type','image')),name='data'),
    url(r'^data.geojson$', GeoJSONLayerView.as_view(model=Place, properties=('image')),name='site_image'),
    url(r'^', include('cms.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    url(r'', include('django.contrib.staticfiles.urls')),
) + urlpatterns
