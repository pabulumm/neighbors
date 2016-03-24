from django.conf.urls import url, include

from . import views

urlpatterns = [
	url(r'^home/$', views.neighborhood_home, name='home'),
	url(r'^status/$', views.neighborhood_status, name='status'),
	url(r'^details/$', views.neighborhood_details, name='details'),
	url(r'^get_neighborhoods/$', views.get_neighborhoods, name='get_neighborhoods'),
	url(r'^about/$', views.about, name='about'),
]