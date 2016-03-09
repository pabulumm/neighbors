from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect, HttpResponse

from .models import UserProfile
from .forms import UserForm
from neighborhood.models import Neighborhood, House


def user_login(request):
	"""
		---USER_LOGIN---
	:param request:
	"""
	if request.method == 'POST':
		# get username and password from input text
		username = request.POST['username_text']
		password = request.POST['password_text']

		# authenticate the credentials
		user = authenticate(username=username, password=password)

		# if we have a user the authentication was successful
		if user:
			# Is the account active? It could have been disabled.
			if user.is_active:
				# If the account is valid and active, we can log the user in.
				# We'll send the user back to the homepage.
				login(request, user)
				return HttpResponseRedirect('/neighborhood/home/')
			else:
				# An inactive account was used - no logging in!
				return HttpResponse("Your Neighbors account is disabled.")
		else:
			# Bad login details were provided. So we can't log the user in.
			return HttpResponse("The username and password you have entered do not match any account.")
	# The request is not a HTTP POST, so display the login form.
	# This scenario would most likely be an HTTP GET.
	else:
		# No context variables to pass to the template system.
		return render(request, 'accounts/login.html', {})


@login_required
def user_logout(request):
	"""
	---USER LOGOUT---
	:param request:
	"""
	logout(request)
	return HttpResponseRedirect('/')


def register_user(request):
	"""
	---REGISTER USER---
	:param request:
	"""
	registered = False
	if request.method == 'POST':
		# Using forms to collect new user data
		user_form = UserForm(request.POST)
		if user_form.is_valid():
			neighborhood = Neighborhood.objects.get(division_title=request.POST['neighborhood_text'])
			house = House.objects.filter(neighborhood=neighborhood,
										 permission_code=request.POST['perm_code_text'])
			if house:
				# We have checked that the forms are valid now save the user
				user = user_form.save()
				# Now we hash the password with the set_password method.
				# Once hashed, we can update the user object.
				user.set_password(user.password)
				user.save()
				user_profile = UserProfile(user=user, house=house)
				user_profile.save()
				return HttpResponseRedirect('/')
			else:
				# no house object was returned, invalid info provided
				return HttpResponse("The neighborhood and permission code you have entered do not match any existing neighborhood.")
	# Not a HTTP POST, so we render our form using two ModelForm instances.
	# These forms will be blank, ready for user input.
	else:
		user_form = UserForm()
	# Render the template depending on the context.
	return render(request, 'accounts/register.html', {'user_form': user_form,
													  'registered': registered})


"""
	---USER PROFILE---
"""
@login_required
def user_profile(request):
	user_prof = request.user.userprofile
	return render(request, 'accounts/user_profile.html', {'house': user_prof})

