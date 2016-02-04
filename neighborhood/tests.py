from django.test import TestCase
from django.core.urlresolvers import reverse
from .models import Neighborhood


class NeighborhoodViewTests(TestCase):
	def setUp(self):
		pass

	def test_neighborhood_home_without_login(self):
		resp = self.client.get('neighborhood:neighborhood_home')
		self.assertEqual(resp.status_code, 404)

