from django.conf.urls import patterns, include, url
from django.views.static import *
from django.conf import settings
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', 'index.views.index', name='idx'),
    url(r'^guideline/$', 'index.views.author_guideline', name='author_guideline'),
    (r'^users/', include('users.urls')),
    (r'^article/', include('article.urls')),
    (r'^util/', include('util.urls')),
    (r'^add_article/', include('add_article.urls')),

    # url(r'^$', 'JRASP.views.home', name='home'),
    # url(r'^JRASP/', include('JRASP.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
		(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)
