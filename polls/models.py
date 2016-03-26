from django.db import models
from django.utils import timezone
import datetime

from neighborhood.models import Neighborhood
from accounts.models import User


class Question(models.Model):
	id = models.AutoField(primary_key=True)
	question_text = models.CharField(max_length=200)
	description = models.TextField(max_length=500, default="Default question description")
	pub_date = models.DateTimeField('date published', default=timezone.now)
	neighborhood = models.ForeignKey(Neighborhood, null=True)
	creator = models.ForeignKey(User, null=True)

	def __str__(self):  # __unicode__ on Python 2
		return self.question_text

	def was_published_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.pub_date <= now

	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Published Recently?'


class Choice(models.Model):
	question = models.ForeignKey(Question, null=True)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	def __str__(self):  # __unicode__ on Python 2
		return self.choice_text


class Vote(models.Model):
	question = models.ForeignKey(Question, null=True)
	choice = models.ForeignKey(Choice, null=True)
	user = models.ForeignKey(User, null=True)
	time = models.DateTimeField(default=timezone.now)

	class Meta:
		unique_together = (('user','choice'),)
