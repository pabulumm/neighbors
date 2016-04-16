from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^new-marker/$', views.new_marker, name='new_marker'),
	url(r'^get-markers/$', views.get_all_markers, name='get_all_markers'),
]