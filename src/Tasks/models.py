from django.db import models
import datetime
from django.urls import reverse

# Create your models here.
class TaskCategory(models.Model):
    categoryName=models.TextField()

    def __str__(self):
        return "%s" % (self.categoryName)

class TaskStatus(models.Model):
    taskStatus = models.TextField()

    def __str__(self):
        return "%s" % (self.taskStatus)

class Tasks(models.Model):
    taskName=models.TextField()
    category =models.ForeignKey(TaskCategory, on_delete=models.CASCADE)
    entryDt = models.DateField(default=datetime.date.today)
    completionDt = models.DateField(default=datetime.date.today)
    taskStatus = models.ForeignKey(TaskStatus, on_delete=models.CASCADE,default="NOT STARTED")

    def get_absolute_url(self):
        return reverse("task-list")
