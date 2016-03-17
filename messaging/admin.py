from django.contrib import admin
from .models import Message,Alert

admin.site.register(Message)
admin.site.register(Alert)