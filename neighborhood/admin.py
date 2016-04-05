from django.contrib import admin

from .models import Neighborhood, House, Event
# Register your models here.
admin.site.register(Neighborhood)
admin.site.register(House)
admin.site.register(Event)

