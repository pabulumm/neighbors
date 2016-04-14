from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^announce/$', views.make_announcement, name='announce'),
	url(r'^get-viewed/$', views.get_viewed, name='get-viewed'),
	url(r'^view-post/$', views.view_post, name='view-post'),
	url(r'^submit-post/$', views.submit_post, name='submit-post'),
	url(r'^refresh-feed/$', views.get_recent_posts_ajax, name='refresh-feed'),
	url(r'^get-announcements/$', views.get_announcements, name='get-announcements'),
]

