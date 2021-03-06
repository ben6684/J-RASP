# Create your views here.
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404, redirect, HttpResponseRedirect, HttpResponse, render
from JRASP.models import KW, File

from django.db.models import Q,Max

from django.core.mail import mail_admins, send_mail

	#################################################################
####################### UTIL :  generic fonctions #######################
	#################################################################

def download(request, file):
	"""
	\brief method that get a id_file and use it to send a http response that open a download window ! very usefull, avoid a lot of security breaches.
	\author{B.Petitpas}
	\date{05/06/2012}

	"""
	if request.META.has_key('HTTP_REFERER'):
		redir = request.META['HTTP_REFERER']
	else:
		redir = 'idx'
	import os
	try:
		fil = get_object_or_404(File, id_file=file)
		if not fil:
			return redirect(redir)
		else:
			fil.number_download +=1
			fil.save()
		print fil.url_file
		if fil.url_file[0]=="/":
			my_data = open(unicode(fil.url_file))
			response = HttpResponse(my_data, content_type='text/plain')
			response['Content-Disposition'] = 'attachment; filename=%s'%os.path.basename(fil.url_file)
			return response
		elif fil.url_file[0:4]=="http":
			return HttpResponseRedirect(fil.url_file)
		else:
			return redirect(redir)
	except:
		return redirect(redir)

	
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def autoKW(request,key):
	k=key+'-KW'
	HTML=''
	if request.is_ajax() and request.POST.has_key(k):
		HTML ="<ul>"
		filt = request.POST.get(k)
		A = KW.objects.filter(nm_kw__istartswith=filt)
		for a in A:
			HTML+="""<li id="%s">%s</li>"""%(a.id_kw,a)
	return HttpResponse(HTML)

import os
def management_file(f,path):
	flag=True
	if not os.path.exists(path):
		try:
			os.makedirs(path)
		except:
			flag=False
	if flag:
		with open(path+'%s'%(f.name), 'wb+') as destination:
			for chunk in f.chunks():
				destination.write(chunk)
			destination.close()
	return flag

def add_kw(obj,kw):
	"""
	\brief{add_kw is a generic version for adding keyword to ANY kind of objects (model object)}
	\in{the object, and a list of keywords separate by a coma}
	\out{None}
	"""
	if kw:
		kw = kw.replace(';',',')
		kw = kw.split(',')
		for k in kw:
			k=k.lstrip()
			k=k.rstrip()
			K = KW.objects.filter(nm_kw__iexact=k)
			if K:
				obj.KW.add(K[0])
			else:
				kk = KW(nm_kw = k)
				kk.save()
				obj.KW.add(kk)
		obj.save()
