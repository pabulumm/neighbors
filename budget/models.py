from django.db import models
from django.utils import timezone
import datetime
from neighborhood.models import Neighborhood

class Budget(models.Model):
	title = models.CharField(max_length=60, default='Community Budget',verbose_name="Budget Title")
	residence_fee = models.DecimalField(max_digits=8, decimal_places=2)
	created_date = models.DateTimeField(default=timezone.now, verbose_name="Created on")
	neighborhood = models.OneToOneField(Neighborhood, default=1, on_delete=models.CASCADE)

	def __str__(self):
		return self.title


class Expense(models.Model):
	id = models.AutoField(primary_key=True)
	budget = models.ForeignKey(Budget, on_delete=models.CASCADE)
	title = models.CharField(max_length=60, default='HOA Division',verbose_name="Neighborhood Title")
	description = models.TextField(verbose_name="Description", default="Description of why and how this expense is needed")
	cost = models.DecimalField(max_digits=12, decimal_places=2)
	created_date = models.DateTimeField(default=timezone.now, verbose_name="Created on")
	start_date = models.DateField(verbose_name="Starts on")
	end_date = models.DateField(verbose_name="Ends on")
	type = models.CharField(max_length=50, default='Improvement', verbose_name='Type of Expense')
	approved = models.BooleanField(default=False)

	def __str__(self):
		return self.title