from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from .models import Neighborhood


@login_required
def neighborhood_home(request):
	# get the user profile from the user object
	user_profile = request.user.userprofile
	neighborhood = user_profile.neighborhood
	neighborhood.has_budget = True
	request.session['neighborhood_id'] = neighborhood.id
	return render(request, 'neighborhood/neighborhood_home.html', {'neighborhood': neighborhood,
																	'user_profile': user_profile })


@login_required
def neighborhood_info(request):
	neighborhood = Neighborhood.objects.get(id=request.session['neighborhood_id'])
	return render(request, 'neighborhood/neighborhood_info.html', {'neighborhood': neighborhood})

