from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse
import json

from .models import Marker


@login_required
def new_marker(request):
	if request.method == 'POST' and request.is_ajax():
		n_id = request.session['neighborhood_id']
		name = request.POST['name']
		lat = request.POST['lat']
		lon = request.POST['lon']
		marker_type = "Testing"
		new_house_marker = Marker(neighborhood_id=n_id,
								  name=name, lat=lat, lon=lon, marker_type=marker_type)
		new_house_marker.save()
		return HttpResponse(json.dumps({'name': name, 'lat': lat, 'lon': lon}), content_type='application/json')


@login_required
def get_all_markers(request):
	if request.method == 'GET' and request.is_ajax():
		markers = [marker.as_dict() for marker in Marker.objects.all()]
		return HttpResponse(json.dumps({'markers': markers}), content_type='application/json')