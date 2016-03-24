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


class FeedPost(models.Model):
	id = models.AutoField(primary_key=True)
	feed = models.ForeignKey(Feed)
	type = models.CharField(max_length=50)
	description = models.CharField(max_length=300)
	user = models.ForeignKey(User)
	create_date = models.DateTimeField(default=timezone.now)
	marker = models.ForeignKey(Marker, null=True)
	poll = models.ForeignKey(Question, null=True)