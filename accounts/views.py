from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, render_to_response, HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

from neighborhood.views import neighborhood_home

from .forms import UserForm, UserProfileForm
from .models import UserProfile


def user_login(request):
	context = RequestContext(request)
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
				return neighborhood_home(request)
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
		return render_to_response('accounts/login.html', {}, context)


@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect('/')


def register_user(request):
	context = RequestContext(request)
	registered = False
	if request.method == 'POST':
		# Using forms to collect new user data
		user_form = UserForm(request.POST)
		profile_form = UserProfileForm(request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			# We have checked that the forms are valid now save the user
			user = user_form.save()
			profile_form = profile_form.save()

			# Now we hash the password with the set_password method.
			# Once hashed, we can update the user object.
			user.set_password(user.password)
			user.save()

			# Now sort out the UserProfile instance.
			# Since we need to set the user attribute ourselves, we set commit=False.
			# This delays saving the model until we're ready to avoid integrity problems.
			profile = UserProfile(user=user, family_name=profile_form.family_name,
								  address=profile_form.address,
								  neighborhood=profile_form.neighborhood)
			profile.save()
			registered = True
	# Not a HTTP POST, so we render our form using two ModelForm instances.
	# These forms will be blank, ready for user input.
	else:
		user_form = UserForm()
		profile_form = UserProfileForm()
	# Render the template depending on the context.
	return render_to_response('accounts/register.html',
							  {'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
							  context)


@login_required
def user_profile(request):
	user_prof = request.user.userprofile
	return render(request, 'accounts/user_profile.html', { 'house': user_prof})

