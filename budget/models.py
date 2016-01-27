from django.db import models
from django.utils import timezone
from neighborhood.models import Neighborhood


class Budget(models.Model):
	id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=60, default='Community Budget',verbose_name="Budget Title")
	total_funds = models.DecimalField(max_digits=14, decimal_places=2, default=0.00, verbose_name="Total Funds")
	total_expenses = models.DecimalField(max_digits=14, decimal_places=2, default=0.00, verbose_name="Total Expenses")
	residence_fee = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Residence Fee")
	created_date = models.DateTimeField(default=timezone.now, verbose_name="Created on")
	neighborhood_id = models.IntegerField(default=-1)

	def __str__(self):
		return self.title


class ExpenseManager(models.Manager):

	@staticmethod
	def get_budget_expenses_by_date(budget_id):
		return Expense.objects.filter(budget=Budget.objects.get(id=budget_id))

	@staticmethod
	def get_expense_by_id(expense_id):
		return Expense.objects.filter(id=expense_id)

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
		(IMPROVEMENT, 'Freshman'),
		(REPAIR, 'Sophomore'),
		(RECREATION, 'Junior'),
		(FEE, 'Senior'),
		(OTHER, 'Senior'),
	)
	types = models.CharField(max_length=3,
									  choices=EXPENSE_TYPES,
									  default=REPAIR)
	id = models.AutoField(primary_key=True)
	budget_id = models.IntegerField()
	title = models.CharField(max_length=60, default='HOA Division',verbose_name="Neighborhood Title")
	description = models.TextField(verbose_name="Description", default="Description of why and how this expense is needed")
	cost = models.DecimalField(max_digits=12, decimal_places=2)
	created_date = models.DateTimeField(default=timezone.now, verbose_name="Created on")
	start_date = models.DateField(verbose_name="Starts on")
	end_date = models.DateField(verbose_name="Ends on")
	type = models.CharField(max_length=50, verbose_name='Type of Expense')
	approved = models.BooleanField(default=False)

	def __str__(self):
		return self.title

