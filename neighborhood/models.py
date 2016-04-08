from django.db import models
from django.utils import timezone

from markers.models import Marker
from accounts.models import User


class Neighborhood(models.Model):
	id = models.AutoField(primary_key=True)
	division_title = models.CharField(max_length=60, default='HOA Division')
	create_date = models.DateField(default=timezone.now)

	def __str__(self):
		return self.division_title


class House(models.Model):
	id = models.AutoField(primary_key=True)
	address = models.CharField(max_length=200)
	neighborhood = models.ForeignKey(Neighborhood)
	permission_code = models.CharField(max_length=25)
	lon = models.FloatField(default=34.220912)
	lat = models.FloatField(default=-119.055079)

	def __str__(self):
		return self.address


class Event(models.Model):
	id = models.AutoField(primary_key=True)
	start = models.DateTimeField(null=True)
	end = models.DateTimeField(null=True)
	created = models.DateTimeField(auto_now=True)
	marker = models.ForeignKey(Marker, null=True)
	location = models.CharField(max_length=100, default="Event Location")
	title = models.CharField(default="Event Title", max_length=200)
	type = models.CharField(default="COMMUNITY", max_length=50)
	description = models.TextField(max_length=1000, default="Event Description.")
	neighborhood = models.ForeignKey(Neighborhood)
	creator = models.ForeignKey(User)

	# TODO - add a field for recurring events eg. weekly, monthly, annually, etc.

	def __str__(self):
		return self.title

	def as_dict(self):
		return {
			'id': self.id,
			'start': str(self.start.date()),
			'end': str(self.end.date()),
			'created': str(self.created.date()),
			'title': self.title,
			'description': self.description,
			'location': self.location,
			'marker_id': self.marker.id,
		}

	def as_teaser(self):
		return {
			'title': self.title,
			'id': self.id,
			'day': self.start.date().day,
		}


class EventGuest(models.Model):
	id = models.AutoField(primary_key=True)
	date_invited = models.DateTimeField(auto_now=True)
	date_response = models.DateTimeField()
	guest = models.ForeignKey(User, null=True, related_name="guest")
	invited_by = models.ForeignKey(User, null=True, related_name="invited_by")

	def __str__(self):
		return self.user


























