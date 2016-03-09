from django.db import models
from django.utils import timezone


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

	def __str__(self):
		return self.address
