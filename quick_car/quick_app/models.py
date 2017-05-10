from __future__ import unicode_literals

from django.db import models
from rest_framework import serializers

# Create your models here.

class Notification(models.Model):
    garage_name = models.CharField(max_length=50)
    mechanic_name = models.CharField(max_length=50)
    cilent_name = models.CharField(max_length=50)
    license_plae_number = models.CharField(max_length=50)
    telephone = models.CharField(max_length=50)
    topics = models.CharField(max_length=50)
    detail = models.CharField(max_length=50)
    to_user = models.CharField(max_length=50)
    is_read = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    date = models.CharField(max_length=50)
    def __unicode__(self):
		return "topics: %s to: %s"%(self.topics, self.to_user)

class NotificationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Notification
		fields = ('topics','detail','to_user','is_read')

class Mechanic(models.Model):
    owner_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    citizen_id = models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    commercial_registration_no = models.CharField(max_length=50)
    account = models.CharField(max_length=50)
    locations = models.CharField(max_length=100)
    def __unicode__(self):
		return "%s"%(self.owner_name)

class User(models.Model):
    username = models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    locations = models.CharField(max_length=100)
    notification = models.ForeignKey(Notification, on_delete=models.CASCADE,null=True)
    def __unicode__(self):
		return "name: %s "%(self.username)

class Job(models.Model):
    topics = models.CharField(max_length=50)
    date = models.CharField(max_length=50)
    time =  models.CharField(max_length=50)
    locations = models.CharField(max_length=50)
    detail = models.CharField(max_length=50)
    mechanic = models.CharField(max_length=50)
    user = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
