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
		name = request.POST['name']
		lat = request.POST['lat']
		lon = request.POST['lon']
		type_of_marker = request.POST['type_of_marker']
		# create the new marker object
		marker = Marker(neighborhood_id=neighborhood.id,
								  name=name, lat=lat, lon=lon,
								  type_of_marker=type_of_marker)
		# save the new marker
		marker.save()

		# now create a new FeedPost for our home page
		feed = Feed.objects.get(neighborhood=neighborhood)
		feedpost = FeedPost(title=name, user=request.user,
							type='MARKER', feed=feed, marker=marker)
		feedpost.save()
		return HttpResponse(json.dumps({'name': name, 'lat': lat, 'lon': lon,
										'type_of_marker': type_of_marker}),
							content_type='application/json')


# @login_required
# def get_all_markers(request):
# 	if request.method == 'GET' and request.is_ajax():
# 		# markers = Marker.objects.all()
# 		neighborhood = request.user.userprofile.house.neighborhood
# 		to_json = []
# 		for marker in Marker.objects.all().filter(neighborhood_id=neighborhood.id):
# 			# for each object, construct a dictionary containing the data you wish to return
# 			marker_dict = {}
# 			marker_dict['name'] = marker.name
# 			marker_dict['lat'] = marker.lat
# 			marker_dict['lon'] = marker.lon
# 			marker_dict['marker_type'] = marker.type_of_marker
# 			# append the dictionary of each marker to the list
# 			to_json.append(marker_dict)
# 		# data = serializers.serialize("json", markers)
# 		# markers = [marker.as_dict() for marker in Marker.objects.all()]
# 		return HttpResponse(json.dumps({'markers': to_json}), content_type='application/json')
# 		# return HttpResponse(data, content_type='application/json')


@login_required
def get_all_markers(request):
	if request.method == 'GET' and request.is_ajax():
		marker_dict = []
		neighborhood = request.user.userprofile.house.neighborhood
		for marker in Marker.objects.all().filter(neighborhood_id=neighborhood.id):
			marker_dict.append(marker.as_dict())
		return HttpResponse(json.dumps({'markers': marker_dict}), content_type='application/json')
