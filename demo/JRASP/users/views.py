# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404, redirect, HttpResponseRedirect, HttpResponse
from django import forms
from django.template import RequestContext

from JRASP.models import *

def users(request):
	
	users=User.objects.all()
	return render_to_response('users/users.html', {'users' : users} ,context_instance=RequestContext(request))
