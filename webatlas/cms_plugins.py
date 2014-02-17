from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from models import Atlas
from django.utils.translation import ugettext as _

class AtlasPlugin(CMSPluginBase):
    model = Atlas
    name = _("Atlas")
    render_template = "cms/plugins/atlas.html"

    def render(self, context, instance, placeholder):
        context.update({
            'object':instance, 
            'placeholder':placeholder, 
        })
        return context
    
plugin_pool.register_plugin(AtlasPlugin)