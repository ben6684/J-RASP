# -*- coding: utf-8 -*-

# Here's the models for the new database !
# Very useful and very easy to use
# not like the former one, extracted from the Slim's one
import os
from django.db import models

class KW(models.Model):
	id_kw = models.AutoField(primary_key=True)
	nm_kw = models.CharField(max_length=500)
	class Meta:
		db_table = u'kw'
	def __unicode__(self):
		return self.nm_kw

class Skill(models.Model):
	id_skill = models.AutoField(primary_key=True)
	name_skill = models.CharField(max_length = 200)
	class Meta:
		db_table = u'skill'
	def __unicode__(self):
		return self.name_skill
	@property
	def get_skill_rate(self):
		usk = self.userskill_set.all()
		return usk[0].rate
		

class User(models.Model):
	id_user = models.AutoField( primary_key = True )
	name_user = models.CharField(max_length = 200)
	fst_name_user = models.CharField(max_length = 200)
	skill_user = models.ManyToManyField(Skill, through='UserSkill',null=True,blank=True)
	class Meta:
		db_table = u'user'
	def __unicode__(self):
		return unicode(self.fst_name_user+' '+self.name_user)
	def get_user_skills(self):
		return self.skill_user

class UserSkill(models.Model):
	id = models.AutoField(primary_key = True)
	user = models.ForeignKey(User)
	skill = models.ForeignKey(Skill)
	rate = models.IntegerField(default=0)
	class Meta:
		db_table = u'user_s_skill'
		
class File(models.Model):
	id_file = models.AutoField(primary_key=True)
	nm_file = models.CharField(max_length = 2000)
	url_file= models.CharField(max_length = 20000)
	size = models.IntegerField(null=True,blank=True)
	type_file = models.CharField(max_length = 200)
	date_creation_file = models.DateField()
	date_modification_file = models.DateField()
	number_download = models.IntegerField(default=0)
	class Meta:
		db_table = u'file'


class Article(models.Model):
	id_article = models.AutoField(primary_key=True)
	title = models.CharField(max_length = 2000)
	author = models.CharField(max_length = 5000) #contains just a string for uthor and affiliation
	reviewer = models.ManyToManyField(User, db_table='article_reviewer', related_name='article_reviewers',null=True,blank=True)
	abstract = models.CharField(max_length = 500000)
	KW = models.ManyToManyField(KW,db_table='article_kw',null=True,blank=True)
	pdf = models.ForeignKey(File,related_name='article_pdf')
	code = models.ForeignKey(File,related_name='article_code')
	example = models.CharField(max_length = 500000)
	date = models.DateField()
	views = models.IntegerField(default=0)
	class Meta:
		db_table = u'article'
		ordering = ['date']


class Feedback(models.Model):
	id_feedback = models.AutoField(primary_key=True)
	title_feedback = models.CharField(max_length = 2000)
	author = models.CharField(max_length = 2000)
	slug = models.CharField(max_length = 500000)
	date_publication = models.DateField()
	good_comment = models.IntegerField(default=0)
	article = models.ForeignKey(Article)
	class Meta:
		db_table = u'feedback'
		ordering = ['good_comment']
