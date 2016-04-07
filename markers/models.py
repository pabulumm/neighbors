from django.contrib.gis.db import models
from django.utils import timezone


class Marker(models.Model):
	id = models.AutoField(primary_key=True)
	type_of_marker = models.CharField(max_length=40, default='DEFAULT')
	description = models.TextField(max_length=300, default='Default marker description.')
	neighborhood_id = models.IntegerField()
	create_date = models.DateTimeField(default=timezone.now)
	title = models.CharField(max_length=50)
	lon = models.FloatField()
	lat = models.FloatField()

	# Returns the string representation of the model.
	def __str__(self):  # __unicode__ on Python 2
		return str(self.id) + " " + self.type_of_marker

	def as_dict(self):
		return {
			'id': self.id,
			'title': self.title,
			'lat': self.lat,
			'lon': self.lon,
			'description': self.description,
			'create_date': str(self.create_date.date()),
			'type_of_marker': self.type_of_marker,
		}