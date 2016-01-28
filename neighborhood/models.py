from django.db import models
from django.utils import timezone


class Neighborhood(models.Model):
	id = models.AutoField(primary_key=True)
	division_title = models.CharField(max_length=60, default='HOA Division')
	create_date = models.DateField(default=timezone.now)
	budget_id = models.IntegerField(default=-1)

	def __str__(self):
		return self.division_title

