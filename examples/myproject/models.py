from django.db import models
from django.contrib import admin

class Intructor(model.Model):
    first_name = model.CharField(max_length=30)
    email = model.CharField()
    last_name = model.CharField(max_length=40)
    def _unicode_(self):
