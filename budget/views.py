from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from neighborhood.models import Neighborhood

from .forms import BudgetForm, ExpenseForm
from .models import Expense, Budget

EXPENSE_KEY = 'expense'

@login_required
def create_budget(request):
	neighborhood = Neighborhood.objects.get(id=request.session['neighborhood_id'])
	if request.method == 'POST':
		budget_form = BudgetForm(request.POST)
		if budget_form.is_valid():
			budget = budget_form.save()
			budget.save()
			neighborhood.budget = budget
			neighborhood.has_budget = True
			return render(request, 'budget/manage_budget.html', {'budget_form': budget_form})
	else:
		budget_form = BudgetForm()
	return render(request, 'budget/create_budget.html', {'budget_form': budget_form})


@login_required
def manage_budget(request, ):
	budget = Budget.objects.get(neighborhoodid=request.session['neighborhood_id'])
	expense_list = Expense.get_budget_expenses_by_date(self, budget.id)
	return render(request, 'budget/manage_budget.html', {'budget': neighborhood.budget} )


@login_required
def new_expense(request):
	budget = get_object_or_404(Neighborhood, pk=request.session['neighborhood_id']).budget
	if request.method == 'POST':
		expense_form = ExpenseForm(request.POST)
		if expense_form.is_valid():
			expense = expense_form.save()
			expense.budget = budget
			expense.save()
	else:
		expense_form = ExpenseForm()
	return render(request, 'budget/new_expense.html', {'expense_form': expense_form})


@login_required
def expense_detail(request, expense_id):
	expense = get_object_or_404(Expense, expense_id)
	return render(request, 'budget/expense_detail.html', {'expense': expense})