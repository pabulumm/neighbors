from django import forms
from .models import Report, Message


class ReportForm(forms.ModelForm):

	class Meta:
		model = Report
		fields = (
			'title',
			'text',
		)


class MessageForm(forms.ModelForm):

	class Meta:
		model = Message
		fields = (
			'text',
		)