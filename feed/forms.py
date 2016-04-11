from django import forms
from .models import FeedPost


class AnnouncementForm(forms.ModelForm):
	class Meta:
		model = FeedPost
		fields = (
			'title',
			'description',
		)


class FeedPostForm(forms.ModelForm):
	class Meta:
		model = FeedPost
		fields = (
			'title',
			'description',
			'type'
		)
