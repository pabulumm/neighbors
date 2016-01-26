from django.db import models
from django.utils import timezone


class Neighborhood(models.Model):
	residence_fee = models.DecimalField(max_digits=8, decimal_places=2, default=10.00)
	id = models.AutoField(primary_key=True)
	division_title = models.CharField(max_length=60, default='HOA Division')
	create_date = models.DateField(default=timezone.now)
	has_budget = models.BooleanField(default=False)

	def __str__(self):
		return self.division_title

