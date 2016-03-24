from django.contrib import admin
from .models import Feed, FeedPost


admin.site.register(Feed)
admin.site.register(FeedPost)