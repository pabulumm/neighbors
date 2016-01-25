from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render


@login_required
def neighborhood_home(request):
	# get the user profile from the user object
	user_profile = request.user.userprofile
	neighborhood = user_profile.neighborhood
	return render(request, 'neighborhood/neighborhood_home.html', {'neighborhood': neighborhood,
																	'user_profile': user_profile })

