from django.conf.urls import url, include

from . import views

urlpatterns = [
	url(r'^home/$', views.neighborhood_home, name='neighborhood_home'),
	url(r'^info/$', views.neighborhood_info, name='neighborhood_info'),
	url(r'^about/$', views.about, name='about'),
]