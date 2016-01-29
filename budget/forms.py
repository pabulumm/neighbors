from .models import Budget, Expense
from django import forms


class BudgetForm(forms.ModelForm):

	class Meta:
		model = Budget
		fields = (
			'title',
			'residence_fee',
			'neighborhood',
		)


class ExpenseForm(forms.ModelForm):

	class Meta:
		model = Expense
		fields = (
			'title',
			'description',
			'cost',
			'start_date',
			'end_date',
			'types',
			'budget',
		)