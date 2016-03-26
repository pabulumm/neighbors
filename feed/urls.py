from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^announce/$', views.make_announcement, name='announce'),
]

