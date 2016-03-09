from budget.models import Budget, Expense
from discussions.models import Discussion
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie
import json
from .models import Neighborhood


@login_required
@ensure_csrf_cookie
def neighborhood_home(request):
	# get the user profile from the user object

	neighborhood = request.user.userprofile.house.neighborhood
	request.session['neighborhood_id'] = neighborhood.id
	try:
		recent_discussion_dict = [dis for dis in Discussion.objects
													 .filter(neighborhood_id=neighborhood.id)
													 .order_by('-last_modified')[:5]]
		budget = Budget.objects.filter(neighborhood=neighborhood)
		expense_list = Expense.objects.filter(budget=budget)
	except NameError:
		return render(request, 'neighborhood/about.html', {'neighborhood': neighborhood})
	return render(request, 'neighborhood/about.html', {'neighborhood': neighborhood,
													  'discussions': recent_discussion_dict,
													  'expense_list': expense_list,
													  'budget': budget})


@login_required
def neighborhood_info(request):
	neighborhood = Neighborhood.objects.get(id=request.session['neighborhood_id'])
	return render(request, 'neighborhood/neighborhood_info.html', {'neighborhood': neighborhood})


def get_neighborhoods(request):
	if request.is_ajax():
		q = request.GET.get('term', '')
		neighborhoods = Neighborhood.objects.filter(division_title__icontains=q)[:20]
		results = []
		for neighborhood in neighborhoods:
			drug_json = {'label': neighborhood.division_title,
						 'value': neighborhood.division_title}
			results.append(drug_json)
		data = json.dumps(results)
	else:
		data = 'fail'
	mimetype = 'application/json'
	return HttpResponse(data, mimetype)


def about(request):
	return render(request, 'neighborhood/about.html', {})
