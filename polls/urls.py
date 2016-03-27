from django.conf.urls import url
from . import views

urlpatterns = [
    #ex. /polls/
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^new/$', views.new_poll, name='new'),
    #ex. /polls/5/
    url(r'^(?P<pk>[0-9]+)/$', views.polls_index_detail, name='detail'),
    #ex. /polls/5/results/
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    #ex. /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]