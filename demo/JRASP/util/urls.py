from django.conf.urls.defaults import *
from django.views.static import *
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('util.views',
					   
    url(r'^download/(?P<file>\w+)/$', 'download', name='download'),		   
    url(r'^autoKW/(?P<key>\w+)/$', 'autoKW', name='autoKW'),
)
