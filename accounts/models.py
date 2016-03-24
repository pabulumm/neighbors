from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from neighborhood.models import House, Neighborhood


class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	house = models.ForeignKey(House)
	join_date = models.DateField(default=timezone.now)


class BoardMemberProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	house = models.ForeignKey(House)
	join_date = models.DateTimeField(default=timezone.now)
	bio = models.CharField(max_length=400)
	position = models.CharField(max_length=50, verbose_name="Board member position")
	neighborhood_id = models.ForeignKey(Neighborhood, null=True)

