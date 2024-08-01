from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

from accounts import models
# Register your models here.


class ProfileInline(admin.StackedInline):
    model = models.Profile
    fields = ('avatar', 'git_link', 'description')


@admin.register(get_user_model())
class UserAdmin_(UserAdmin):
    model = get_user_model()
    inlines = [ProfileInline]