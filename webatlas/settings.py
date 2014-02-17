# Django settings for webatlas project.
# -*- coding: utf-8 -*-
import os
gettext = lambda s: s
PROJECT_PATH = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'betty',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'dawson',
        'PASSWORD': 'dawson',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

ALLOWED_HOSTS = ['*']

TIME_ZONE = 'Canada/Yukon'

LANGUAGE_CODE = 'en-us'

LANGUAGES = [ 
('en-us', 'English'),
]

SITE_ID = 1

USE_I18N = False

USE_L10N = True

USE_TZ = True

MEDIA_ROOT = os.path.join(PROJECT_PATH, "media")
MEDIA_URL = "/media/"

STATIC_ROOT = os.path.join(PROJECT_PATH, "static")
STATIC_URL = "/static/"

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    'local-static','bower_components'
)


TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH, "templates"),
)

CMS_TEMPLATES = (
    ('base.html', 'Base Template'),
    ('base_map.html','Map Template'),
    ('test.html','Test Template'),
    ('template_main.html','Atlas Template'),
    ('template_base.html','Atlas Base'),
)
# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'h@j#7g3u12aqs7%e!63k!n^%&c=2i=m#6ykgf$4o_dwsk1dn@0'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
'cms.middleware.page.CurrentPageMiddleware',
'cms.middleware.user.CurrentUserMiddleware',
'cms.middleware.toolbar.ToolbarMiddleware',
'cms.middleware.language.LanguageCookieMiddleware',
)

ROOT_URLCONF = 'webatlas.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'webatlas.wsgi.application'


TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'cms.context_processors.media',
    'sekizai.context_processors.sekizai',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
'cms',     # django CMS itself
'mptt',    # utilities for implementing a modified pre-order traversal tree
'menus',   # helper for model independent hierarchical website navigation
'south',   # intelligent schema and data migrations
'sekizai', # for javascript and css management
 'filer',
'easy_thumbnails',
'cms.plugins.text',
'cms.plugins.picture',
'cmsplugin_filer_file',
'cmsplugin_filer_folder',
'cmsplugin_filer_image',
'cmsplugin_filer_teaser',
'cmsplugin_filer_video',
'leaflet',
'djgeojson',
# 'osm',
'webatlas',
'awesome_bootstrap',
'olwidget',
)

LEAFLET_CONFIG = {
#   'SPATIAL_EXTENT' : (-145.0, 54.0, -135, 84),
   'DEFAULT_CENTER': (66.6,-145.0),
   'DEFAULT_ZOOM' : 4,
   'ATTRIBUTION_PREFIX': 'Powered by GeoPrism'
  
}


THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    #'easy_thumbnails.processors.scale_and_crop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


SERIALIZATION_MODULES = {
	'geojson': 'djgeojson.serializers'
}

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
