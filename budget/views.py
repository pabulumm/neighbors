from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .forms import BudgetForm, ExpenseForm


@login_required
def create_budget(request):
	neighborhood = request.user.userprofile.neighborhood
	if request.method == 'POST':
		budget_form = BudgetForm(request.POST)
		if budget_form.is_valid():
			budget = budget_form.save()
			budget.save()
			neighborhood.budget = budget
			return render(request, 'budget/manage_budget.html', {'budget_form': budget_form} )

	return render(request, 'budget/create_budget.html', {} )


@login_required
def manage_budget(request):
	neighborhood = request.user.userprofile.neighborhood
	return render(request, 'budget/manage_budget.html', {'budget': neighborhood.budget} )


@login_required
def new_expense(request):
	budget = request.user.userprofile.neighborhood.budget
	if request.method == 'POST':
		expense_form = ExpenseForm(request.POST)
		if expense_form.is_valid():
			expense = expense_form.save()
			expense.save()

	return render(request, 'budget/manage_budget.html', {'budget': budget})


@login_required
def expense_detail(request):
	budget = request.user.userprofile.neighborhood.budget
	#if request.method == 'POST':
		#if expense_form.is_valid():

	return render(request, 'budget/manage_budget.html', {'budget': budget})