from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist

from neighborhood.models import Neighborhood

from .forms import BudgetForm, ExpenseForm
from .models import ExpenseManager, Budget, Expense

EXPENSE_KEY = 'expense'


"""
	CREATE BUDGET
	This is the view passed to the user when their neighborhood does not
	have a budget already attached to it. Uses a Django form to get input
	from user and create the budget

	FIELDS TO USER:
		- title
		- total_funds : initial
		- total_expenses : initial
		- residence_fee

	FIELDS TO AUTO ASSIGN:
		- neighborhood_id
		- create_date
"""
@login_required
def create_budget(request):
	neighborhood = Neighborhood.objects.get(id=request.session['neighborhood_id'])
	if request.method == 'POST':
		budget_form = BudgetForm(request.POST)
		if budget_form.is_valid():
			neighborhood.has_budget = True
			budget = budget_form.save()
			budget.neighborhood_id = neighborhood.id
			budget.save()
			neighborhood.budget = budget
		return HttpResponseRedirect('/budget/manage_budget/')
	else:
		budget_form = BudgetForm()
	return render(request, 'budget/create_budget.html', {'budget_form': budget_form})


"""
	MANAGE BUDGET
	This is the view passed to the user when their neighborhood has a viewable
	budget. It displays the attributes of a Budget model in addition to the list
	of expenses with a budget_id attr matching the current budget.id
"""
@login_required
def manage_budget(request, ):
	try:
		budget = Budget.objects.get(neighborhood_id=request.session['neighborhood_id'])
	except ObjectDoesNotExist:
		return HttpResponseRedirect('/budget/new_budget/')
	expense_list = ExpenseManager.get_budget_expenses_by_date(budget.id)
	return render(request, 'budget/manage_budget.html', {'budget': budget,
														 'expense_list': expense_list} )


"""
	NEW EXPENSE
	This is the view passed to the user when they wish to create a new
	expense to be added to the budget once approved. It uses a Django
	form to create the new expense object.
"""
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


"""
	EXPENSE DETAIL
	This is the view passed to the user when they select an expense
	from the expense list displayed on the budget home page. It displays
	the attributes of the expense object to the user.
"""
@login_required
def expense_detail(request, expense_id):
	expense = get_object_or_404(Expense, expense_id)
	return render(request, 'budget/expense_detail.html', {'expense': expense})