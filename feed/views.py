from accounts.models import Activity
from django.shortcuts import HttpResponse, HttpResponseRedirect, get_object_or_404
from .models import FeedPost, Feed, PostView
from .forms import AnnouncementForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required
import json

from markers.models import Marker


def get_recent_posts(feed_id):
	feed = get_object_or_404(Feed, pk=feed_id)
	return FeedPost.objects.filter(feed=feed).order_by('-create_date')[:20]


@login_required
def make_announcement(request):
	announcement_form = AnnouncementForm(request.POST)
	if announcement_form.is_valid():
		announcement = announcement_form.save()
		announcement.create_date = timezone.now()
		announcement.feed = Feed.objects.get(
			neighborhood=request.user.userprofile.house.neighborhood)
		announcement.type = 'ANNOUNCEMENT'
		announcement.user = request.user
		announcement.save()
		if announcement.id is not None:
			activity = Activity(type='ANNOUNCEMENT', user=request.user, assoc_obj_id=announcement.id)
			activity.save()

		return HttpResponseRedirect('/neighborhood/home/')
	return HttpResponse("You're not allowed to make announcements homie.")


@login_required
def get_viewed(request):
	"""
	Check if a view object has been created denoting that the requesting user
	has seen the post corresponding to the post_id data passed via AJAX.
	If view does exist, return the date it was created, else return false
	:param request:
	:return:
	"""
	if request.method == 'GET' and request.is_ajax():
		post = FeedPost.objects.get(id=request.GET['feed_post_id'])
		user = request.user
		if PostView.objects.filter(post=post, user=user):
			viewed = True
			post_view = PostView.objects.get(post=post, user=user)
			post_date = str(post_view.date.date())
			return HttpResponse(json.dumps({'viewed': viewed,
											'date': post_date}), content_type='application/json')
		viewed = False
		return HttpResponse(json.dumps({'viewed': viewed}), content_type='application/json')


@login_required
def view_post(request):
	if request.is_ajax() and request.method == 'POST':
		post_viewed = False
		post = FeedPost.objects.get(id=request.POST['post_id'])
		view, created = PostView.objects.get_or_create(user=request.user, post=post)
		if created:  # view was created noting user has seen the post - remove unseen flag
			post_viewed = True
			view.save()
		return HttpResponse(json.dumps({'post_viewed': post_viewed}), content_type='application/json')


@login_required
def submit_post(request):
	post_dict = []
	if request.is_ajax() and request.method == 'POST':
		text = request.POST['text']
		user = request.user
		neighborhood = request.user.userprofile.house.neighborhood
		feed = Feed.objects.get(neighborhood=neighborhood)
		post_type = request.POST['post_type']
		marker_id = request.POST['marker_id']
		post = FeedPost(text=text, user=user, feed=feed, type=post_type)
		print("HAS_MARKER IS: " + request.POST['has_marker'])
		if request.POST['has_marker'] == 1:
			post.marker = Marker.objects.get(id=marker_id)
			print('*******************ADDED MARKER TO POST*******************')
		if post:
			print('**********************SANITY CHECK*************************')
			post.save()
			if post.id is not None:
				activity = Activity(activity_type='POST', user=request.user, assoc_obj_id=post.id)
				activity.save()
			return HttpResponse(json.dumps({'post': post_dict}), content_type='application/json')


@login_required
def get_recent_posts_ajax(request):
	"""
	AJAX call for a refresh of the most recent posts to be displayed on the home page.
	:param request:
	:return:
	"""
	if request.method == 'GET' and request.is_ajax():
		neighborhood = request.user.userprofile.house.neighborhood
		feed = Feed.objects.get(neighborhood=neighborhood)
		post_dict = []
		for post in FeedPost.objects.filter(feed=feed).order_by('-create_date')[:20]:
			post_as_dict = post.as_dict()
			if post.marker is not None:
				post_as_dict['marker_id'] = post.marker.id
			elif post.poll is not None:
				post_as_dict['poll_id'] = post.poll.id
			post_dict.append(post_as_dict)
		return HttpResponse(json.dumps({'posts': post_dict}), content_type='application/json')


@login_required
def get_announcements(request):
	if request.method == 'GET' and request.is_ajax():
		neighborhood = request.user.userprofile.house.neighborhood
		feed = Feed.objects.get(neighborhood=neighborhood)
		post_dict = []
		for announcement in FeedPost.objects.filter(feed=feed, type='ANNOUNCEMENT').order_by('-create_date'):
			post_dict.append(announcement.as_dict())
		return HttpResponse(json.dumps({'announcements': post_dict}), content_type='application/json')
