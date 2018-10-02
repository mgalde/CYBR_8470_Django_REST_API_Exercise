from __future__ import unicode_literals

from django.db import models
from django.core.validators import *

from django.contrib.auth.models import User, Group

from django.contrib import admin
import base64

class Event(models.Model):
	eventtype = models.CharField(max_length=1000, blank=False)
	timestamp = models.DateTimeField()
	userid = models.CharField(max_length=1000, blank=True)
	requestor = models.GenericIPAddressField(blank=False)

	def __str__(self):
		return str(self.eventtype)

class Dog(models.Model):
	dogname = models.CharField(max_length=1000, blank=False)
	dogage = models.DateTimeField()
	dogbreed = models.CharField(max_length=1000, blank=False)
	doggender = models.CharField(max_length=1000, blank=False)
	dogcolor = models.CharField(max_length=1000, blank=False)
	dogfood = models.CharField(max_length=1000, blank=False)
	dogtoy = models.CharField(max_length=1000, blank=False)
	eventtype = models.CharField(max_length=1000, blank=False)
	timestamp = models.DateTimeField()
	userid = models.CharField(max_length=1000, blank=True)
	requestor = models.GenericIPAddressField(blank=False)

	def __str__(self):
		return str(self.eventtype)

class User(models.Model):
	username = models.CharField(max_length=1000, blank=False)
	age = models.DateTimeField()
	password = models.CharField(max_length=1000, blank=False)
	email = models.CharField(max_length=1000, blank=False)
	gender = models.CharField(max_length=1000, blank=False)
	educationlevel = models.CharField(max_length=1000, blank=False)
	city = models.CharField(max_length=1000, blank=False)
	state = models.CharField(max_length=1000, blank=False)

	def __str__(self):
		return str(self.eventtype)

class EventAdmin(admin.ModelAdmin):
	list_display = ('eventtype', 'timestamp')

class ApiKey(models.Model):
	owner = models.CharField(max_length=1000, blank=False)
	key = models.CharField(max_length=5000, blank=False)

	def __str__(self):
		return str(self.owner) + str(self.key)

class ApiKeyAdmin(admin.ModelAdmin):
	list_display = ('owner','key')
