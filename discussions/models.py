from django.db import models
from django.utils import timezone

from accounts.models import User

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
	creator = models.ForeignKey(User)
	neighborhood_id = models.IntegerField(verbose_name="Neighborhood_id")


class Comment(models.Model):
	id = models.AutoField(primary_key=True)
	text = models.TextField(verbose_name="Comment Text")
	create_date = models.DateTimeField(default=timezone.now)
	creator = models.ForeignKey(User)
	discussion = models.ForeignKey(Discussion)


