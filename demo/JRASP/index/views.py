# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404, redirect, HttpResponseRedirect, HttpResponse
from django import forms
from django.template import RequestContext

from JRASP.models import *

def index(request):
	"""
	Just show the index page with the informations
	"""
	articles = Article.objects.all()
	return render_to_response('index/index.html', {'articles' : articles} ,context_instance=RequestContext(request))

def author_guideline(request):
	"""
	Must be remove from index app but just for the demo : 
	It is serving the author guideline page, which is static and contains link to OJS
	"""
	return render_to_response('index/guideline.html', context_instance=RequestContext(request))
