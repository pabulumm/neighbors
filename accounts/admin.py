from django.contrib import admin

from .models import UserProfile, Activity

admin.site.register(UserProfile)
admin.site.register(Activity)