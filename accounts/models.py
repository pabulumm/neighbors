from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from neighborhood.models import House


class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	house = models.ForeignKey(House)
	join_date = models.DateField(default=timezone.now)

