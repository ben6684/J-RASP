
import datetime
from django import forms
from django.db.models import Q
from JRASP.models import *
from django.template.defaultfilters import filesizeformat
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import get_object_or_404

######SOME UTILITIES FONCTIONS THAT CAN BE USED IN ALL THE FORMS ######


class filesize(str):
	"""
	Class that enable to transform '2.5MB' in bits size :
		print filesize('2.5MB').bytesize() # 2621440
		print filesize(1024).bytesize() # 1024
		print filesize('1024KB').bytesize() # 1048576
	"""
	SUFFIXES = ['KB','MB','GB','TB','PB','EB','ZB','YB'] 
	def bytesize(self):
		try:
			exp = self.SUFFIXES.index(self.__str__()[-2:])
			return int(float(self.__str__()[:-2])*1024**(exp+1)) 
		except ValueError:
			return self

class ContentTypeRestrictedFileField(forms.FileField):
    """
    Same as FileField, but you can specify:
        * content_types - list containing allowed content_types. Example: ['application/pdf', 'image/jpeg']
        * max_upload_size - a number indicating the maximum file size allowed for upload.
            2.5MB - 2621440
            5MB - 5242880
            10MB - 10485760
            20MB - 20971520
            50MB - 5242880
            100MB 104857600
            250MB - 214958080
            500MB - 429916160
    """
    def __init__(self, *args, **kwargs):
        self.content_types = kwargs.pop("content_types")
        self.max_upload_size = kwargs.pop("max_upload_size")

        super(ContentTypeRestrictedFileField, self).__init__(*args, **kwargs)

    def clean(self, *args, **kwargs):        
        data = super(ContentTypeRestrictedFileField, self).clean(*args, **kwargs)
	if data:
		file = data.file
		try:
			content_type = file.content_type
			if content_type in self.content_types:
				if file._size > self.max_upload_size:
					raise forms.ValidationError(_('Please keep filesize under %s. Current filesize %s') % (filesizeformat(self.max_upload_size), filesizeformat(file._size)))
			else:
				raise forms.ValidationError(_('Filetype not supported.'))
		except AttributeError:
			pass        
            
		return data

#### FORMULARS ####
class FeedbackForm(forms.Form):
	title = forms.CharField(max_length=2000, label='Title')
	author = forms.CharField(max_length=2000, label='Name')
	slug = forms.CharField(max_length=500000,widget=forms.Textarea(),label='Comment')
	

class ArticleForm(forms.Form):
	title  = forms.CharField(max_length=2000, label='Title')
	author = forms.CharField(max_length=2000, label='Authors')
	abstract  = forms.CharField(max_length=500000,widget=forms.Textarea(),label='Abstract')
	KW = forms.CharField(max_length=2000, label='Keywords')
	example = forms.CharField(max_length=500000,widget=forms.Textarea(),label='HTML field example')

