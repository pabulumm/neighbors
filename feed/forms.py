from django import forms
from .models import FeedPost


class AnnouncementForm(forms.ModelForm):
	class Meta:
		model = FeedPost
		fields = (
			'text',
		)


class FeedPostForm(forms.ModelForm):
	class Meta:
		model = FeedPost
		fields = (
			'text',
			'type'
		)
