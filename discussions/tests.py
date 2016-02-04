from django.test import TestCase
from .models import Discussion, Comment


def create_discussion(title, description):
	"""
	Creates a sample discussion for testing
	:param title:
	:param description:
	:return: discussion object
	"""
	return Discussion.objects.create(title=title, description=description)


def create_comment(discussion, text):
	"""
	Creates a comment to be associated with the given
	discussion
	:param discussion:
	:param text:
	:return: comment object
	"""
	return Comment.objects.create(text=text, discussion=discussion)


class DiscussionTestCase(TestCase):

	def test_discussion_no_comments(self):
		discussion = Discussion.objects.create(title="Discussion",
								  description="discussion topic description")


