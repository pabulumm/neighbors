from django.shortcuts import render, get_object_or_404, HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from django.forms import formset_factory
from django.contrib.auth.decorators import login_required

from neighborhood.models import Neighborhood

from .models import Question, Choice, Vote
from .forms import QuestionForm, ChoiceForm


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
	ChoiceFormSet = formset_factory(ChoiceForm, extra=2)
	if request.method == 'POST':
		# Validate the poll topic Question and Choices
		question_form = QuestionForm(request.POST)
		choice_formset = ChoiceFormSet(request.POST)
		if question_form.is_valid() and choice_formset.is_valid():
			# Save question_form and create Question object
			question = question_form.save()
			question.neighborhood = get_object_or_404(Neighborhood, pk=request.session['neighborhood_id'])
			question.creator = request.user
			question.save()
			# Save each choice form into Choice object
			for choice_form in choice_formset:
				choice = choice_form.save()
				choice.question = question
				choice.save()
			return HttpResponseRedirect('/neighborhood/home')
			# choice_form.is_valid() failed
		# question_form.is_valid() failed
		else:
			return HttpResponse("Poll topic is not valid")
	# not a request.POST
	# create blank forms to return
	else:
		question_form = QuestionForm()
		choice_formset = ChoiceFormSet()
	return render(request, 'polls/new_poll.html', {'question_form': question_form,
												   'choice_formset': choice_formset})


#def get_recent_polls(request):
	#n_id = request.session['neighborhood_id']
	#recent_polls = [poll for poll in Question.objects.filter(neighborhood_id=n_id).order_by('las')]
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




# end
