from django.contrib import admin
from .models import TaskStatus, TaskCategory, Tasks

# Register your models here.
admin.site.register(TaskCategory)
admin.site.register(Tasks)
admin.site.register(TaskStatus)

# Register your models here.
