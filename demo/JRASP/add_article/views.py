# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404, redirect, HttpResponseRedirect, HttpResponse
from django import forms
from django.template import RequestContext
from django.conf import settings

from JRASP.models import *
from JRASP.forms import *

from util.views import *
from util import *

import datetime

def add_article(request):
	"""
	function that take the form of add_article and add it to the database
	"""
	if request.method == 'POST':
		form = ArticleForm(request.POST,request.FILES)
		if form.is_valid():
			#check for a pdf file
			if request.FILES.has_key('pdf'):
				pdf_file = request.FILES['pdf']
				#check extention to do ...
				date= datetime.date.today()
				pdf_f = File(nm_file=pdf_file.name,url_file="/",size=pdf_file.size,type_file='PDF',date_creation_file=date,date_modification_file=date)
				pdf_f.save()
			else:
				return render_to_response('add_article/add_article.html',{'form':form,'error_message':"Need an article for a complete submission"}, context_instance=RequestContext(request))				
			#check for the zip file 
			if request.FILES.has_key('zip'):
				zip_file = request.FILES['zip']
				#check extention to do ...
				date= datetime.date.today()
				zip_f = File(nm_file=zip_file.name,url_file="/",size=zip_file.size,type_file='ZIP',date_creation_file=date,date_modification_file=date)
				zip_f.save()
			else:
				return render_to_response('add_article/add_article.html',{'form':form,'error_message':"Need an article for a complete submission"}, context_instance=RequestContext(request))			
			#add the article objects
			a = Article(title=form.cleaned_data['title'], author=form.cleaned_data['author'],abstract=form.cleaned_data['abstract'],pdf=pdf_f,code=zip_f,example=form.cleaned_data['example'],date=date)
			a.save()
			add_kw(a,form.cleaned_data['KW'])
			
			#url:
			url = settings.MEDIA_ROOT+unicode(a.id_article)+'/'
			#then add the real url for file AND download them
			pdf_f.url_file = url+pdf_f.nm_file
			pdf_f.save()
			flag_p = management_file(pdf_file,url)
			zip_f.url_file = url+zip_f.nm_file
			zip_f.save()			
			flag_z = management_file(zip_file,url)
			if not flag_p or not flag_z:
				a.delete()
				pdf_f.delete()
				zip_f.delete()
			return redirect('idx')
		else:
			return render_to_response('add_article/add_article.html',{'form':form,'error_message':form.errors}, context_instance=RequestContext(request))	
			

	form = ArticleForm()
	return render_to_response('add_article/add_article.html',{'form':form}, context_instance=RequestContext(request))
