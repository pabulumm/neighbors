from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .models import Report
from .forms import ReportForm
from messaging.models import Message


@login_required
def make_announcement(request):
	reportform = ReportForm(request.POST)
	if reportform.is_valid():
		report = reportform.save()
		return HttpResponseRedirect('/neighborhood/home/')
	return HttpResponse("You're not allowed to make reports homie.")


@login_required
def reply(request):
	if request.method == 'POST' and request.is_ajax():
		text = request.POST['text']
		lm_id = request.POST['lm_id']
		receiver_name = request.POST['receiver_name']
		receiver = User.objects.get(username=receiver_name)
		sender = request.user
		message = Message(text=text, sender=sender, receiver=receiver,
						  last_message_id=lm_id)
		message.save()
		if message.id is not None:
			return HttpResponse('Message has been sent')
	return HttpResponse('Error: Not POST or AJAX')


@login_required
def new_message(request):
	if request.method == 'POST' and request.is_ajax():
		text = request.POST['text']
		receiver_name = request.POST['receiver_name']
		receiver = User.objects.get(username=receiver_name)
		sender = request.user
		message = Message(text=text, sender=sender, receiver=receiver)
		message.save()
		if message.id is not None:
			return HttpResponse('Message has been sent')
	return HttpResponse('Error: Not POST or AJAX')

