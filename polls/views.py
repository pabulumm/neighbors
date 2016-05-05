from accounts.models import Activity
from django.shortcuts import render, get_object_or_404, HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from django.forms import formset_factory
from django.contrib.auth.decorators import login_required
import json

from neighborhood.models import Neighborhood

from .models import Question, Choice, Vote, VotePoll, Poll
from .forms import QuestionForm, ChoiceForm, PollForm
from feed.models import Feed, FeedPost


class IndexView(generic.ListView):
	template_name = 'polls/index.html'
	context_object_name = 'latest_question_list'

	def get_queryset(self):
		"""
		Return the last five published questions (not including
		those set to be in the future).
		"""
		return Question.objects.filter(
			pub_date__lte=timezone.now()
		).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
	model = Question
	template_name = 'polls/detail.html'

	def get_queryset(self):
		"""
		Excludes any questions that aren't published yet.
		"""
		return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
	model = Question
	template_name = 'polls/results.html'


@login_required
def new_poll(request):
	if request.method == 'POST':
		# Validate the poll topic Question and Choices
		poll_form = PollForm(request.POST)
		if poll_form.is_valid():
			neighborhood = request.user.userprofile.house.neighborhood
			# Save question_form and create Question object
			poll = poll_form.save()
			poll.neighborhood = neighborhood
			poll.creator = request.user
			poll.save()
			if poll.id is not None:
				# create feedpost to post this new poll to the neighborhood feed
				feed = Feed.objects.get(neighborhood=neighborhood)
				feedpost = FeedPost(text=poll.question_text, user=request.user,
									type='POLL', feed=feed, decision=poll)
				feedpost.save()

				# create activity for user profile
				activity = Activity(type='POLL-CREATE', user=request.user, assoc_obj_id=poll.id)
				activity.save()
				return HttpResponseRedirect('/neighborhood/home')
		else:
			return HttpResponse("Poll is not valid")


# @login_required
# def new_question(request):
# 	ChoiceFormSet = formset_factory(ChoiceForm, extra=2)
# 	if request.method == 'POST':
# 		# Validate the poll topic Question and Choices
# 		question_form = QuestionForm(request.POST)
# 		choice_formset = ChoiceFormSet(request.POST)
# 		if question_form.is_valid() and choice_formset.is_valid():
# 			neighborhood = get_object_or_404(Neighborhood, pk=request.session['neighborhood_id'])
# 			# Save question_form and create Question object
# 			question = question_form.save()
# 			question.neighborhood = neighborhood
# 			question.creator = request.user
# 			question.save()
# 			# Save each choice form into Choice object
# 			for choice_form in choice_formset:
# 				choice = choice_form.save()
# 				choice.question = question
# 				choice.save()
#
# 			# create feedpost to post this new poll to the neighborhood feed
# 			feed = Feed.objects.get(neighborhood=neighborhood)
# 			feedpost = FeedPost(title=question.question_text, user=request.user,
# 								type='POLL', feed=feed, poll=question)
# 			feedpost.save()
# 			return HttpResponseRedirect('/neighborhood/home')
# 			# choice_form.is_valid() failed
# 		# question_form.is_valid() failed
# 		else:
# 			return HttpResponse("Poll topic is not valid")
# 	# not a request.POST
# 	# create blank forms to return
# 	else:
# 		question_form = QuestionForm()
# 		choice_formset = ChoiceFormSet()
# 	return render(request, 'polls/new_poll.html', {'question_form': question_form,
# 												   'choice_formset': choice_formset})


@login_required
def polls_index_detail(request, pk):
	question_list = Question.objects.filter(
		pub_date__lte=timezone.now()
	).order_by('-pub_date')
	selected_question = get_object_or_404(Question, pk=pk)
	return render(request, 'polls/detail.html', {'selected_question': selected_question,
												   'question_list': question_list})


@login_required()
def get_poll(request):
	if request.method == 'GET' and request.is_ajax():
		poll = get_object_or_404(Question, pk=request.GET['id'])
		poll_dict = poll.as_dict()
		return HttpResponse(json.dumps({'poll': poll_dict}), content_type='application/json')


@login_required
def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		# Redisplay the question voting form
		return render(request, 'polls/detail.html', {
			'question': question,
			'error_message': "You didn't select a choice",
		})
	else:
		vote_obj, created = Vote.objects.get_or_create(user=request.user,
												   question=question,
												   choice=selected_choice)
		if not created:
			return HttpResponse("You sneaky buggah! You already voted!")
		else:
			selected_choice.votes += 1
			selected_choice.save()
			# Always return an HttpResponseRedirect after successfully dealing
			# with POST data. This prevents data from being posted twice if a
			# user hits the Back button.
			return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


@login_required
def poll_vote(request):
	if request.method == 'POST' and request.is_ajax():
		vote_choice = request.POST['vote']
		poll_id = request.POST['poll_id']
		print('********SERVER RECEIVED VOTE FOR POLL: ' + poll_id + '********')
		poll = get_object_or_404(Poll, pk=poll_id)
		vote, created = VotePoll.objects.get_or_create(choice=vote_choice,
						user=request.user,
						poll=poll)
		if created:
			activity = Activity(type='POLL-VOTE', user=request.user, assoc_obj_id=vote.id)
			activity.save()
			return HttpResponse(json.dumps({'vote_id': vote.id}), content_type='application/json')
	return HttpResponse(json.dumps({'vote_id': -1}), content_type='application/json')


@login_required
def get_votes(request):
	if request.method == 'GET' and request.is_ajax():
		poll = Poll.objects.get(id=request.GET['poll_id'])
		total_votes = VotePoll.objects.filter(poll=poll).__len__()
		confirm_votes = VotePoll.objects.filter(poll=poll, choice='CONFIRM').__len__()
		deny_votes = VotePoll.objects.filter(poll=poll, choice='DENY').__len__()
		return HttpResponse(json.dumps({'total_count': total_votes,
										'confirm_count': confirm_votes,
										'deny_count': deny_votes}), content_type='application/json')