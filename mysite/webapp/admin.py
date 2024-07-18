from django.contrib import admin

# Register your models here.
from webapp.models import Task, Status, Type, Project

admin.site.register(Status)
admin.site.register(Task)
admin.site.register(Type)
admin.site.register(Project)