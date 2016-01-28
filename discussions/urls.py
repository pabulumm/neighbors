from django.conf.urls import url

from . import views


urlpatterns = [
	url(r'^index/', views.discussion_index, name='index'),
	url(r'^(?P<pk>[0-9]+)/$', views.discussion_detail, name='detail'),
]