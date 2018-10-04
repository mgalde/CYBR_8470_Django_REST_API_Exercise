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

BREEDDEFINE = (
	('Tiny', 'Tiny'),
	('Small', 'Small'),
	('Medium', 'Medium'),
	('Large', 'Large'),)

BREEDRATE = (
	(1, 1),
	(2, 2),
	(3, 3),
	(4, 4),
	(5, 5),)

class Breed(models.Model):
	breedname = models.CharField(max_length=1000, blank=False)
	breedsize = models.IntegerField(max_length=5, choices=BREEDDEFINE)
	friendliness = models.IntegerField(choices=BREEDRATE)
	trainability = models.IntegerField(choices=BREEDRATE)
	sheddingamount = models.IntegerField(choices=BREEDRATE)
	exerciseneeds = models.IntegerField(choices=BREEDRATE)
	requestor = models.GenericIPAddressField(blank=False)

	def __str__(self):
		return str(self.breedname)

class Dog(models.Model):
	dogname = models.CharField(max_length=1000, blank=False)
	dogage = models.IntegerField(max_length=5, blank=False)
	dogbreed = models.ForeignKey(Breed, on_delete=models.CASCADE)
	doggender = models.CharField(max_length=1000, blank=False)
	dogcolor = models.CharField(max_length=1000, blank=False)
	dogfood = models.CharField(max_length=1000, blank=False)
	dogtoy = models.CharField(max_length=1000, blank=False)
	requestor = models.GenericIPAddressField(blank=False)

	def __str__(self):
		return str(self.dogname)

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
		return str(self.username)

class Profile(models.Model):
	username = models.CharField(max_length=1000, blank=False)
	age = models.DateTimeField()
	password = models.CharField(max_length=1000, blank=False)
	email = models.CharField(max_length=1000, blank=False)
	gender = models.CharField(max_length=1000, blank=False)
	educationlevel = models.CharField(max_length=1000, blank=False)
	city = models.CharField(max_length=1000, blank=False)
	state = models.CharField(max_length=1000, blank=False)

	def __str__(self):
		return str(self.username)

class Create_User(models.Model):
	username = models.CharField(max_length=1000, blank=False)
	age = models.DateTimeField()
	password = models.CharField(max_length=1000, blank=False)
	email = models.CharField(max_length=1000, blank=False)
	gender = models.CharField(max_length=1000, blank=False)
	educationlevel = models.CharField(max_length=1000, blank=False)
	city = models.CharField(max_length=1000, blank=False)
	state = models.CharField(max_length=1000, blank=False)

	def __str__(self):
		return str(self.username)

class EventAdmin(admin.ModelAdmin):
	list_display = ('eventtype', 'timestamp')

class ApiKey(models.Model):
	owner = models.CharField(max_length=1000, blank=False)
	key = models.CharField(max_length=5000, blank=False)

	def __str__(self):
		return str(self.owner) + str(self.key)

class ApiKeyAdmin(admin.ModelAdmin):
	list_display = ('owner','key')
