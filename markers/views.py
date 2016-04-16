from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse
from django.core import serializers
import json

from .models import Marker
from feed.models import Feed, FeedPost


@login_required
def new_marker(request):
	if request.method == 'POST' and request.is_ajax():
		neighborhood = request.user.userprofile.house.neighborhood
		# grab attr values for the new marker
		name = request.POST['title']
		lat = request.POST['lat']
		lon = request.POST['lon']
		type_of_marker = request.POST['type_of_marker']
		# create the new marker object
		marker = Marker(neighborhood_id=neighborhood.id,
								  title=name, lat=lat, lon=lon,
								  type_of_marker=type_of_marker)
		# save the new marker
		marker.save()
		return HttpResponse(json.dumps({'marker_id': marker.id}), content_type='application/json')


@login_required
def get_all_markers(request):
	if request.method == 'GET' and request.is_ajax():
		marker_dict = []
		neighborhood = request.user.userprofile.house.neighborhood
		for marker in Marker.objects.all().filter(neighborhood_id=neighborhood.id):
			marker_dict.append(marker.as_dict())
		return HttpResponse(json.dumps({'markers': marker_dict}), content_type='application/json')
