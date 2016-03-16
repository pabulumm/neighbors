from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse
import json

from .models import Marker


@login_required
def new_marker(request):
	if request.method == 'POST' and request.is_ajax():
		neighborhood = request.user.userprofile.house.neighborhood
		name = request.POST['name']
		lat = request.POST['lat']
		lon = request.POST['lon']
		type_of_marker = request.POST['type_of_marker']
		new_house_marker = Marker(neighborhood_id=neighborhood.id,
								  name=name, lat=lat, lon=lon, type_of_marker=type_of_marker)
		new_house_marker.save()
		return HttpResponse(json.dumps({'name': name, 'lat': lat, 'lon': lon, 'type_of_marker': type_of_marker}), content_type='application/json')


@login_required
def get_all_markers(request):
	if request.method == 'GET' and request.is_ajax():
		markers = [marker.as_dict() for marker in Marker.objects.all()]
		return HttpResponse(json.dumps({'markers': markers}), content_type='application/json')