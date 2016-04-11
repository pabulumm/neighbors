from django.shortcuts import HttpResponse, HttpResponseRedirect, get_object_or_404
from .models import FeedPost, Feed, PostView
from .forms import AnnouncementForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import json


def get_recent_posts(feed_id):
	feed = get_object_or_404(Feed, pk=feed_id)
	return FeedPost.objects.all().filter(feed=feed).order_by('-create_date')[:20]


@login_required
def make_announcement(request):
	if request.user.userprofile.member_status != 'neighbor':
		announcement_form = AnnouncementForm(request.POST)
		if announcement_form.is_valid():
			announcement = announcement_form.save()
			announcement.create_date = timezone.now()
			announcement.feed = Feed.objects.get(
				neighborhood=request.user.userprofile.house.neighborhood)
			announcement.type = 'ANNOUNCEMENT'
			announcement.user = request.user
			announcement.save()
			return HttpResponseRedirect('/neighborhood/home/')
	else:
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
	post = ""
	if request.is_ajax() and request.method == 'POST':
		pass
	return HttpResponse(json.dumps({'post': post}), content_type='application/json')
