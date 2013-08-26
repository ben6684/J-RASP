from django.conf.urls.defaults import *
from django.views.static import *
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('article.views',
    url(r'^$', 'articles',name='articles'),	
    url(r'^add_comment/$', 'add_comment',name='add_comment'),	
	url(r'^(?P<id_article>\w+)/$', 'article',name='article'),	
    
)
