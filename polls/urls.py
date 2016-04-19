from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^new/$', views.new_poll, name='new'),
	url(r'^(?P<pk>[0-9]+)/$', views.polls_index_detail, name='detail'),
	url(r'^fetch-poll/$', views.get_poll, name='get_poll'),
	url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
	url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
	url(r'^poll-vote/$', views.poll_vote, name='poll-vote')
]
