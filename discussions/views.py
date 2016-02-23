from django.shortcuts import get_object_or_404, render, HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
import json

from .models import Discussion, Comment
from .forms import DiscussionForm, CommentForm


@login_required
def discussion_index(request):
	"""
		---DISCUSSION INDEX---
	:param request:
	:return discussion_list:
	"""
	discussion_list = Discussion.objects.filter(neighborhood_id=request.session['neighborhood_id'])
	return render(request, 'discussions/index.html', {'discussion_list': discussion_list})


@login_required
def discussion_detail(request, d_id):
	"""
		---DISCUSSION DETAIL---
	:param request:
	:param d_id:
	:return discussion:
	:return discussion comments:
	:return comment_form:
	"""
	discussion = get_object_or_404(Discussion, pk=d_id)
	if request.method == 'POST':
		comment_form = CommentForm(request.POST)
		if comment_form.is_valid():
			comment = comment_form.save()
			comment.discussion = discussion
			comment.creator = request.user
			comment.save()
			discussion.update_last_modified()
		else:
			return HttpResponse("There was an ERROR when saving your comment")
	else:
		comment_form = CommentForm()
	comments = Comment.objects.filter(discussion=discussion)
	return render(request, 'discussions/detail.html', {'discussion': discussion,
													   'comments': comments,
													   'comment_form': comment_form})

@login_required
def new_discussion(request):
	"""
		---NEW DISCUSSION---
	:param request;
	:return discussion_form
	"""
	if request.method == 'POST':
		discussion_form = DiscussionForm(request.POST)
		if discussion_form.is_valid():
			discussion = discussion_form.save()
			discussion.neighborhood_id = request.session['neighborhood_id']
			discussion.creator = request.user
			discussion.save()
			return HttpResponseRedirect('/discussions/index/')
		else:
			return HttpResponse("There was an ERROR when saving your discussion topic")
	else:
		discussion_form = DiscussionForm()
	return render(request, 'discussions/new_discussion.html', {'discussion_form': discussion_form})


@login_required
def get_recent_discussions(request):
	"""
		Return the 5 most recently modified discussions
	:param request:
	:return:
	"""
	n_id = request.session['neighborhood_id']
	recent_discussion_dict = [dis for dis in Discussion.objects
									 .filter(neighborhood_id=n_id)
									 .order_by('-last_modified')[:5]]
	return HttpResponse(json.dumps({'disc_list': recent_discussion_dict}), content_type='application/json')
























