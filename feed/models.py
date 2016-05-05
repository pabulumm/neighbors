from django.db import models
from django.utils import timezone
from accounts.models import User
from neighborhood.models import Neighborhood
from markers.models import Marker
from polls.models import Poll, Question


class Feed(models.Model):
	id = models.AutoField(primary_key=True)
	neighborhood = models.ForeignKey(Neighborhood)
	create_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return str(self.id)


class FeedPost(models.Model):
	id = models.AutoField(primary_key=True)
	feed = models.ForeignKey(Feed, null=True)
	type = models.CharField(max_length=50, default='ANNOUNCEMENT')
	text = models.TextField(max_length=1000)
	user = models.ForeignKey(User, null=True)
	create_date = models.DateTimeField(default=timezone.now)
	marker = models.ForeignKey(Marker, null=True)
	poll = models.ForeignKey(Question, null=True)
	decision = models.ForeignKey(Poll, null=True)

	def __str__(self):
		return self.text

	def as_dict(self):
		return {
			'post_id': int(self.id),
			'text': self.text,
			'user': self.user.first_name + " " + self.user.last_name,
			'post_type': self.type,
			'date': str(self.create_date.date())
		}


class PostView(models.Model):
	id = models.AutoField(primary_key=True)
	date = models.DateTimeField(auto_now=True)
	post = models.ForeignKey(FeedPost)
	user = models.ForeignKey(User)

	def __str__(self):
		return "Post " + str(self.post.id) + " viewed by " + self.user.username

	def as_dict(self):
		return {
			'user': self.user.username,
			'date': str(self.date.date()),
			'post': self.post.id
		}