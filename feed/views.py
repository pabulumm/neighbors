from django.shortcuts import render, get_object_or_404
from .models import FeedPost, Feed


def get_recent_posts(feed_id):
	return FeedPost.objects.all().filter(
		feed=get_object_or_404(Feed, pk=feed_id)
	).order_by('-create_date')[:10]

