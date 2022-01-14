from django.db import models
from Exercise_Category.models import Exercise_Category
from Exercise.models import Exercise


# Create your models here.
class Exercise_Day(models.Model):
    Ex_Date = models.DateTimeField()
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s' % (self.exercise.Exercise_Name, self.exercise.Category)


