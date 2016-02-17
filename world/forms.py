from django.contrib.gis import forms


class GeoMapForm(forms.Form):
	point = forms.PointField(widget=forms.OSMWidget(
		attrs={'map_width': 800, 'map_height': 500}
	))