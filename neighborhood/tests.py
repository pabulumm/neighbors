from django.test import TestCase

# Create your tests here.

class NeighborhoodViewTests(TestCase):
	def test_neighborhood_home(self):
		resp = self.client.get('/neighborhood/home/')
		self.assertEqual(resp.status_code, 200)

