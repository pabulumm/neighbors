from django import forms
from .models import FeedPost


class AnnouncementForm(forms.ModelForm):

	class Meta:
		model = FeedPost
		fields = (
			'title',
			'description',
		)