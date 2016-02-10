from django.test import TestCase
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

