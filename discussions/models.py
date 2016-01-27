from django.db import models
from django.utils import timezone


class Comment(models.Model):
	id = models.AutoField(primary_key=True)
	text = models.TextField(verbose_name="Comment Text")
	create_date = models.DateTimeField(default=timezone.now)
	creator_id = models.IntegerField(verbose_name="Creator ID")
	discussion = models.ForeignKey(Discussion, unique=True)


class Discussion(models.Model):
	id = models.AutoField(primary_key=True)
	title = models.CharField(default="Discussion Title", verbose_name="Discussion Title")
	create_date = models.DateTimeField(default=timezone.now)
	creator_id = models.IntegerField(verbose_name="Creator ID")
	neighborhood_id = models.IntegerField(verbose_name="Neighborhood_id")
