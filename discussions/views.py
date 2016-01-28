from django.shortcuts import get_object_or_404, render
from django.views import generic

from .models import Discussion, Comment


def discussion_index(request):
	discussion_list = Discussion.objects.filter(neighborhood_id=request.session['neighborhood_id'])
	return render(request, 'discussions/index.html', {'discussion_list': discussion_list})


def discussion_detail(request, discussion_id):
	discussion = get_object_or_404(Discussion, discussion_id)
	comments = Comment.objects.filter(discussion=discussion)
	return render(request, 'discussions/detail.html', {'discussion': discussion,
													   'comments': comments})
