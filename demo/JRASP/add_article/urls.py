from django.conf.urls import *
from django.views.static import *
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('add_article.views',
    url(r'^$', 'add_article',name='add_article'),    
)
