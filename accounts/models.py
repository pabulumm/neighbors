from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from neighborhood.models import Neighborhood


class UserProfile(models.Model):
	user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
	family_name = models.CharField(max_length=50, default='family_name')
	neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE)
	join_date = models.DateField(default=timezone.now)
	address = models.CharField(max_length=100, default="Unknown")

	def __str__(self):
		return self.family_name
