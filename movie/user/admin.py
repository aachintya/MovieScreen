from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Movies,Show

admin.site.register(Movies)

admin.site.register(Show)
