from django.test import TestCase
from django.utils import timezone
import datetime
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


class DiscussionMethodTestCase(TestCase):

	def test_update_last_modified(self):
		"""
		If a discussion is created it should have a default
		last_modified time. When calling update_last_modified()
		the discussion last_modified should be reset to the
		current time. Thus it should not equal the time of
		instantiation.
		"""
		discussion = Discussion(title="Sample Discussion")
		time = discussion.last_modified
		discussion.update_last_modified()
		self.assertNotEqual(time, discussion.last_modified)

	def test_was_published_recently_with_future_question(self):
		"""
		was_published_recently() should return False for discussions where pub_date
		is in the future
		"""
		time = timezone.now() + datetime.timedelta(days=30)
		future_discussion = Discussion(create_date=time)
		self.assertEqual(future_discussion.was_published_recently(), False)

	def test_was_published_recently_with_old_question(self):
		"""
		was_published_recently() should return False for discussions whose
		pub_date is older than 1 day.
		"""
		time = timezone.now() - datetime.timedelta(days=30)
		old_discussion = Discussion(create_date=time)
		self.assertEqual(old_discussion.was_published_recently(), False)

	def test_was_published_recently_with_recent_question(self):
		"""
		was_published_recently() should return True for discussions whose
		pub_date is within the last day.
		"""
		time = timezone.now() - datetime.timedelta(hours=1)
		recent_discussion = Discussion(create_date=time)
		self.assertEqual(recent_discussion.was_published_recently(), True)

