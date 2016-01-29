from django.shortcuts import get_object_or_404, render, HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Discussion, Comment


"""
	---DISCUSSION INDEX---
"""
def discussion_index(request):
	discussion_list = Discussion.objects.filter(neighborhood_id=request.session['neighborhood_id'])
	return render(request, 'discussions/index.html', {'discussion_list': discussion_list})


"""
	---DISCUSSION DETAIL---
"""
def discussion_detail(request, discussion_id):
	discussion = get_object_or_404(Discussion, discussion_id)
	request.session['current_discussion'] = discussion.id
	comments = Comment.objects.filter(discussion=discussion)
	return render(request, 'discussions/detail.html', {'discussion': discussion,
													   'comments': comments})

"""
	---NEW DISCUSSION---
"""
def new_discussion(request):
	if request.method == 'POST':
		discussion_name = request.POST['topic']
		discussion_description = request.POST['description']
		discussion = Discussion(
			title=discussion_name,
			description=discussion_description,
			neighborhood_id=request.session['neighborhood_id'],
			creator=request.user
		)
		if discussion:
			discussion.save()
			url = reverse('discussion_detail', kwargs={'discussion_id': discussion.id})
			return HttpResponseRedirect(url)
		else:
			return HttpResponse("There was an ERROR when saving your discussion topic")
	return render(request, 'discussions/new_discussion.html', {})


"""
	---NEW COMMENT---
"""
def new_comment(request):
	discussion = get_object_or_404(Discussion, pk=request.session['discussion_id'])
	if request.method == 'POST':
		comment_text = request.POST['text']
		comment = Comment(text=comment_text, discussion=discussion, creator=request.user)
		if comment:
			comment.save()
			url = reverse('discussion_detail', kwargs={'discussion_id': discussion.id})
			return HttpResponseRedirect(url)
		else:
			return HttpResponse("There was an ERROR when saving your comment")
	return render(request, 'discussions/new_comment.html', {})



