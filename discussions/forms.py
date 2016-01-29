from django import forms
from .models import Discussion, Comment


class DiscussionForm(forms.ModelForm):

	class Meta:
		model = Discussion
		fields = (
			'title',
			'description',
		)