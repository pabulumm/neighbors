from django.shortcuts import render, HttpResponse
import json

from .models import HouseMarker


def new_marker(request):

	if request.method == 'POST' and request.is_ajax():
		name = request.POST['name']
		lat = request.POST['lat']
		lon = request.POST['lon']
		new_house_marker = HouseMarker(name=name, lat=lat, lon=lon)
		new_house_marker.save()
		return HttpResponse(json.dumps({'name': name, 'lat': lat, 'lon': lon}), content_type='application/json')
		#return HttpResponse(json.dumps({'name': name}), content_type='application/json')
