from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import ensure_csrf_cookie
from django.shortcuts import render

from world.forms import GeoMapForm
from .models import Neighborhood



@login_required
@ensure_csrf_cookie
def neighborhood_home(request):
	# get the user profile from the user object
	user_profile = request.user.userprofile
	neighborhood = user_profile.neighborhood
	request.session['neighborhood_id'] = neighborhood.id
	map_form = GeoMapForm()
	return render(request, 'neighborhood/neighborhood_home.html', {'neighborhood': neighborhood,
																	'user_profile': user_profile,
																   	'map_form': map_form})


@login_required
def neighborhood_info(request):
	neighborhood = Neighborhood.objects.get(id=request.session['neighborhood_id'])
	return render(request, 'neighborhood/neighborhood_info.html', {'neighborhood': neighborhood})


def about(request):
	return render(request, 'neighborhood/about.html', {})


