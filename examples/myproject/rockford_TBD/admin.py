from django.contrib import admin
from .models import Room
admin.site.register(Room)
from .models import Choice
admin.site.register(Choice)