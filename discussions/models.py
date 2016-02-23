from django.db import models
from django.utils import timezone
import datetime


from accounts.models import User
from neighborhood.models import Neighborhood

# STATIC VARIABLES
MAX_DISCUSSION_NAME_LENGTH = 250


class Discussion(models.Model):
	id = models.AutoField(primary_key=True)
	title = models.CharField(
		max_length=MAX_DISCUSSION_NAME_LENGTH,
		default="Discussion Title", verbose_name="Discussion Title")
	description = models.TextField(
		default="Initial presentation of the Discussion Topic",
		verbose_name="Discussion Description")
	create_date = models.DateTimeField(default=timezone.now)
	creator = models.ForeignKey(User, null=True)
	neighborhood = models.ForeignKey(Neighborhood, null=True)
	last_modified = models.DateTimeField(default=timezone.now)

	def __str__(self):  # __unicode__ on Python 2
		return self.title

	def update_last_modified(self):
		self.last_modified = timezone.now()

	def was_published_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days=5) <= self.create_date <= now

	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Published Recently?'

	def as_dict(self):
		return {
			'title': self.title,
			'description': self.description,
			'last_modified': self.last_modified
		}


class Comment(models.Model):
	id = models.AutoField(primary_key=True)
	text = models.TextField(verbose_name="Comment Text")
	create_date = models.DateTimeField(default=timezone.now)
	creator = models.ForeignKey(User, null=True)
	discussion = models.ForeignKey(Discussion, null=True)

	def __str__(self):  # __unicode__ on Python 2
		return self.text


