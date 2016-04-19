from django.conf.urls import url, include

from . import views

urlpatterns = [
	url(r'^home/$', views.neighborhood_home, name='home'),
	url(r'^status/$', views.neighborhood_status, name='status'),
	url(r'^index/$', views.index, name='index'),
	url(r'^details/$', views.neighborhood_details, name='details'),
	url(r'^get-neighborhoods/$', views.get_neighborhoods, name='get_neighborhoods'),
	url(r'^get-event/$', views.get_event, name='get_event'),
	url(r'^current-calendar/$', views.get_current_calendar, name='current_calendar'),
	url(r'^specific-calendar/$', views.get_specific_calendar, name='specific_calendar'),
	url(r'^new-event/$', views.new_event, name='new-event'),
]