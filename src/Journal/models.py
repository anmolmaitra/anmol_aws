from django.db import models
import datetime

# Create your models here.
class Journal(models.Model):
    JEntry = models.TextField()
    IsVisible = models.BooleanField()
    entryDt = models.DateField(default=datetime.date.today)
