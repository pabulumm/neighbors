from django.db import models
from django.utils import timezone
from neighborhood.models import Neighborhood

import datetime


class Budget(models.Model):
	id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=60, default='Community Budget',verbose_name="Budget Title")
	total_funds = models.DecimalField(max_digits=14, decimal_places=2, default=0.00, verbose_name="Total Funds")
	total_expenses = models.DecimalField(max_digits=14, decimal_places=2, default=0.00, verbose_name="Total Expenses")
	residence_fee = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Residence Fee", default=10.00)
	created_date = models.DateTimeField(default=timezone.now, verbose_name="Created on")
	neighborhood = models.ForeignKey(Neighborhood)

	def __str__(self):
		return self.title


"""
	EXPENSE CLASS
	Expenses are a cost charge to be added to the budget upon
	approval.

	TO BE ADDED
	- split into RECURRING and SINGLE-TIME classes to inherit
	from standing Expense class.
"""
class Expense(models.Model):
	IMPROVEMENT = 'IMP'
	REPAIR = 'REP'
	RECREATION = 'REC'
	FEE = 'FEE'
	OTHER = 'OTH'
	EXPENSE_TYPES = (
		(IMPROVEMENT, 'Improvement'),
		(REPAIR, 'Repair'),
		(RECREATION, 'Recreation'),
		(FEE, 'Fee'),
		(OTHER, 'Other'),
	)
	types = models.CharField(max_length=3, choices=EXPENSE_TYPES, default=REPAIR)
	id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=60, default='Expense',verbose_name="Expense Title")
	description = models.TextField(verbose_name="Description", default="Description of why and how this expense is needed")
	cost = models.DecimalField(max_digits=12, decimal_places=2)
	create_date = models.DateTimeField(default=timezone.now, verbose_name="Created on")
	start_date = models.DateTimeField(verbose_name="Starts on")
	end_date = models.DateTimeField(verbose_name="Ends on")
	type = models.CharField(max_length=50, verbose_name='Type of Expense')
	approved = models.BooleanField(default=False)
	approval_date = models.DateTimeField(null=True)
	budget = models.ForeignKey(Budget)

	def __str__(self):
		return self.title

	def approve(self):
		self.approved = True
		self.approval_date = timezone.now()

	def unapprove(self):
		self.approved = False

	def was_recently_approved(self):
		if self.approved:
			now = timezone.now()
			return now - datetime.timedelta(days=7) <= self.approval_date <= now
		else:
			return False


