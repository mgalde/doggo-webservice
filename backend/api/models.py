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
	('Large', 'Large'),
)

BREEDRATE = (
	(1, 1),
	(2, 2),
	(3, 3),
	(4, 4),
	(5, 5),
)

class Breed(models.Model):
	breedname = models.CharField(max_length=1000, blank=False)
	breedsize = models.CharField(max_length=1000, choices=BREEDDEFINE)
	friendliness = models.IntegerField(choices=BREEDRATE)
	trainability = models.IntegerField(choices=BREEDRATE)
	sheddingamount = models.IntegerField(choices=BREEDRATE)
	exerciseneeds = models.IntegerField(choices=BREEDRATE)
	requestor = models.GenericIPAddressField(null=True, blank=False)

	def __str__(self):
		return str(self.breedname)


class Dog(models.Model):
	dogname = models.CharField(max_length=1000, blank=False)
	dogage = models.IntegerField()
	dogbreed = models.ForeignKey(Breed, on_delete=models.CASCADE)
	doggender = models.CharField(max_length=1000, blank=False)
	dogcolor = models.CharField(max_length=1000, blank=False)
	dogfood = models.CharField(max_length=1000, blank=False)
	dogtoy = models.CharField(max_length=1000, blank=False)
	requestor = models.GenericIPAddressField(null=True, blank=False)

	def __str__(self):
		return str(self.dogname)


class EventAdmin(admin.ModelAdmin):
	list_display = ('eventtype', 'timestamp')

class ApiKey(models.Model):
	owner = models.CharField(max_length=1000, blank=False)
	key = models.CharField(max_length=5000, blank=False)

	def __str__(self):
		return str(self.owner) + str(self.key)

class ApiKeyAdmin(admin.ModelAdmin):
	list_display = ('owner','key')
