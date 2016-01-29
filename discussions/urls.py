from django.conf.urls import url

from . import views


urlpatterns = [
	url(r'^index/', views.discussion_index, name='index'),
	url(r'^(?P<d_id>\d+)/$', views.discussion_detail, name='detail'),
	url(r'^new_discussion/', views.new_discussion, name='new_discussion'),
	url(r'^new_comment/', views.new_comment, name='new_comment'),
]