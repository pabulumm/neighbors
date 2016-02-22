from django.contrib.gis.db import models


class WorldBorder(models.Model):
	# Regular Django fields corresponding to the attributes in the
	# world borders shapefile.
	name = models.CharField(max_length=50)
	area = models.IntegerField()
	pop2005 = models.IntegerField('Population 2005')
	fips = models.CharField('FIPS Code', max_length=2)
	iso2 = models.CharField('2 Digit ISO', max_length=2)
	iso3 = models.CharField('3 Digit ISO', max_length=3)
	un = models.IntegerField('United Nations Code')
	region = models.IntegerField('Region Code')
	subregion = models.IntegerField('Sub-Region Code')
	lon = models.FloatField()
	lat = models.FloatField()

	# GeoDjango-specific: a geometry field (MultiPolygonField)
	mpoly = models.MultiPolygonField()

	# Returns the string representation of the model.
	def __str__(self):  # __unicode__ on Python 2
		return self.name


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


class YardSaleMarker(models.Model):
	name = models.CharField(max_length=50)
	create_date = models.DateTimeField(auto_now=True)
	date = models.DateField()
	start_time = models.TimeField(null=True)
	end_time = models.TimeField(null=True)
	lon = models.FloatField()
	lat = models.FloatField()

	# Returns the string representation of the model.
	def __str__(self):  # __unicode__ on Python 2
		return self.name


class ConstructionMarker(models.Model):
	name = models.CharField(max_length=200)
	create_date = models.DateTimeField(auto_now=True)
	start_date = models.DateField()
	end_date = models.DateField()


class TheftMarker(models.Model):
	time_of_incident = models.DateTimeField(verbose_name='Time/Date of Incident')
	description = models.CharField(max_length=400, verbose_name='Description')
	lon = models.FloatField()
	lat = models.FloatField()


class TrashMarker(models.Model):
	create_date = models.DateTimeField(auto_now=True)
	description = models.CharField(max_length=400, verbose_name='Description')
	lon = models.FloatField()
	lat = models.FloatField()


class ExpenseMarker(models.Model):
	create_date = models.DateTimeField(auto_now=True)
	expense_id = models.IntegerField()
	lon = models.FloatField()
	lat = models.FloatField()


class PoolMarker(models.Model):
	create_date = models.DateTimeField(auto_now=True)
	open = models.TimeField()
	close = models.TimeField()
	lon = models.FloatField()
	lat = models.FloatField()


class SpaMarker(models.Model):
	create_date = models.DateTimeField(auto_now=True)
	open = models.TimeField()
	close = models.TimeField()
	lon = models.FloatField()
	lat = models.FloatField()


class HazardMarker(models.Model):
	create_date = models.DateTimeField(auto_now=True)
	description = models.CharField(max_length=400, verbose_name='Description')
	lon = models.FloatField()
	lat = models.FloatField()
