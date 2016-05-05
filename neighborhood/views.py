import datetime
import json
from calendar import monthcalendar, month_name

from accounts.models import UserProfile, Activity
from budget.models import Budget, Expense
from discussions.models import Discussion
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect
from django.utils import timezone
from django.views.decorators.csrf import ensure_csrf_cookie
from feed.forms import AnnouncementForm
from feed.models import Feed, FeedPost
from feed.views import get_recent_posts
from markers.models import Marker
from messaging.models import Message
from messaging.forms import ReportForm
from polls.forms import PollForm
from polls.models import Poll, Question
from .forms import EventForm
from .models import Neighborhood, Event


@login_required
@ensure_csrf_cookie
def neighborhood_home(request):
	if request.method == 'POST':
		report_form = ReportForm(request.POST)
		if report_form.is_valid():
			report = report_form.save()
			report.sender = request.user
			report.time = timezone.now()
			report.save()
	report_form = ReportForm()
	announcement_form = AnnouncementForm()
	pollform = PollForm()
	neighborhood = request.user.userprofile.house.neighborhood
	request.session['neighborhood_id'] = neighborhood.id
	feed = Feed.objects.get(neighborhood=neighborhood)
	feedposts = get_recent_posts(feed.id)
	eventform = EventForm()
	request.session['feed_id'] = feed.id
	user_prof = request.user.userprofile
	# return the 20 most recent activities from the user
	activities = Activity.objects.filter(user=request.user).order_by('date')[:20]
	# return the 20 most recent user messages
	messages = Message.objects.filter(receiver=request.user).order_by('time')[:20]
	board_permissions = user_prof.is_board_member()
	polls = Poll.objects.filter(neighborhood=neighborhood,
								pub_date__lte=timezone.now()).order_by('-pub_date')

	markers = Marker.objects.all().filter(neighborhood_id=neighborhood.id)
	return render(request, 'neighborhood/map_home.html', {'neighborhood': neighborhood,
														  'user': user_prof,
														  'activities': activities,
														  'messages':messages,
														  'markers': markers,
														  'feedposts': feedposts,
														  'report_form': report_form,
														  'announcement_form':announcement_form,
														  'pollform':pollform,
														  'eventform':eventform,
														  'board_permissions': board_permissions,
														  'polls': polls})


@login_required
def neighborhood_status(request):
	neighborhood = request.user.userprofile.house.neighborhood
	try:
		recent_discussion_dict = [dis for dis in Discussion.objects
													 .filter(neighborhood_id=neighborhood.id)
													 .order_by('-last_modified')[:5]]
		budget = Budget.objects.filter(neighborhood=neighborhood)
		expense_list = Expense.objects.filter(budget=budget)
		poll_list = Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
	except NameError:
		return render(request, 'neighborhood/status.html', {'neighborhood': neighborhood})
	return render(request, 'neighborhood/status.html', {'neighborhood': neighborhood,
														'budget': budget,
														'discussions': recent_discussion_dict,
														'expense_list': expense_list,
														'latest_question_list': poll_list})


@login_required
def index(request):
	neighborhood = request.user.userprofile.house.neighborhood
	polls = Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')
	announcements = FeedPost.objects.filter(type='ANNOUNCEMENT')
	budget = Budget.objects.filter(neighborhood=neighborhood)
	selected_question = polls[0]
	return render(request, 'neighborhood/index.html', {'polls': polls,
														'announcements':announcements,
														'budget':budget,
													    'selected_question':selected_question})


@login_required
def neighborhood_details(request):
	neighborhood = request.user.userprofile.house.neighborhood
	try:
		board_members = UserProfile.objects.all().filter(neighborhood_id=neighborhood.id)
		poll_list = Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
	except NameError:
		return render(request, 'neighborhood/details.html', {'neighborhood': neighborhood})
	return render(request, 'neighborhood/details.html', {'neighborhood': neighborhood,
														'latest_question_list': poll_list,
														'board_members': board_members})


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


def get_event_teasers(year, month, neighborhood):
	all_events = Event.objects.filter(neighborhood=neighborhood)
	event_teasers = []
	for event in all_events:
		edate = event.start.date()
		if edate.year == year and edate.month == month:
			event_teasers.append(event.as_teaser())
	return event_teasers


@login_required
def get_current_calendar(request):
	if request.method == 'GET' and request.is_ajax():
		now = datetime.datetime.now()
		month = month_name[now.month]
		neighborhood = request.user.userprofile.house.neighborhood
		event_teasers = get_event_teasers(now.year, now.month, neighborhood)
		days = []
		for week in monthcalendar(now.year, now.month):
			for day in week:
				days.append(day)
		return HttpResponse(json.dumps({'month': month,
										'month_int': now.month,
										'year': now.year,
										'event_teasers': event_teasers,
										'days': days}),
							content_type='application/json')


@login_required
def get_specific_calendar(request):
	if request.method == 'GET' and request.is_ajax():
		month_int = request.GET['month']
		year_int = request.GET['year']
		print('**** Got values year:'+year_int+' & month:'+month_int+' ****"')
		month = month_name[int(month_int)]
		print('**** Fetching Event Teasers ****"')
		event_teasers = get_event_teasers(int(month_int), int(month_int))
		days = []
		print('**** Generating new list of days with year'+year_int+' & month'+month_int+' ****"')
		for week in monthcalendar(int(year_int), int(month_int)):
			for day in week:
				days.append(day)
		return HttpResponse(json.dumps({'month': month,
										'month_int': int(month_int),
										'year': int(year_int),
										'event_teasers': event_teasers,
										'days': days}),
							content_type='application/json')
	return HttpResponse('Request was not of type GET or this method was called without using ajax.')


@login_required
def get_event(request):
	if request.method == 'GET' and request.is_ajax():
		print("*************"+request.GET['event_id']+"***************")
		event = get_object_or_404(Event, pk=request.GET['event_id'])
		print("*************EVENT FOUND****************")
		event_dict = event.as_dict()
		return HttpResponse(json.dumps({'event': event_dict}))


@login_required
def new_event(request):
	if request.method == 'POST':
		eventform = EventForm(request.POST)
		if eventform.is_valid():

			event = eventform.save()
			event.neighborhood = request.user.userprofile.house.neighborhood
			event.creator = request.user
			event.save()
			if event.id is not None:

				activity = Activity(type='EVENT-CREATE', user=request.user, assoc_obj_id=event.id)
				activity.save()
				return HttpResponseRedirect('/neighborhood/home')
		else:
			return HttpResponse("Event form is not valid!")
	return HttpResponse('Not a POST request')

