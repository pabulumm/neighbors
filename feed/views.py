from django.shortcuts import HttpResponse, HttpResponseRedirect, render, get_object_or_404
from .models import FeedPost, Feed
from .forms import AnnouncementForm
from django.utils import timezone


def get_recent_posts(feed_id):
	return FeedPost.objects.all().filter(
		feed=get_object_or_404(Feed, pk=feed_id)
	).order_by('-create_date')[:10]


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
