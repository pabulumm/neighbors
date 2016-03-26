from django.db import models
from django.utils import timezone
from accounts.models import User


class Chat(models.Model):
	id = models.AutoField(primary_key=True)
	users = models.ManyToManyField(User)
	created = models.DateTimeField(default=timezone.now)


class Message(models.Model):
	id = models.AutoField(primary_key=True)
	chat = models.ForeignKey(Chat, null=True)
	text = models.CharField(max_length=1000)
	time = models.DateTimeField(default=timezone.now)
	sender = models.ForeignKey(User, related_name='sender')
	receiver = models.ForeignKey(User, related_name='recipient')


class Alert(models.Model):
	text = models.CharField(max_length=1000)
	time_created = models.DateTimeField(auto_now=True)
	time_alert = models.DateTimeField()
	sender = models.ForeignKey(User, null=True)


class Report(models.Model):
	title = models.CharField(max_length=100)
	text = models.CharField(max_length=1000)
	time = models.DateTimeField(auto_now=True)
	sender = models.ForeignKey(User, related_name='reporter', null=True)
	recipients = models.ManyToManyField(User, related_name='recipients')

