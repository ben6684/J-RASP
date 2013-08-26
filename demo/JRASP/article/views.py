# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404, redirect, HttpResponseRedirect, HttpResponse
from django import forms
from django.template import RequestContext

from JRASP.models import *
from JRASP.forms import FeedbackForm

import datetime

def articles(request):
	"""
	Show all the articles into some fancy way 
	"""
	articles = Article.objects.all()
	return render_to_response('article/articles.html',{'articles': articles,}, context_instance=RequestContext(request))


def article(request, id_article):
	"""
	Show all the information about an article
	id_article : as the name indicates, it is the id of the article you want to see
	"""
	article = get_object_or_404(Article, id_article = id_article)
	article.views = article.views + 1
	article.save()
	if request.method=='POST': #a comment is send
		form = FeedbackForm(request.POST)
		if form.is_valid():
			date= datetime.date.today()
			fb = Feedback(title_feedback = form.cleaned_data['title'], author = form.cleaned_data['author'], slug=form.cleaned_data['slug'],date_publication=date,article=article)
			fb.save()
		else:
			#error
			return render_to_response('article/article.html',{'article': article,'form':form,'error_message':form.errors }, context_instance=RequestContext(request))
	
	# the usual way to show this page 
	form = FeedbackForm()
	return render_to_response('article/article.html',{'article': article,'form':form}, context_instance=RequestContext(request))

def add_comment(request):
	"""
	just count the good comment of a feedback
	"""
	html=""
	if request.GET.has_key('id_fb'):
		id_fb = int(request.GET['id_fb'])
		fb = get_object_or_404(Feedback,id_feedback=id_fb)
		fb.good_comment = fb.good_comment + 1
		fb.save()
		html=unicode(fb.good_comment)
	return HttpResponse(html)
	

