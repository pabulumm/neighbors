from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^new_marker/$', views.new_marker, name='new_marker'),
	url(r'^get_markers/$', views.get_all_markers, name='get_all_markers'),
]