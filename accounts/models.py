from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from neighborhood.models import House, Neighborhood


class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	house = models.ForeignKey(House, null=True)
	join_date = models.DateField(default=timezone.now)
	bio = models.TextField(max_length=1000, default='Default biography')
	member_status = models.CharField(max_length=100, default='neighbor')
	neighborhood_id = models.IntegerField(null=True)

	def is_board_member(self):
		return self.member_status is not 'neighbor'

	def __str__(self):
		return self.user.first_name + " " + self.user.last_name

