from django.db import models
from django.utils import timezone
from accounts.models import User
from neighborhood.models import Neighborhood
from markers.models import Marker
from polls.models import Question


class Feed(models.Model):
	id = models.AutoField(primary_key=True)
	neighborhood = models.ForeignKey(Neighborhood)
	create_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.id


class FeedPost(models.Model):
	id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=50, default='Feed Post Title')
	feed = models.ForeignKey(Feed, null=True)
	type = models.CharField(max_length=50, default='ANNOUNCEMENT')
	description = models.TextField(max_length=300)
	user = models.ForeignKey(User, null=True)
	create_date = models.DateTimeField(default=timezone.now)
	marker = models.ForeignKey(Marker, null=True)
	poll = models.ForeignKey(Question, null=True)

	def __str__(self):
		return self.title

