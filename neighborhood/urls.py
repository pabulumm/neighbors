from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^home', views.neighborhood_home, name='neighborhood_home'),
]