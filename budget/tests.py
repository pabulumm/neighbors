from django.test import TestCase
from django.utils import timezone
import datetime

from .models import Budget, Expense


class BudgetMethodTests(TestCase):
	pass


class ExpenseMethodTests(TestCase):
	def test_expense_approval_on_create(self):
		""" If an expense is created, then the approval
		status should return False
		"""
		expense = Expense(title="Sample Expense")
		self.assertEqual(expense.approved, False)

	def test_expense_approval_after_approve(self):
		""" If an expense is approved, then the
		approval status should return True
		"""
		expense = Expense(title="Sample Expense")
		expense.approve()
		self.assertEqual(expense.approved, True)

	def test_expense_approval_after_unapprove(self):
		""" If an expense is unapproved, then the
		approval status should return False
		"""
		expense = Expense(title="Sample Expense", approved=True)
		expense.unapprove()
		self.assertEqual(expense.approved, False)

	def test_was_recently_approved_future_expense(self):
		""" If an expense was approved in the future by
		magical wizards it was NOT approved recently
		:return: False
		"""
		time = timezone.now() + datetime.timedelta(days=30)
		future_expense_thirty_days = Expense(title="Expense", approval_date=time, approved=True)
		time = timezone.now() + datetime.timedelta(days=1)
		future_expense_one_day = Expense(title="Expense", approval_date=time, approved=True)
		self.assertEqual(future_expense_thirty_days.was_recently_approved(), False)
		self.assertEqual(future_expense_one_day.was_recently_approved(), False)

	def test_was_recently_approved_past_expense(self):
		""" If an expense was approved more than 7 days or
		one week prior then it was NOT recently approved
		:return:
		"""
		time = timezone.now() - datetime.timedelta(days=30)
		past_expense_thirty_days = Expense(title="Expense", approval_date=time, approved=True)
		time = timezone.now() - datetime.timedelta(days=7)
		past_expense_seven_days = Expense(title="Expense", approval_date=time, approved=True)
		self.assertEqual(past_expense_thirty_days.was_recently_approved(), False)
		self.assertEqual(past_expense_seven_days.was_recently_approved(), False)

	def test_was_recently_approved_current_expense(self):
		""" If an expense was approved in the
		past week it was recently approved
		:return: True
		"""
		time = timezone.now() - datetime.timedelta(days=6)
		current_expense_six_days = Expense(title="Expense", approval_date=time, approved=True)
		time = timezone.now() - datetime.timedelta(days=1)
		current_expense_one_day = Expense(title="Expense", approval_date=time, approved=True)
		self.assertEqual(current_expense_six_days.was_recently_approved(), True)
		self.assertEqual(current_expense_one_day.was_recently_approved(), True)

