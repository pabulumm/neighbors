from .models import Budget, Expense
from django import forms

class BudgetForm(forms.ModelForm):

	class Meta:
		model = Budget
		fields = ('title',
				  'total_funds',
				  'total_expenses',
				  'residence_fee',)


class ExpenseForm(forms.ModelForm):
	TYPES = (
		('1', 'Improvement'),
		('2', 'Repair'),
		('3', 'Recreation'),
		('4', 'Fee'),
		('5', 'Other'),
	)

	type = forms.ChoiceField(choices=TYPES)

	class Meta:
		model = Expense
		fields = ('title',
				  'description',
				  'cost',
				  'start_date',
				  'end_date',
				  'budget_id')