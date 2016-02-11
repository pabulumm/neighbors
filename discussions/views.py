from django.shortcuts import get_object_or_404, render, HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from .models import Discussion, Comment
from .forms import DiscussionForm, CommentForm


"""
	---DISCUSSION INDEX---
"""
@login_required
def discussion_index(request):
	discussion_list = Discussion.objects.filter(neighborhood_id=request.session['neighborhood_id'])
	return render(request, 'discussions/index.html', {'discussion_list': discussion_list})


"""
	---DISCUSSION DETAIL---
"""
@login_required
def discussion_detail(request, d_id):
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

"""
	---NEW DISCUSSION---
"""
@login_required
def new_discussion(request):
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



