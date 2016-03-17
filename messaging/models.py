from django.db import models
from django.utils import timezone
from accounts.models import User


class Message(models.Model):
	text = models.CharField(max_length=1000)
	time_sent = models.DateTimeField(default=timezone.now)
	sender = models.ForeignKey(User, related_name='sender')
	receiver = models.ForeignKey(User, related_name='receiver')


class Alert(models.Model):
	text = models.CharField(max_length=1000)
	time_created = models.DateTimeField(auto_now=True)
	time_alert = models.DateTimeField()
	sender = models.ForeignKey(User)

