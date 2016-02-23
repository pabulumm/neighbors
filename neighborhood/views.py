from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import ensure_csrf_cookie
from django.shortcuts import render

from .models import Neighborhood
from budget.models import Budget, Expense
from discussions.models import Discussion



@login_required
@ensure_csrf_cookie
def neighborhood_home(request):
	# get the user profile from the user object
	user_profile = request.user.userprofile
	neighborhood = user_profile.neighborhood
	request.session['neighborhood_id'] = neighborhood.id
	try:
		recent_discussion_dict = [dis for dis in Discussion.objects
									 .filter(neighborhood_id=neighborhood.id)
									 .order_by('-last_modified')[:5]]
		budget = Budget.objects.get(neighborhood=neighborhood)
		expense_list = Expense.objects.filter(budget=budget)
	except NameError:
		return render(request, 'neighborhood/neighborhood_home.html', {'neighborhood': neighborhood,
																	'user_profile': user_profile})
	return render(request, 'neighborhood/neighborhood_home.html', {'neighborhood': neighborhood,
																	'user_profile': user_profile,
																	'discussions': recent_discussion_dict,
																    'expense_list': expense_list,
																    'budget': budget})


@login_required
def neighborhood_info(request):
	neighborhood = Neighborhood.objects.get(id=request.session['neighborhood_id'])
	return render(request, 'neighborhood/neighborhood_info.html', {'neighborhood': neighborhood})


def about(request):
	return render(request, 'neighborhood/about.html', {})


