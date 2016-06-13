
from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^house/$', views.user_profile, name='user_profile'),
	url(r'^login/$', views.user_login, name='user_login'),
	url(r'^demo-login/$', views.demo_login, name='demo_login'),
	url(r'^logout/$', views.user_logout, name='user_logout'),
	url(r'^register/$', views.register_user, name='register_user'),
]