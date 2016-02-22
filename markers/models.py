from django.contrib.gis.db import models


class Marker(models.Model):
	neighborhood_id = models.IntegerField()
	name = models.CharField(max_length=50)
	lon = models.FloatField()
	lat = models.FloatField()
	marker_type = models.CharField(default='House', max_length=50)

	# Returns the string representation of the model.
	def __str__(self):  # __unicode__ on Python 2
		return self.name

	def as_dict(self):
		return {
			'name': self.name,
			'lat': self.lat,
			'lon': self.lon,
			'type': self.marker_type,
		}