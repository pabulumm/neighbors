from django.contrib import admin
from .models import Feed, FeedPost, PostView

admin.site.register(Feed)
admin.site.register(FeedPost)
admin.site.register(PostView)
